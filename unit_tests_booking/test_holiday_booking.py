import unittest
import json
import requests
from datetime import datetime
import csv
import os


class TestHolidayBooking(unittest.TestCase):

    base_url = "http://100.25.26.186:8002/tools/holiday/book"
    test_timings = {}
    test_results = {}  # Dictionary to store test results

    def setUp(self):
        self.start_time = datetime.now()

    def tearDown(self):
        duration = datetime.now() - self.start_time
        test_name = self.id().split(".")[-1]
        self.test_timings[test_name] = {
            "start_time": self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "duration_seconds": duration.total_seconds(),
        }

    def post_request(self, data):
        response = requests.post(
            self.base_url,
            headers={"accept": "application/json", "Content-Type": "application/json"},
            data=json.dumps(data),
        )
        return response

    def test_second_request(self):
        response = self.post_request({"request_id": "s1", "params": {}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_name_provided(self):
        response = self.post_request(
            {"request_id": "s1", "params": {"name": "marshall"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_name_and_country_provided(self):
        response = self.post_request(
            {"request_id": "s1", "params": {"name": "marshall", "country": "UK"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_complete_info(self):
        response = self.post_request(
            {
                "request_id": "s1",
                "params": {"name": "marshall", "country": "UK", "age": "78"},
            }
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_insurance_provided(self):
        response = self.post_request(
            {
                "request_id": "s1",
                "params": {
                    "name": "marshall",
                    "country": "UK",
                    "age": "78",
                    "insurance": "maybe yes",
                },
            }
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_no_more_modifications(self):
        # Re-submit the same request_id to ensure no changes can be made
        response = self.post_request(
            {
                "request_id": "s1",
                "params": {
                    "name": "marshall",
                    "country": "UK",
                    "age": "78",
                    "insurance": "maybe yes",
                },
            }
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_empty_params(self):
        response = self.post_request({"request_id": "s1", "params": {}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_missing_name(self):
        response = self.post_request(
            {"request_id": "s1", "params": {"country": "UK", "age": "78"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_missing_country(self):
        response = self.post_request(
            {"request_id": "s1", "params": {"name": "marshall", "age": "78"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_missing_age(self):
        response = self.post_request(
            {"request_id": "s1", "params": {"name": "marshall", "country": "UK"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_large_age_value(self):
        response = self.post_request(
            {
                "request_id": "s1",
                "params": {"name": "marshall", "country": "UK", "age": "999"},
            }
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_special_characters_in_name(self):
        response = self.post_request(
            {
                "request_id": "s1",
                "params": {"name": "mar$h@ll", "country": "UK", "age": "78"},
            }
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_empty_request(self):
        response = self.post_request({})
        self.assertEqual(response.status_code, 422)
        data = response.json()
        self.assertIn("detail", data)
        self.assertTrue(any("msg" in item for item in data["detail"]))

    def test_missing_request_id(self):
        response = self.post_request({"params": {}})
        self.assertEqual(response.status_code, 422)
        data = response.json()
        self.assertIn("detail", data)
        self.assertTrue(any("msg" in item for item in data["detail"]))

    def test_valid_request_with_edge_case_name(self):
        response = self.post_request(
            {"request_id": "s11", "params": {"name": "john_doe_123", "country": "USA", "age": "30"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_valid_info_without_age(self):
        response = self.post_request(
            {"request_id": "s121", "params": {"name": "alice", "country": "Canada"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])  
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(data["interactions"][0]["variable_name"], "age")

    def test_valid_info_with_short_country_name(self):
        response = self.post_request(
            {"request_id": "s21", "params": {"name": "jack", "country": "US", "age": "18"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_valid_info_with_long_country_name(self):
        response = self.post_request(
            {"request_id": "s20", "params": {"name": "ian", "country": "Papua New Guinea", "age": "28"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    
    def test_valid_info_with_mixed_case_country(self):
        response = self.post_request(
            {"request_id": "s19", "params": {"name": "hannah", "country": "uSa", "age": "22"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_valid_info_with_uppercase_country(self):
        response = self.post_request(
            {"request_id": "s18", "params": {"name": "george", "country": "USA", "age": "40"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_valid_info_with_special_chars_in_name(self):
        response = self.post_request(
            {"request_id": "s17", "params": {"name": "anne-marie", "country": "Italy", "age": "35"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_valid_info_with_different_age(self):
        response = self.post_request(
            {"request_id": "s16", "params": {"name": "eve", "country": "France", "age": "60"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_valid_request_different_country(self):
        response = self.post_request(
            {"request_id": "s13", "params": {"name": "bob", "country": "Australia", "age": "25"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_valid_info_with_insurance(self):
        response = self.post_request(
            {
                "request_id": "s14",
                "params": {"name": "charlie", "country": "Germany", "age": "45", "insurance": "yes"},
            }
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_valid_info_with_minimal_params(self):
        response = self.post_request(
            {"request_id": "1234445", "params": {"name": "dave"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])  # The booking is not complete
        self.assertIsNone(data["booking_id"])  # No booking_id yet
        self.assertIsNotNone(data.get("interactions"))  # Interactions should be present

        # Check that the interactions include requests for country and age
        interaction_variables = [interaction["variable_name"] for interaction in data["interactions"]]
        self.assertIn("country", interaction_variables)
        self.assertIn("age", interaction_variables)

    def test_valid_info_with_country_only(self):
        response = self.post_request(
            {"request_id": "s3316", "params": {"name": "eve", "country": "France"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])  # The booking is not complete
        self.assertIsNone(data["booking_id"])  # No booking_id yet
        self.assertIsNotNone(data.get("interactions"))  # Interactions should be present

        # Check that the interactions include a request for age
        interaction_variables = [interaction["variable_name"] for interaction in data["interactions"]]
        self.assertIn("age", interaction_variables)

    def test_valid_info_with_age_only(self):
        response = self.post_request(
            {"request_id": "s417", "params": {"name": "frank", "age": "45"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])  # The booking is not complete
        self.assertIsNone(data["booking_id"])  # No booking_id yet
        self.assertIsNotNone(data.get("interactions"))  # Interactions should be present

        # Check that the interactions include a request for country
        interaction_variables = [interaction["variable_name"] for interaction in data["interactions"]]
        self.assertIn("country", interaction_variables)

    def test_valid_info_with_complete_params(self):
        response = self.post_request(
            {"request_id": "s18", "params": {"name": "gary", "country": "USA", "age": "60"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])  # The booking is complete
        self.assertIsNotNone(data["booking_id"])  # A booking_id should be present
        self.assertIsNone(data.get("interactions"))  # No interactions should be present

    def test_invalid_request_missing_name(self):
        response = self.post_request(
            {"request_id": "s1339", "params": {"country": "UK", "age": "45"}}
        )
        self.assertEqual(response.status_code, 200)  # Expecting a 200 status code
        data = response.json()
        self.assertFalse(data["complete"])  # Expecting 'complete' to be False indicating interaction required
        self.assertIsNone(data["booking_id"])  # Expecting 'booking_id' to be None
        self.assertIsNotNone(data.get("interactions"))  # Expecting interactions to be present
        self.assertEqual(data["interactions"][0]["variable_name"], "name")  # Expecting the first interaction to be for 'name'

    def test_valid_info_with_additional_params(self):
        response = self.post_request(
            {"request_id": "s20", "params": {"name": "emma", "country": "USA", "age": "30", "insurance": "yes"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_invalid_request_missing_country(self):
        response = self.post_request(
            {"request_id": "s271", "params": {"name": "bob", "age": "40"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(data["interactions"][0]["variable_name"], "country")

    def test_valid_info_with_age_below_50(self):
        response = self.post_request(
            {"request_id": "s22", "params": {"name": "grace", "country": "Australia", "age": "35"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_valid_info_with_age_above_50_and_no_insurance(self):
        response = self.post_request(
            {"request_id": "s24", "params": {"name": "hannah", "country": "Spain", "age": "60", "insurance": "no"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_valid_info_with_min_age(self):
        response = self.post_request(
            {"request_id": "s25", "params": {"name": "joe", "country": "New Zealand", "age": "18"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))


    def test_valid_info_with_different_country(self):
        response = self.post_request(
            {"request_id": "s27", "params": {"name": "michael", "country": "Japan"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(data["interactions"][0]["variable_name"], "age")

    def test_invalid_request_missing_age_and_country(self):
        response = self.post_request(
            {"request_id": "s28", "params": {"name": "lisa"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(len(data["interactions"]), 2)

    def test_valid_info_with_insurance(self):
        response = self.post_request(
            {"request_id": "s29", "params": {"name": "emma", "country": "Germany", "age": "55", "insurance": "yes"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_invalid_request_missing_name(self):
        response = self.post_request(
            {"request_id": "s30", "params": {"country": "UK", "age": "45"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertIn("name", data["interactions"][0]["question"])

    def test_valid_info_without_country(self):
        response = self.post_request(
            {"request_id": "s31", "params": {"name": "john", "age": "30"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(data["interactions"][0]["variable_name"], "country")

    def test_invalid_request_large_age_value(self):
        response = self.post_request(
            {"request_id": "s32", "params": {"name": "samantha", "country": "Australia", "age": "150"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        # Adjust the assertion to match the new behavior
        self.assertEqual(data["interactions"][0]["variable_name"], "insurance")
        self.assertEqual(data["interactions"][0]["question"], "As you are over 50, do you need insurance?")

    def test_valid_request_with_all_params(self):
        response = self.post_request(
            {"request_id": "s50", "params": {"name": "john", "country": "USA", "age": "30"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_invalid_request_missing_country(self):
        response = self.post_request(
            {"request_id": "s51", "params": {"name": "emma", "age": "25"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(data["interactions"][0]["variable_name"], "country")

    def test_valid_request_with_insurance_yes(self):
        response = self.post_request(
            {"request_id": "s52", "params": {"name": "michael", "country": "Germany", "age": "60", "insurance": "yes"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_valid_request_with_insurance_no(self):
        response = self.post_request(
            {"request_id": "s53", "params": {"name": "sophia", "country": "France", "age": "50", "insurance": "no"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_invalid_request_missing_age(self):
        response = self.post_request(
            {"request_id": "s54", "params": {"name": "william", "country": "UK"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(data["interactions"][0]["variable_name"], "age")
    def test_valid_request_with_optional_params(self):
        response = self.post_request(
            {"request_id": "s60", "params": {"name": "emma", "country": "Canada", "age": "40", "insurance": "yes"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_invalid_request_missing_name_and_country(self):
        response = self.post_request(
            {"request_id": "s61", "params": {"age": "30"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertIn("name", data["interactions"][0]["variable_name"])
        self.assertIn("country", data["interactions"][1]["variable_name"])

    def test_valid_request_without_insurance1(self):
        response = self.post_request(
            {"request_id": "s62", "params": {"name": "james", "country": "Australia", "age": "25"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_valid_request_with_minimum_age1(self):
        response = self.post_request(
            {"request_id": "s70", "params": {"name": "Sophia", "country": "USA", "age": "18"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_invalid_request_missing_age1(self):
        response = self.post_request(
            {"request_id": "s71", "params": {"name": "Michael", "country": "Germany"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(data["interactions"][0]["variable_name"], "age")

    def test_valid_request_with_empty_country1(self):
        response = self.post_request(
            {"request_id": "s7a2", "params": {"name": "Emily", "country": "", "age": "25"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])  # Asserting that 'complete' should be False
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(data["interactions"][0]["variable_name"], "country")

    
    def test_valid_request_with_age_and_country(self):
        response = self.post_request(
            {"request_id": "s999", "params": {"name": "Sophia", "country": "Germany", "age": "30"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_invalid_request_missing_age(self):
        response = self.post_request(
            {"request_id": "s777", "params": {"name": "Isabella", "country": "France"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(data["interactions"][0]["variable_name"], "age")

    def test_invalid_request_missing_country(self):
        response = self.post_request(
            {"request_id": "s666", "params": {"name": "Liam", "age": "25"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(data["interactions"][0]["variable_name"], "country")

    def test_invalid_request_large_age_value(self):
            response = self.post_request(
                {"request_id": "s555", "params": {"name": "Emma", "country": "Australia", "age": "150"}}
            )
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertFalse(data["complete"])
            self.assertIsNone(data["booking_id"])
            self.assertIsNotNone(data.get("interactions"))
            
            # Check for the interaction related to insurance
            found_insurance_interaction = False
            for interaction in data["interactions"]:
                if interaction["variable_name"] == "insurance":
                    found_insurance_interaction = True
                    self.assertEqual(interaction["question"], "As you are over 50, do you need insurance?")
                    self.assertFalse(interaction["complete"])
                    self.assertIsNone(interaction["answer"])
                    break
            
            self.assertTrue(found_insurance_interaction, "Expected interaction about insurance")

    def test_invalid_request_missing_name(self):
        response = self.post_request(
            {"request_id": "s444", "params": {"country": "UK", "age": "45"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        
        # Check for interaction asking for "name" instead of "detail"
        found_name_interaction = False
        for interaction in data["interactions"]:
            if interaction["variable_name"] == "name":
                found_name_interaction = True
                self.assertEqual(interaction["question"], "What is your name?")
                self.assertFalse(interaction["complete"])
                self.assertIsNone(interaction["answer"])
                break
        
        self.assertTrue(found_name_interaction, "Expected interaction asking for name")

    def test_valid_request_with_empty_country(self):
        response = self.post_request(
            {"request_id": "s333", "params": {"name": "Emily", "country": "", "age": "25"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(data["interactions"][0]["variable_name"], "country")

    def test_valid_request_with_age_only(self):
        response = self.post_request(
            {"request_id": "s9499", "params": {"name": "", "country": "", "age": "30"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(data["interactions"][0]["variable_name"], "name")

    def test_invalid_request_missing_all_params(self):
        response = self.post_request(
            {"request_id": "s998", "params": {}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(len(data["interactions"]), 3)  # Assuming there are 3 required parameters


    def test_valid_request_with_additional_params(self):
        response = self.post_request(
            {"request_id": "s995", "params": {"name": "Michael", "country": "Germany", "age": "40", "additional_param": "value"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_invalid_request_duplicate_request_id(self):
        response = self.post_request(
            {"request_id": "s994", "params": {"name": "Emma", "country": "France", "age": "25"}}
        )
        self.assertEqual(response.status_code, 200)
        data1 = response.json()
        
        # Make a duplicate request with the same request_id
        response = self.post_request(
            {"request_id": "s994", "params": {"name": "Emma", "country": "France", "age": "25"}}
        )
        self.assertEqual(response.status_code, 200)
        data2 = response.json()

        self.assertEqual(data1, data2)  # Ensure response data is the same for duplicate requests

    def test_valid_request_with_name_and_country(self):
        response = self.post_request(
            {"request_id": "s888", "params": {"name": "Sophia", "country": "Brazil", "age": "28"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_valid_request_with_country_only(self):
        response = self.post_request(
            {"request_id": "s887", "params": {"name": "", "country": "Japan", "age": ""}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(data["interactions"][0]["variable_name"], "name")


    def test_invalid_request_missing_age(self):
        response = self.post_request(
            {"request_id": "s886", "params": {"name": "Isabella", "country": "Italy"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(data["interactions"][0]["variable_name"], "age")

    def test_valid_request_with_name_and_insurance(self):
        response = self.post_request(
            {"request_id": "s885", "params": {"name": "Alexander", "country": "Spain", "age": "55", "insurance": "Yes"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_valid_request_with_name_and_no_insurance(self):
        response = self.post_request(
            {"request_id": "s884", "params": {"name": "Olivia", "country": "Germany", "age": "45", "insurance": "No"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

        
    def test_valid_request_with_only_age(self):
        response = self.post_request(
            {"request_id": "s990", "params": {"name": "", "country": "", "age": "40"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(data["interactions"][0]["variable_name"], "name")

    def test_valid_request_with_insurance_false(self):
        response = self.post_request(
            {"request_id": "s992", "params": {"name": "Mia", "country": "Canada", "age": "52", "insurance": "No"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_request_with_empty_name_and_country(self):
        response = self.post_request(
            {"request_id": "s993", "params": {"name": "", "country": "", "age": ""}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))
        self.assertEqual(data["interactions"][0]["variable_name"], "name")

    
    def test_valid_request_with_full_info_but_no_insurance(self):
        response = self.post_request(
            {"request_id": "s996", "params": {"name": "Michael", "country": "India", "age": "49"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))
        
    def test_request_with_special_characters_in_name(self):
        response = self.post_request(
            {"request_id": "s997", "params": {"name": "An@!ta", "country": "Italy", "age": "30"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_valid_request_with_boundary_age(self):
        response = self.post_request(
            {"request_id": "s998", "params": {"name": "John", "country": "USA", "age": "18"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_request_with_unsupported_country(self):
        response = self.post_request(
            {"request_id": "s999", "params": {"name": "Alice", "country": "Neverland", "age": "25"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_non_numeric_age(self):
        response = self.post_request(
            {"request_id": "s1000", "params": {"name": "Bob", "country": "France", "age": "twenty"}}
        )
        self.assertEqual(response.status_code, 500)

    def test_valid_request_with_insurance_true(self):
        response = self.post_request(
            {"request_id": "s1001", "params": {"name": "Laura", "country": "Germany", "age": "35", "insurance": "Yes"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_request_with_invalid_request_id_format(self):
        response = self.post_request(
            {"request_id": "invalid_id", "params": {"name": "Tom", "country": "USA", "age": "28"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_exceedingly_long_name(self):
        long_name = "A" * 256  # Assuming a name longer than 255 characters is invalid
        response = self.post_request(
            {"request_id": "s1002", "params": {"name": long_name, "country": "Australia", "age": "45"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_exceedingly_long_country(self):
        long_country = "A" * 256  # Assuming a country longer than 255 characters is invalid
        response = self.post_request(
            {"request_id": "s1003", "params": {"name": "Sarah", "country": long_country, "age": "30"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_empty_request_id(self):
        response = self.post_request(
            {"request_id": "", "params": {"name": "Nina", "country": "Spain", "age": "26"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_valid_request_with_different_country(self):
        response = self.post_request(
            {"request_id": "s1005", "params": {"name": "Sophie", "country": "Netherlands", "age": "33"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_request_with_age_below_minimum_threshold(self):
        response = self.post_request(
            {"request_id": "s1006", "params": {"name": "Oscar", "country": "Belgium", "age": "0"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_age_above_maximum_threshold(self):
        response = self.post_request(
            {"request_id": "s1007", "params": {"name": "Ella", "country": "Norway", "age": "15450"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_valid_data_and_different_insurance_value(self):
        response = self.post_request(
            {"request_id": "s1009", "params": {"name": "Hannah", "country": "New Zealand", "age": "40", "insurance": "Yes"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_request_with_null_params(self):
        response = self.post_request(
            {"request_id": "s1010", "params": None}
        )
        self.assertEqual(response.status_code, 422)

    def test_request_with_missing_request_id_field(self):
        response = self.post_request(
            {"params": {"name": "Emily", "country": "Denmark", "age": "27"}}  # Missing 'request_id'
        )
        self.assertEqual(response.status_code, 422)

    def test_request_with_valid_data_and_special_characters_in_country(self):
        response = self.post_request(
            {"request_id": "s1011", "params": {"name": "Lucas", "country": "Brazil@2024", "age": "29"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_null_age(self):
        response = self.post_request(
            {"request_id": "s1012", "params": {"name": "Emma", "country": "Japan", "age": None}}
        )
        self.assertEqual(response.status_code, 500)

    def test_request_with_numeric_name(self):
        response = self.post_request(
            {"request_id": "s1013", "params": {"name": "12345", "country": "Argentina", "age": "35"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_whitespace_name(self):
        response = self.post_request(
            {"request_id": "s1014", "params": {"name": "    ", "country": "Chile", "age": "40"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_whitespace_country(self):
        response = self.post_request(
            {"request_id": "s1015", "params": {"name": "Henry", "country": "    ", "age": "32"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_whitespace_age(self):
        response = self.post_request(
            {"request_id": "s1016", "params": {"name": "Claire", "country": "Portugal", "age": "    "}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_negative_age(self):
        response = self.post_request(
            {"request_id": "s1017", "params": {"name": "David", "country": "Switzerland", "age": "-5"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_zero_age(self):
        response = self.post_request(
            {"request_id": "s1018", "params": {"name": "Zoe", "country": "Finland", "age": "0"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_decimal_age(self):
        response = self.post_request(
            {"request_id": "s1019", "params": {"name": "Eva", "country": "Iceland", "age": "29.5"}}
        )
        self.assertEqual(response.status_code, 500)

    def test_request_with_special_characters_in_country(self):
        response = self.post_request(
            {"request_id": "s1020", "params": {"name": "Gavin", "country": "Mex@ico", "age": "44"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_insurance_field_only(self):
        response = self.post_request(
            {"request_id": "s1022", "params": {"insurance": "Yes"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_boolean_age(self):
        response = self.post_request(
            {"request_id": "s1023", "params": {"name": "Tina", "country": "Japan", "age": True}}
        )
        self.assertEqual(response.status_code, 500)

    def test_request_with_empty_request_id_and_params(self):
        response = self.post_request(
            {"request_id": "", "params": {}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_missing_name_field(self):
        response = self.post_request(
            {"request_id": "s1025", "params": {"country": "Canada", "age": "25"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_minimum_valid_age(self):
        response = self.post_request(
            {"request_id": "s1027", "params": {"name": "Leo", "country": "UK", "age": "1"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_request_with_uppercase_country(self):
        response = self.post_request(
            {"request_id": "s1028", "params": {"name": "Samantha", "country": "USA", "age": "45"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_request_with_lowercase_country(self):
        response = self.post_request(
            {"request_id": "s1029", "params": {"name": "Martin", "country": "usa", "age": "37"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_request_with_mixed_case_country(self):
        response = self.post_request(
            {"request_id": "s1030", "params": {"name": "Laura", "country": "UsA", "age": "29"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_request_with_special_characters_in_name_field(self):
        response = self.post_request(
            {"request_id": "s1031", "params": {"name": "John_Doe", "country": "Italy", "age": "31"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_request_with_no_name_and_valid_country_age(self):
        response = self.post_request(
            {"request_id": "s1032", "params": {"name": "", "country": "Brazil", "age": "23"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))

    def test_request_with_no_country_and_valid_name_age(self):
        response = self.post_request(
            {"request_id": "s1033", "params": {"name": "Kim", "country": "", "age": "41"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))

    def test_request_with_valid_name_and_country_no_age(self):
        response = self.post_request(
            {"request_id": "s1035", "params": {"name": "Diana", "country": "Germany", "age": ""}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))

    def test_request_with_country_as_number(self):
        response = self.post_request(
            {"request_id": "s1036", "params": {"name": "Nina", "country": "123", "age": "36"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_valid_name_and_country_no_insurance(self):
        response = self.post_request(
            {"request_id": "s1037", "params": {"name": "Oliver", "country": "Denmark", "age": "28"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_request_with_empty_name_and_country_and_valid_age(self):
        response = self.post_request(
            {"request_id": "s1038", "params": {"name": "", "country": "", "age": "34"}}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data["complete"])
        self.assertIsNone(data["booking_id"])
        self.assertIsNotNone(data.get("interactions"))

    def test_request_with_only_valid_insurance_field(self):
        response = self.post_request(
            {"request_id": "s1039", "params": {"insurance": "No"}}
        )
        self.assertEqual(response.status_code, 400)

    def test_request_with_null_name(self):
        response = self.post_request(
            {"request_id": "s1040", "params": {"name": None, "country": "Australia", "age": "27"}}
        )
        self.assertEqual(response.status_code, 500)

    def test_request_with_null_country(self):
        response = self.post_request(
            {"request_id": "s1041", "params": {"name": "John", "country": None, "age": "27"}}
        )
        self.assertEqual(response.status_code, 500)

    def test_request_with_age_as_boolean(self):
        response = self.post_request(
            {"request_id": "s1042", "params": {"name": "Emma", "country": "Italy", "age": False}}
        )
        self.assertEqual(response.status_code, 500)

    def test_request_with_empty_request_body(self):
        response = self.post_request({})
        self.assertEqual(response.status_code, 422)

    def test_request_with_invalid_json_format(self):
        response = requests.post(
            self.base_url,
            headers={"accept": "application/json", "Content-Type": "application/json"},
            data="invalid_json_format"
        )
        self.assertEqual(response.status_code, 422)

class CustomTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_results = {}

    def addSuccess(self, test):
        super().addSuccess(test)
        self.test_results[test.id().split(".")[-1]] = "pass"

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.test_results[test.id().split(".")[-1]] = "fail"

    def addError(self, test, err):
        super().addError(test, err)
        self.test_results[test.id().split(".")[-1]] = "error"

class CustomTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return CustomTestResult(self.stream, self.descriptions, self.verbosity)

def generate_csv_report(test_timings, test_results):
    filename = "test_report_holiday_booking.csv"
    fieldnames = ["Test Case Name", "Start Time", "Duration (seconds)", "Status"]

    existing_tests = set()

    # Read existing test case names from the CSV file
    if os.path.isfile(filename):
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                existing_tests.add(row["Test Case Name"])

    with open(filename, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header only if file is empty
        if not os.path.isfile(filename) or os.stat(filename).st_size == 0:
            writer.writeheader()

        for test_name, timing in test_timings.items():
            if test_name not in existing_tests:  # Check if test case already exists
                status = test_results.get(test_name, "unknown")
                writer.writerow({
                    "Test Case Name": test_name,
                    "Start Time": timing["start_time"],
                    "Duration (seconds)": timing["duration_seconds"],
                    "Status": status
                })
                existing_tests.add(test_name)  # Add to set to prevent duplicates

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHolidayBooking)
    runner = CustomTestRunner()
    result = runner.run(suite)
    generate_csv_report(TestHolidayBooking.test_timings, result.test_results)

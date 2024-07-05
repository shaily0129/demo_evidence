import unittest
import requests
import json
from datetime import datetime

class TestHolidayBookingExtended(unittest.TestCase):

    base_url = "http://100.25.26.186:8002/tools/holiday/book"
    test_timings = {}

    def setUp(self):
        self.start_time = datetime.now()

    def tearDown(self):
        duration = datetime.now() - self.start_time
        test_name = self.id().split('.')[-1]
        self.test_timings[test_name] = {
            'start_time': self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            'duration_seconds': duration.total_seconds()
        }

    def post_request(self, data):
        response = requests.post(
            self.base_url,
            headers={"accept": "application/json", "Content-Type": "application/json"},
            data=json.dumps(data),
        )
        return response
    
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
    

if __name__ == "__main__":
    unittest.main()

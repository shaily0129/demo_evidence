import unittest
import json
import requests
from datetime import datetime
import csv
import os


class TestHolidayBooking(unittest.TestCase):

    base_url = "http://100.25.26.186:8002/tools/holiday/book"
    test_timings = {}

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


def generate_csv_report():
    csv_file = "test_report_holiday_booking.csv"
    print(f"Generating CSV report: {csv_file}")

    with open(
        csv_file, "w", newline=""
    ) as file:  # Use 'w' mode to overwrite and include headers
        writer = csv.writer(file)
        writer.writerow(
            ["Test Name", "Start Time", "Duration (seconds)"]
        )  # Writing headers
        for test_name, timings in TestHolidayBooking.test_timings.items():
            writer.writerow(
                [test_name, timings["start_time"], timings["duration_seconds"]]
            )
            print(
                f"Written row: {[test_name, timings['start_time'], timings['duration_seconds']]}"
            )


if __name__ == "__main__":
    unittest.main(
        exit=False
    )  # Make sure to use exit=False so that the script continues after tests
    generate_csv_report()
    print("CSV report generation completed.")

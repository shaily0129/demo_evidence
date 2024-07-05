import unittest
import requests
from datetime import datetime
import os
import csv


class TestRateResponse(unittest.TestCase):
    base_url = "http://3.82.58.102:8000"
    endpoint = "/rate_response"

    def test_successful_rating(self):
        # Prepare request payload
        payload = {
            "user_id": "test_user",
            "channel": "test_channel",
            "response_id": "test_response",
            "rating": 5,
            "comment": "Great service!",
        }

        # Make POST request to the endpoint
        response = requests.post(self.base_url + self.endpoint, json=payload)

        # Assert status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert response structure
        response_json = response.json()
        self.assertIn("user_id", response_json)
        self.assertIn("channel", response_json)
        self.assertIn("response_id", response_json)
        self.assertIn("rating", response_json)
        self.assertIn("comment", response_json)
        self.assertIn("datetime_rating", response_json)
        self.assertIn("success_code", response_json)
        self.assertIn("message", response_json)

    def test_validation_error_missing_fields(self):
        # Missing 'user_id' in request payload
        payload = {
            "channel": "test_channel",
            "response_id": "test_response",
            "rating": 4,
            "comment": "Good service!",
        }

        # Make POST request to the endpoint
        response = requests.post(self.base_url + self.endpoint, json=payload)

        # Assert status code is 422
        self.assertEqual(response.status_code, 422)

        # Assert response structure for validation error
        response_json = response.json()
        self.assertIn("detail", response_json)
        self.assertIsInstance(response_json["detail"], list)
        self.assertGreater(len(response_json["detail"]), 0)
        error_detail = response_json["detail"][0]
        self.assertIn("loc", error_detail)
        self.assertIn("msg", error_detail)
        self.assertIn("type", error_detail)


def generate_csv_report():
    csv_file = "test_report_.csv"
    print(f"Generating CSV report: {csv_file}")

    with open(
        csv_file, "w", newline=""
    ) as file:  # Use 'w' mode to overwrite and include headers
        writer = csv.writer(file)
        writer.writerow(
            ["Test Name", "Start Time", "Duration (seconds)"]
        )  # Writing headers
        for test_name, timings in TestRateResponse.test_timings.items():
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

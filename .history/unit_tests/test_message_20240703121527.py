import unittest
import requests
import json
from datetime import datetime
import csv
import os

class TestInteractEndpoint(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://3.82.58.102:8000"
        self.endpoint = "/interact"
        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
        }

    def test_successful_interaction(self):
        # Prepare request payload for successful interaction
        payload = {
            "user_id": "test_user",
            "channel": "web",
            "request_id": "123",
            "topics": ["general"],
            "message": "Hello, how are you?",
            "metadata": {
                "additionalProp1": "value1",
                "additionalProp2": "value2",
                "additionalProp3": "value3",
            },
        }

        # Send POST request
        response = requests.post(
            self.base_url + self.endpoint, headers=self.headers, json=payload
        )

        # Assert response status code and structure
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("response_duration", response.json())
        self.assertIn("agent_answer", response.json())

    def test_validation_error(self):
        # Prepare request payload for validation error (missing required fields)
        payload = {
            # Missing required fields intentionally to trigger validation error
        }

        # Send POST request
        response = requests.post(
            self.base_url + self.endpoint, headers=self.headers, json=payload
        )

        # Assert response status code and structure for validation error
        self.assertEqual(response.status_code, 422)
        self.assertIn("detail", response.json())
        self.assertIsInstance(response.json()["detail"], list)

def generate_csv_report():
    csv_file = 'test_report.csv'
    print(f"Generating CSV report: {csv_file}")

    with open(csv_file, 'w', newline='') as file:  # Use 'w' mode to overwrite and include headers
        writer = csv.writer(file)
        writer.writerow(['Test Name', 'Start Time', 'Duration (seconds)'])  # Writing headers
        for test_name, timings in TestInteractEndpoint.test_timings.items():
            writer.writerow([test_name, timings['start_time'], timings['duration_seconds']])
            print(f"Written row: {[test_name, timings['start_time'], timings['duration_seconds']]}")

if __name__ == '__main__':
    unittest.main(exit=False)  # Make sure to use exit=False so that the script continues after tests
    generate_csv_report()
    print("CSV report generation completed.")
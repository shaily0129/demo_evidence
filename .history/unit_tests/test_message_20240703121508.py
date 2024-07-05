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


if __name__ == "__main__":
    unittest.main()

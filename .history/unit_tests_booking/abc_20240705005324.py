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

    def test_different_request_id(self):
        response = self.post_request({"request_id": "s26", "params": {"name": "John"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assert(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_insurance_for_age_over_50(self):
        response = self.post_request({"request_id": "s36", "params": {"name": "Alice", "age": "55"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        if int(data["params"]["age"]) > 50:
            self.assertIsNotNone(data.get("insurance"))
        else:
            self.assertIsNone(data.get("insurance"))

    def test_special_characters_in_name_and_country(self):
        response = self.post_request({"request_id": "s46", "params": {"name": "mar$h@ll", "country": "US", "age": "40"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_invalid_age_format(self):
        response = self.post_request({"request_id": "s106", "params": {"name": "David", "age": "twenty"}})
        self.assertEqual(response.status_code, 422)
        data = response.json()
        self.assertIn("detail", data)
        self.assertTrue(any("age" in item.get("msg", "").lower() for item in data["interactions"]))

    def test_missing_name_and_country(self):
        response = self.post_request({"request_id": "s163", "params": {"age": "30"}})
        self.assertEqual(response.status_code, 422)
        data = response.json()
        self.assertIn("detail", data)
        self.assertTrue(any("name" in item.get("msg", "").lower() or "country" in item.get("msg", "").lower() for item in data["interactions"]))

if __name__ == "__main__":
    unittest.main()

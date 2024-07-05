import unittest
import requests


class TestHolidayBookingExtended(unittest.TestCase):

    base_url = "http://100.25.26.186:8002/tools/holiday/book"

    def make_request(self, data):
        response = requests.post(
            f"{self.BASE_URL}?interaction_text={data}",
            headers={"accept": "application/json"},
        )
        return response.json()

    def test_different_request_id(self):
        response = self.post_request({"request_id": "s2", "params": {"name": "John"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_insurance_for_age_over_50(self):
        response = self.post_request({"request_id": "s3", "params": {"name": "Alice", "age": "55"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNotNone(data.get("insurance"))

    def test_special_characters_in_name_and_country(self):
        response = self.post_request({"request_id": "s4", "params": {"name": "mar$h@ll", "country": "US", "age": "40"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["complete"])
        self.assertIsNotNone(data["booking_id"])
        self.assertIsNone(data.get("interactions"))

    def test_invalid_age_format(self):
        response = self.post_request({"request_id": "s5", "params": {"name": "David", "age": "twenty"}})
        self.assertEqual(response.status_code, 422)
        data = response.json()
        self.assertIn("detail", data)
        self.assertTrue(any("age" in item.get("msg", "").lower() for item in data["detail"]))

    def test_missing_name_and_country(self):
        response = self.post_request({"request_id": "s6", "params": {"age": "30"}})
        self.assertEqual(response.status_code, 422)
        data = response.json()
        self.assertIn("detail", data)
        self.assertTrue(any("name" in item.get("msg", "").lower() or "country" in item.get("msg", "").lower() for item in data["detail"]))


if __name__ == "__main__":
    unittest.main()

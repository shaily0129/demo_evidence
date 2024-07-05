import unittest
import json
import requests

class TestHolidayBooking(unittest.TestCase):

    base_url = 'http://100.25.26.186:8002/tools/holiday/book'

    def post_request(self, data):
        response = requests.post(self.base_url, headers={
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }, data=json.dumps(data))
        return response

    def test_initial_request(self):
        response = self.post_request({"request_id": "", "params": {}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['complete'])
        self.assertIsNone(data['booking_id'])
        self.assertIn('interactions', data)
        self.assertEqual(len(data['interactions']), 3)

    def test_second_request(self):
        response = self.post_request({"request_id": "s1", "params": {}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['complete'])
        self.assertIsNone(data['booking_id'])
        self.assertIn('interactions', data)
        self.assertEqual(len(data['interactions']), 3)

    def test_name_provided(self):
        response = self.post_request({"request_id": "s1", "params": {"name": "marshall"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['complete'])
        self.assertIsNone(data['booking_id'])
        self.assertIn('interactions', data)
        self.assertEqual(len(data['interactions']), 2)
        self.assertEqual(data['params']['name'], 'marshall')

    def test_name_and_country_provided(self):
        response = self.post_request({"request_id": "s1", "params": {"name": "marshall", "country": "UK"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['complete'])
        self.assertIsNone(data['booking_id'])
        self.assertIn('interactions', data)
        self.assertEqual(len(data['interactions']), 1)
        self.assertEqual(data['params']['name'], 'marshall')
        self.assertEqual(data['params']['country'], 'UK')

    def test_complete_info(self):
        response = self.post_request({"request_id": "s1", "params": {"name": "marshall", "country": "UK", "age": "78"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNone(data['booking_id'])
        self.assertIn('interactions', data)
        self.assertEqual(len(data['interactions']), 1)
        self.assertEqual(data['params']['name'], 'marshall')
        self.assertEqual(data['params']['country'], 'UK')
        self.assertEqual(data['params']['age'], '78')

    def test_insurance_provided(self):
        response = self.post_request({"request_id": "s1", "params": {"name": "marshall", "country": "UK", "age": "78", "insurance": "maybe yes"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNotNone(data['booking_id'])
        self.assertIsNone(data['interactions'])
        self.assertEqual(data['params']['name'], 'marshall')
        self.assertEqual(data['params']['country'], 'UK')
        self.assertEqual(data['params']['age'], '78')
        self.assertEqual(data['params']['insurance'], 'maybe yes')

    def test_no_more_modifications(self):
        # Re-submit the same request_id to ensure no changes can be made
        response = self.post_request({"request_id": "s1", "params": {"name": "marshall", "country": "UK", "age": "78", "insurance": "maybe yes"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNotNone(data['booking_id'])
        self.assertIsNone(data['interactions'])
        self.assertEqual(data['params']['name'], 'marshall')
        self.assertEqual(data['params']['country'], 'UK')
        self.assertEqual(data['params']['age'], '78')
        self.assertEqual(data['params']['insurance'], 'maybe yes')

if __name__ == '__main__':
    unittest.main()

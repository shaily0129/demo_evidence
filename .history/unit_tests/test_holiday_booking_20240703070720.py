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
        self.assert(data['complete'])
        self.assertIsNone(data['booking_id'])
        self.assertIn('interactions', data)
        self.assertEqual(len(data['interactions']), 3)

    def test_second_request(self):
        response = self.post_request({"request_id": "s1", "params": {}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNotNone(data['booking_id'])
        self.assertIsNone(data.get('interactions'))
        
    def test_name_provided(self):
        response = self.post_request({"request_id": "s1", "params": {"name": "marshall"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNotNone(data['booking_id'])
        self.assertIsNone(data.get('interactions'))
        
    def test_name_and_country_provided(self):
        response = self.post_request({"request_id": "s1", "params": {"name": "marshall", "country": "UK"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNotNone(data['booking_id'])
        self.assertIsNone(data.get('interactions'))
        
    def test_complete_info(self):
        response = self.post_request({"request_id": "s1", "params": {"name": "marshall", "country": "UK", "age": "78"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNotNone(data['booking_id'])
        self.assertIsNone(data.get('interactions'))
        
    def test_insurance_provided(self):
        response = self.post_request({"request_id": "s1", "params": {"name": "marshall", "country": "UK", "age": "78", "insurance": "maybe yes"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNotNone(data['booking_id'])
        self.assertIsNone(data.get('interactions'))
        
    def test_no_more_modifications(self):
        # Re-submit the same request_id to ensure no changes can be made
        response = self.post_request({"request_id": "s1", "params": {"name": "marshall", "country": "UK", "age": "78", "insurance": "maybe yes"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNotNone(data['booking_id'])
        self.assertIsNone(data.get('interactions'))

    def test_missing_name(self):
        response = self.post_request({"request_id": "s2", "params": {"country": "UK", "age": "30"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['complete'])
        self.assertIsNone(data['booking_id'])
        self.assertIn('interactions', data)
        self.assertEqual(data['interactions'][0]['variable_name'], 'name')

    def test_missing_country(self):
        response = self.post_request({"request_id": "s3", "params": {"name": "john", "age": "30"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['complete'])
        self.assertIsNone(data['booking_id'])
        self.assertIn('interactions', data)
        self.assertEqual(data['interactions'][0]['variable_name'], 'country')

    def test_missing_age(self):
        response = self.post_request({"request_id": "s4", "params": {"name": "john", "country": "UK"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['complete'])
        self.assertIsNone(data['booking_id'])
        self.assertIn('interactions', data)
        self.assertEqual(data['interactions'][0]['variable_name'], 'age')

    def test_invalid_age(self):
        response = self.post_request({"request_id": "s5", "params": {"name": "john", "country": "UK", "age": "invalid"}})
        self.assertEqual(response.status_code, 422)

    def test_additional_parameters(self):
        response = self.post_request({"request_id": "s6", "params": {"name": "john", "country": "UK", "age": "30", "extra_param": "extra_value"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNotNone(data['booking_id'])
        self.assertIsNone(data.get('interactions'))

    def test_empty_request_id(self):
        response = self.post_request({"request_id": "", "params": {"name": "john", "country": "UK", "age": "30"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNone(data['booking_id'])
        self.assertIn('interactions', data)
        self.assertEqual(len(data['interactions']), 3)

    def test_nonexistent_request_id(self):
        response = self.post_request({"request_id": "nonexistent", "params": {"name": "john", "country": "UK", "age": "30"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['complete'])
        self.assertIsNone(data['booking_id'])
        self.assertIn('interactions', data)

    def test_partial_data_completion(self):
        response = self.post_request({"request_id": "s7", "params": {"name": "john"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['complete'])
        self.assertIsNone(data['booking_id'])
        self.assertIn('interactions', data)
        self.assertEqual(data['interactions'][0]['variable_name'], 'age')

        response = self.post_request({"request_id": "s7", "params": {"age": "30"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['complete'])
        self.assertIsNone(data['booking_id'])
        self.assertIn('interactions', data)
        self.assertEqual(data['interactions'][0]['variable_name'], 'country')

        response = self.post_request({"request_id": "s7", "params": {"country": "UK"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNotNone(data['booking_id'])
        self.assertIsNone(data.get('interactions'))

    def test_no_params(self):
        response = self.post_request({"request_id": "s8", "params": {}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data['complete'])
        self.assertIsNone(data['booking_id'])
        self.assertIn('interactions', data)
        self.assertEqual(len(data['interactions']), 3)

if __name__ == '__main__':
    unittest.main()

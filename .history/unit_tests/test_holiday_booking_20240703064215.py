import unittest
import requests

class TestHolidayBooking(unittest.TestCase):
    
    def setUp(self):
        self.url = 'http://100.25.26.186:8002/tools/holiday/book'
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        self.payload = {
            "request_id": "",
            "params": {}
        }
    
    def test_booking_response(self):
        response = requests.post(self.url, headers=self.headers, json=self.payload)
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('request_id', data)
        self.assertIn('params', data)
        self.assertIn('interactions', data)
        self.assertIn('complete', data)
        self.assertIn('booking_id', data)
        
        self.assertIsInstance(data['request_id'], str)
        self.assertIsInstance(data['params'], dict)
        self.assertIsInstance(data['interactions'], list)
        self.assertIsInstance(data['complete'], bool)
        
        for interaction in data['interactions']:
            self.assertIn('variable_name', interaction)
            self.assertIn('variable_type', interaction)
            self.assertIn('question', interaction)
            self.assertIn('options', interaction)
            self.assertIn('answer', interaction)
            self.assertIn('complete', interaction)
            
            self.assertIsInstance(interaction['variable_name'], str)
            self.assertIsInstance(interaction['variable_type'], str)
            self.assertIsInstance(interaction['question'], str)
            self.assertIsInstance(interaction['options'], (list, type(None)))
            self.assertIsInstance(interaction['answer'], (str, type(None)))
            self.assertIsInstance(interaction['complete'], bool)

if __name__ == '__main__':
    unittest.main()

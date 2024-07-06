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
    
    def test_request_with_empty_request_body(self):
        response = self.post_request({})
        self.assertEqual(response.status_code, 422)

    def test_request_with_invalid_json_format(self):
        response = requests.post(
            self.base_url,
            headers={"accept": "application/json", "Content-Type": "application/json"},
            data="invalid_json_format"
        )
        self.assertEqual(response.status_code, 422)

    

    
    

if __name__ == "__main__":
    unittest.main()

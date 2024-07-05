import unittest
import json
import requests
import datetime
import csv

class TestHolidayBooking(unittest.TestCase):

    base_url = 'http://100.25.26.186:8002/tools/holiday/book'

    def post_request(self, data):
        response = requests.post(self.base_url, headers={
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }, data=json.dumps(data))
        return response

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

        
    def test_empty_params(self):
        response = self.post_request({"request_id": "s1", "params": {}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNotNone(data['booking_id'])
        self.assertIsNone(data.get('interactions'))


    def test_missing_name(self):
        response = self.post_request({"request_id": "s1", "params": {"country": "UK", "age": "78"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNotNone(data['booking_id'])
        self.assertIsNone(data.get('interactions'))

    def test_missing_country(self):
        response = self.post_request({"request_id": "s1", "params": {"name": "marshall", "age": "78"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNotNone(data['booking_id'])
        self.assertIsNone(data.get('interactions'))

    def test_missing_age(self):
        response = self.post_request({"request_id": "s1", "params": {"name": "marshall", "country": "UK"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNotNone(data['booking_id'])
        self.assertIsNone(data.get('interactions'))

    def test_large_age_value(self):
        response = self.post_request({"request_id": "s1", "params": {"name": "marshall", "country": "UK", "age": "999"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNotNone(data['booking_id'])
        self.assertIsNone(data.get('interactions'))


    def test_special_characters_in_name(self):
        response = self.post_request({"request_id": "s1", "params": {"name": "mar$h@ll", "country": "UK", "age": "78"}})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['complete'])
        self.assertIsNotNone(data['booking_id'])
        self.assertIsNone(data.get('interactions'))

    def test_empty_request(self):
        response = self.post_request({})
        self.assertEqual(response.status_code, 422)
        data = response.json()
        self.assertIn('detail', data)
        self.assertTrue(any('msg' in item for item in data['detail']))

    def test_missing_request_id(self):
        response = self.post_request({"params": {}})
        self.assertEqual(response.status_code, 422)
        data = response.json()
        self.assertIn('detail', data)
        self.assertTrue(any('msg' in item for item in data['detail']))


if __name__ == "__main__":
    # Run the tests and capture results
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHolidayBooking)
    result = unittest.TextTestRunner().run(suite)

    # Add current date and time to each test result
    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Save results to CSV file
    csv_file = '/Users/shailygoyal/Desktop/demo_evidence/unit_tests/test_report_holiday_book.csv'
    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ['test_name', 'outcome', 'timestamp']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for test_result in result.failures + result.errors:
            test_name = str(test_result[0]).split()[0]
            writer.writerow({
                'test_name': test_name,
                'outcome': 'FAIL',
                'timestamp': current_datetime
            })

    print(f"Tests completed at: {current_datetime}")
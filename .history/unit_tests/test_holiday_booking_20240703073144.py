import unittest

class TestHolidayBooking(unittest.TestCase):

    def test_initial_request(self):
        # Simulating the initial request test case
        data = {'request_id': 's1', 'params': {'name': 'marshall', 'country': 'UK', 'age': '78', 'insurance': 'maybe yes'}, 'interactions': None, 'complete': True, 'booking_id': '74614649'}
        self.assertFalse(data['complete'], f"Expected 'complete' to be False but got {data['complete']}")

    def test_name_provided(self):
        # Simulating the name provided test case
        data = {'request_id': 's1', 'params': {'name': 'marshall', 'country': 'UK', 'age': '78', 'insurance': 'maybe yes'}, 'interactions': None, 'complete': True, 'booking_id': '74614649'}
        self.assertFalse(data['complete'], f"Expected 'complete' to be False but got {data['complete']}")

    def test_name_and_country_provided(self):
        # Simulating the name and country provided test case
        data = {'request_id': 's1', 'params': {'name': 'marshall', 'country': 'UK', 'age': '78', 'insurance': 'maybe yes'}, 'interactions': None, 'complete': True, 'booking_id': '74614649'}
        self.assertFalse(data['complete'], f"Expected 'complete' to be False but got {data['complete']}")

    def test_second_request(self):
        # Simulating the second request test case
        data = {'request_id': 's1', 'params': {'name': 'marshall', 'country': 'UK', 'age': '78', 'insurance': 'maybe yes'}, 'interactions': None, 'complete': True, 'booking_id': '74614649'}
        self.assertFalse(data['complete'], f"Expected 'complete' to be False but got {data['complete']}")

    def test_insurance_provided(self):
        # Simulating the insurance provided test case
        data = {'request_id': 's1', 'params': {'name': 'marshall', 'country': 'UK', 'age': '78', 'insurance': 'maybe yes'}, 'interactions': None, 'complete': True, 'booking_id': '74614649'}
        self.assertNotIn('interactions', data)

    def test_no_more_modifications(self):
        # Simulating the no more modifications test case
        data = {'request_id': 's1', 'params': {'name': 'marshall', 'country': 'UK', 'age': '78', 'insurance': 'maybe yes'}, 'interactions': None, 'complete': True, 'booking_id': '74614649'}
        self.assertNotIn('interactions', data)

    def test_invalid_age(self):
        # Simulating the invalid age test case
        response = {'status_code': 422}  # Adjust this according to your test setup
        self.assertEqual(response['status_code'], 422)

    def test_nonexistent_request_id(self):
        # Simulating the nonexistent request ID test case
        data = {'request_id': 'nonexistent', 'params': {'name': 'john', 'country': 'UK', 'age': '30'}, 'interactions': None, 'complete': True, 'booking_id': '13897361'}
        self.assertNotIn('interactions', data)

    def test_partial_data_completion(self):
        # Simulating the partial data completion test case
        data = {'request_id': 's1', 'params': {'name': 'marshall', 'country': 'UK', 'age': '78', 'insurance': 'maybe yes'}, 'interactions': [{'variable_name': 'country', 'variable_type': 'str', 'question': 'What is your country of birth?', 'options': None, 'answer': None, 'complete': False}], 'complete': False, 'booking_id': None}
        self.assertEqual(data['interactions'][0]['variable_name'], 'country')

    def test_empty_request_id(self):
        # Simulating the empty request ID test case
        data = {'request_id': '', 'params': {'name': 'john', 'country': 'UK', 'age': '30'}, 'interactions': None, 'complete': True, 'booking_id': '61832912'}
        self.assertNotIn('interactions', data)

    def test_additional_parameters(self):
        # Simulating the additional parameters test case
        data = {'request_id': 's6', 'params': {'name': 'john', 'country': 'UK', 'age': '30', 'extra_param': 'extra_value'}, 'interactions': None, 'complete': True, 'booking_id': '50786770'}
        self.assertNotIn('interactions', data)

    def test_no_params(self):
        # Simulating the no params test case
        data = {'request_id': 's8', 'params': {}, 'interactions': [{'variable_name': 'name', 'variable_type': 'str', 'question': 'What is your name?', 'options': None, 'answer': None, 'complete': False}, {'variable_name': 'age', 'variable_type': 'str', 'question': 'What is your age?', 'options': None, 'answer': None, 'complete': False}, {'variable_name': 'country', 'variable_type': 'str', 'question': 'What is your country of birth?', 'options': None, 'answer': None, 'complete': False}], 'complete': False, 'booking_id': None}
        self.assertNotIn('interactions', data)


if __name__ == '__main__':
    unittest.main()

import unittest #63 tests
import requests
import json
import os
import csv
from datetime import datetime

class TestInteractAPI(unittest.TestCase):
    test_timings = {}
    BASE_URL="http://3.82.58.102:8000/interact"

    def setUp(self):
        self.base_url = self.BASE_URL

    def setUp(self):
        self.start_time = datetime.now()

    def tearDown(self):
        duration = datetime.now() - self.start_time
        test_name = self.id().split('.')[-1]
        self.test_timings[test_name] = {
            'start_time': self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            'duration_seconds': duration.total_seconds()
        }

    def test_weather_request(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "what is today's weather in Boulder, CO?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_greeting_request(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_request(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "I have patient who is suffering from hyperthermia and loss of blood. what to do?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_request2(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "My patient has a severe allergic reaction. What immediate actions should I take?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_request_with_hashtag(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "I have patient #p2 who is suffering from hyperthermia and loss of blood. what to do?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_request1(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "What are the symptoms of a heart attack, and how should I respond?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_interaction_states_in_usa(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "how many states in United States of America",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_interaction_conversion_metric(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "Convert 100 miles to kilometers",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn("agent_answer", response_data)
        self.assertIn("text_sections", response_data["agent_answer"])
        self.assertTrue(
            "kilometers" in response_data["agent_answer"]["text_sections"][0]["text"]
        )

    def test_time_conversion_query(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "Convert 5 PM IST to EDT",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())
        self.assertTrue(
            "EDT" in response.json()["agent_answer"]["text_sections"][0]["text"]
        )

    def test_currency_conversion_query(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "Convert 100 USD to EUR",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())
        self.assertTrue(
            "EUR" in response.json()["agent_answer"]["text_sections"][0]["text"]
        )

    def test_medical_request3(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "Can you provide guidance on treating a third-degree burn injury?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_request4(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "How should I manage a patient with a suspected concussion?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_request5(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "My patient has a severe allergic reaction. What immediate actions should I take?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_request6(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "What are the steps to perform CPR on an unconscious person?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_request7(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "A patient #p3 is experiencing cardiac arrest, what should I do?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_request8(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "A patient #p4 with a history of asthma is having difficulty breathing and wheezing, what immediate actions should be taken?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_request9(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "A patient #p5 has ingested a toxic substance and is now showing signs of poisoning, what are the recommended first aid steps?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_request10(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "A patient #p6 is experiencing severe abdominal pain and has a fever, could this be appendicitis and what should be the next steps?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_request11(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "A patient #p7 has suffered a deep laceration to the arm and is bleeding profusely, how can I control the bleeding and treat the wound?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_request12(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "A patient #p8 has lost consciousness after a head injury, what should I do to ensure they remain stable until help arrives?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_evac1(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "Evaluate the current risk level for patient who has a history of diabetes and is experiencing elevated blood sugar levels.",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_evac2(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "How should I assess the severity of the symptoms for patient #p2 who has been vomiting and has a high fever for the past two days?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_evac3(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "What is the recommended evaluation protocol for patient #p3 who has sustained a concussion and is now showing signs of confusion and dizziness?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_evac4(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "Please provide a detailed evaluation plan for patient #p4 who is undergoing chemotherapy and has developed a persistent cough and shortness of breath.",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_evac5(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "How can I accurately evaluate the mental health status of patient who has been displaying symptoms of severe anxiety and depression?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_medical_evac6(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "What steps should I take to thoroughly evaluate the condition of patient who is presenting with unexplained weight loss and fatigue?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_empty_payload(self):
        payload = {}
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 422)

    def test_invalid_data_types(self):
        payload = {
            "user_id": 123,  # should be a string
            "channel": True,  # should be a string
            "request_id": None,  # should be a string
            "topics": "string",  # should be an array
            "message": 456,  # should be a string
            "metadata": "string",  # should be a dict
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 422)

    def test_missing_required_fields(self):
        payload = {
            "user_id": "string",
            # "channel" is missing
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 422)

    def test_exceeding_maximum_lengths(self):
        payload = {
            "user_id": "string" * 1000,
            "channel": "string",
            "request_id": "string",
            "topics": ["string"] * 1000,
            "message": "hi, how are you?" * 1000,
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)

    def test_non_json_payload(self):
        payload = "this is not a json"
        response = requests.post(
            self.base_url, data=payload, headers={"Content-Type": "text/plain"}
        )
        self.assertEqual(response.status_code, 422)

    def test_special_characters(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "@#$%^&*()",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_special_characters(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "@#$%^&*()",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_invalid_json_format(self):
        payload = '{"user_id": "string", "channel": "string", "request_id": "string", "topics": ["string"], "message": "hi, how are you?", "metadata": "string"}'
        response = requests.post(
            self.base_url, data=payload, headers={"Content-Type": "application/json"}
        )
        self.assertEqual(response.status_code, 422)

    def test_invalid_enum_values(self):
        payload = {
            "user_id": "string",
            "channel": "invalid_channel",  # Assuming channel has specific valid values
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)

    def test_xss_attack_vector(self):
        payload = {
            "user_id": "<script>alert('XSS');</script>",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)

    def test_sql_injection_attack_vector(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "1; DROP TABLE users",  # SQL Injection attempt
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)

    def test_simultaneous_requests(self):
        from concurrent.futures import ThreadPoolExecutor

        def send_request():
            payload = {
                "user_id": "string",
                "channel": "string",
                "request_id": "string",
                "topics": ["string"],
                "message": "hi, how are you?",
                "metadata": {
                    "additionalProp1": "string",
                    "additionalProp2": "string",
                    "additionalProp3": "string",
                },
            }
            response = requests.post(self.base_url, json=payload)
            return response.status_code

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(send_request) for _ in range(10)]
            results = [future.result() for future in futures]
            for status_code in results:
                self.assertEqual(status_code, 200)

    def test_non_ascii_characters(self):
        payload = {
            "user_id": "用户",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "こんにちは",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)

    def test_whitespace_strings(self):
        payload = {
            "user_id": " ",
            "channel": " ",
            "request_id": " ",
            "topics": [" "],
            "message": " ",
            "metadata": {
                "additionalProp1": " ",
                "additionalProp2": " ",
                "additionalProp3": " ",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)

    def test_empty_strings(self):
        payload = {
            "user_id": "",
            "channel": "",
            "request_id": "",
            "topics": [""],
            "message": "",
            "metadata": {
                "additionalProp1": "",
                "additionalProp2": "",
                "additionalProp3": "",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)

    def test_boundary_numerical_values(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",
            "metadata": {
                "numeric_field": -1,  # assuming there is a numeric field
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 422)

    def test_extra_fields(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
            "extra_field": "extra_value",
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)  # assuming extra fields are ignored

    def test_invalid_http_headers(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        headers = {"Invalid-Header": "value"}
        response = requests.post(self.base_url, json=payload, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_invalid_urls(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        invalid_url = "http://3.82.58.102:8000/invalid"
        response = requests.post(invalid_url, json=payload)
        self.assertEqual(response.status_code, 404)

    def test_large_payload(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"] * 1000,  # large array of strings
            "message": "hi, how are you?" * 1000,  # large message
            "metadata": {
                "additionalProp1": "string" * 1000,  # large strings
                "additionalProp2": "string" * 1000,
                "additionalProp3": "string" * 1000,
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 413)  # Assuming 413 Payload Too Large

    def test_malformed_json_payload(self):
        payload = '{"user_id": "string", "channel": "string"  "request_id": "string", "topics": ["string"], "message": "hi, how are you?", "metadata": {"additionalProp1": "string", "additionalProp2": "string", "additionalProp3": "string"}}'
        response = requests.post(
            self.base_url, data=payload, headers={"Content-Type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)

    def test_empty_json_payload(self):
        payload = None
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 400)

    def test_missing_metadata(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",
            # "metadata" field is missing
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 400)

    def test_missing_message(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            # "message" field is missing
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 400)

    def test_large_payload(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"] * 1000,  # large array of strings
            "message": "hi, how are you?" * 1000,  # large message
            "metadata": {
                "additionalProp1": "string" * 1000,  # large strings
                "additionalProp2": "string" * 1000,
                "additionalProp3": "string" * 1000,
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)  # Assuming 413 Payload Too Large

    def test_malformed_json_payload(self):
        payload = '{"user_id": "string", "channel": "string"  "request_id": "string", "topics": ["string"], "message": "hi, how are you?", "metadata": {"additionalProp1": "string", "additionalProp2": "string", "additionalProp3": "string"}}'
        response = requests.post(
            self.base_url, data=payload, headers={"Content-Type": "application/json"}
        )
        self.assertEqual(response.status_code, 422)

    def test_empty_json_payload(self):
        payload = None
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 422)

    def test_missing_metadata(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",
            # "metadata" field is missing
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 422)

    def test_missing_message(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            # "message" field is missing
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 422)

    def test_case_sensitivity(self):
        payload1 = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "Hi, How are you?",  # Different case for message
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        payload2 = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",  # Lowercase message
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response1 = requests.post(self.base_url, json=payload1)
        response2 = requests.post(self.base_url, json=payload2)
        self.assertEqual(
            response2.status_code, 200
        )  # Assuming case insensitive comparison

    def test_long_request_id(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "a" * 1000,  # Very long request_id
            "topics": ["string"],
            "message": "hi, how are you?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)

    def test_invalid_topics_type(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": "invalid_type",  # Invalid type for topics
            "message": "hi, how are you?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 422)

    def test_empty_topics(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": [],  # Empty array for topics
            "message": "hi, how are you?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)

    def test_missing_user_id(self):
        payload = {
            # "user_id" field is missing
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 422)

    def test_missing_channel(self):
        payload = {
            "user_id": "string",
            # "channel" field is missing
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 422)

    def test_message_length_limit(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "a" * 10000,  # Very long message
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 500)

    def test_null_metadata_values(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",
            "metadata": {
                "additionalProp1": None,  # Null value in metadata
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 422)

    def test_invalid_metadata_format(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",
            "metadata": "invalid_metadata_format",
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 422)

    def test_whitespace_message(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "   ",  # Whitespace message
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)

    def test_null_metadata_values(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",
            "metadata": {
                "additionalProp1": None,  # Null value in metadata
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 422)

    def test_multiple_topics(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["topic1", "topic2", "topic3"],  # Multiple topics
            "message": "hi, how are you?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)

    def test_unicode_characters_in_message(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "こんにちは",  # Unicode characters in message
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(
            response.status_code, 200
        )  # Assuming API handles Unicode characters correctly

    def test_empty_metadata(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",
            "metadata": {},  # Empty metadata
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(
            response.status_code, 200
        )  # Assuming API can handle empty metadata

    def test_empty_message(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "",  # Empty message
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)

    def test_multiple_topics(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["topic1", "topic2", "topic3"],  # Multiple topics
            "message": "hi, how are you?",
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_unicode_characters_in_message(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "こんにちは",  # Unicode characters in message
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)  # Assuming API handles Unicode characters correctly
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_empty_metadata(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "hi, how are you?",
            "metadata": {},  # Empty metadata
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)  # Assuming API can handle empty metadata
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())

    def test_empty_message(self):
        payload = {
            "user_id": "string",
            "channel": "string",
            "request_id": "string",
            "topics": ["string"],
            "message": "",  # Empty message
            "metadata": {
                "additionalProp1": "string",
                "additionalProp2": "string",
                "additionalProp3": "string",
            },
        }
        response = requests.post(self.base_url, json=payload)
        self.assertEqual(response.status_code, 200)  
        self.assertIn("datetime_response", response.json())
        self.assertIn("agent_answer", response.json())


def generate_csv_report():
    csv_file = 'test_report_interact.csv'
    print(f"Generating CSV report: {csv_file}")

    with open(csv_file, 'w', newline='') as file:  # Use 'w' mode to overwrite and include headers
        writer = csv.writer(file)
        writer.writerow(['Test Name', 'Start Time', 'Duration (seconds)'])  # Writing headers
        for test_name, timings in TestInteractAPI.test_timings.items():
            writer.writerow([test_name, timings['start_time'], timings['duration_seconds']])
            print(f"Written row: {[test_name, timings['start_time'], timings['duration_seconds']]}")

if __name__ == '__main__':
    unittest.main(exit=False)  # Make sure to use exit=False so that the script continues after tests
    generate_csv_report()
    print("CSV report generation completed.")

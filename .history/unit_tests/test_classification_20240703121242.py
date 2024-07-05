import unittest #68 tests
import requests


class TestClassificationAPI(unittest.TestCase):

    BASE_URL = "http://3.82.58.102:8000/interact/classification"

    def make_request(self, interaction_text):
        response = requests.post(
            f"{self.BASE_URL}?interaction_text={interaction_text}",
            headers={"accept": "application/json"},
        )
        return response.json()

    def test_classification_triage(self):
        interaction_text = "i have patient with HR 110/90 and temp of 40C"
        expected_classification = "triage"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_evacuation_planning(self):
        interaction_text = "i am stuck at mountain, suggest something"
        expected_classification = "evacuation-planning"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_triage_2(self):
        interaction_text = "patient has chest pain and shortness of breath"
        expected_classification = "triage"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_greeting(self):
        interaction_text = "hello, how are you?"
        expected_classification = "greeting"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_emergency(self):
        interaction_text = "there is a fire in the building"
        expected_classification = "evacuation-planning"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_help(self):
        interaction_text = "i need help with my computer"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_greet(self):
        interaction_text = "你好"
        expected_classification = "greeting"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_greetings(self):
        interaction_text = "안녕하세요"
        expected_classification = "greeting"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_information(self):
        interaction_text = "can you tell me the time?"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_evacuation_planning_3(self):
        interaction_text = "earthquake has destroyed buildings, need evacuation"
        expected_classification = "evacuation-planning"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_default(self):
        interaction_text = "this is a random text"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_greeting_2(self):
        interaction_text = "good morning!"
        expected_classification = "greeting"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_greeting_3(self):
        interaction_text = "hi there!"
        expected_classification = "greeting"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_other(self):
        interaction_text = "do you listen music?"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_other_2(self):
        interaction_text = "no clear context provided"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_other_3(self):
        interaction_text = "example text for testing other category"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_triage_4(self):
        interaction_text = "patient has a deep cut and bleeding heavily"
        expected_classification = "medical"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_evacuation_planning_4(self):
        interaction_text = "there is a gas leak, need evacuation"
        expected_classification = "evacuation-planning"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_greeting_4(self):
        interaction_text = "hey, what's up?"
        expected_classification = "greeting"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_other_4(self):
        interaction_text = "can you recommend a good book?"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_other_5(self):
        interaction_text = "what's the weather like today?"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_other_6(self):
        interaction_text = "how do I change my password?"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_triage_5(self):
        interaction_text = "patient is unconscious with shallow breathing"
        expected_classification = "triage"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_evacuation_planning_5(self):
        interaction_text = "major traffic accident, need immediate evacuation"
        expected_classification = "evacuation-planning"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_greeting_5(self):
        interaction_text = "howdy! long time no see"
        expected_classification = "greeting"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_triage_6(self):
        interaction_text = (
            "patient experiencing sudden chest pain and shortness of breath"
        )
        expected_classification = "triage"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_evacuation_planning_6(self):
        interaction_text = (
            "chemical spill in the factory, immediate evacuation required"
        )
        expected_classification = "evacuation-planning"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_greeting_6(self):
        interaction_text = "hey, how have you been?"
        expected_classification = "greeting"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_other_10(self):
        interaction_text = "what are the symptoms of Dengue fever?"
        expected_classification = "medical"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_other_12(self):
        interaction_text = "recommend a good place for snorkeling"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_triage_7(self):
        interaction_text = "a patient has been brought in with a severe allergic reaction, difficulty breathing"
        expected_classification = "triage"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_evacuation_planning_7(self):
        interaction_text = (
            "forest fire spreading rapidly, nearby residents need immediate evacuation"
        )
        expected_classification = "evacuation-planning"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_greeting_7(self):
        interaction_text = "hey there, how was your trip?"
        expected_classification = "greeting"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_greeting_786(self):
        interaction_text = "It's hot outside."
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_greeting_723(self):
        interaction_text = "my friend is playing outside then she will go to school"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_other_13(self):
        interaction_text = "what is fasting?"
        expected_classification = "medical"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_other_14(self):
        interaction_text = "how do I apply for a visa?"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_other_15(self):
        interaction_text = (
            "recommendations for a good online course in machine learning"
        )
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_other(self):
        interaction_text = ""
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_numeric(self):
        interaction_text = "12345"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_non_ascii(self):
        interaction_text = "नमस्ते, दुनिया!"
        expected_classification = "greeting"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_only_symbols(self):
        interaction_text = ")"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_empty_interaction_text(self):
        interaction_text = ""
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_single_character(self):
        interaction_text = "a"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_special_characters(self):
        interaction_text = "@"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_mixed_language_text(self):
        interaction_text = "Hello こんにちは"
        expected_classification = "greeting"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_sql_injection(self):
        interaction_text = "'; DROP TABLE users; --"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_html_content(self):
        interaction_text = "<html><body>Hello</body></html>"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_json_input(self):
        interaction_text = '{"key": "value"}'
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_large_numbers(self):
        interaction_text = "12345678901234567890"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_emoji(self):
        interaction_text = "😀"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_unicode_symbols(self):
        interaction_text = "✈️🚀🏠"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_only_symbols(self):
        interaction_text = ")"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_cyrillic_text(self):
        interaction_text = "Привет"
        expected_classification = "greeting"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_arabic_text(self):
        interaction_text = "مرحبا"
        expected_classification = "greeting"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_email_address(self):
        interaction_text = "test@example.com"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_url(self):
        interaction_text = "https://www.example.com"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_script_tag(self):
        interaction_text = "<script>alert('Hello')</script>"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_plain_text_paragraph(self):
        interaction_text = "This is a paragraph of plain text to test the classification API."
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_whitespace_only(self):
        interaction_text = "     "
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_tab_character(self):
        interaction_text = "\t"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_newline_character(self):
        interaction_text = "\n"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_mixed_case_text(self):
        interaction_text = "HeLLo WoRLd"
        expected_classification = "greeting"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_empty_string(self):
        interaction_text = ""
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_escaped_characters(self):
        interaction_text = "Line1\\nLine2\\nLine3"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_combination_characters(self):
        interaction_text = "abc123!@"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_whitespace_between_text(self):
        interaction_text = "hello      world"
        expected_classification = "greeting"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_code_snippet(self):
        interaction_text = "def func():\n    return 'hello'"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_combined_unicode_text(self):
        interaction_text = "こんにちは (Hello) 123"
        expected_classification = "greeting"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")

    def test_classification_mixed_numbers_and_letters(self):
        interaction_text = "abc123xyz"
        expected_classification = "other"
        result = self.make_request(interaction_text)
        self.assertEqual(result["classification"], expected_classification)
        self.assertEqual(result["interaction_text"], interaction_text)
        self.assertEqual(result["implementation"], "agent002")


# if __name__ == "__main__":
#     unittest.main()

def generate_csv_report():
    csv_file = 'test_report.csv'
    print(f"Generating CSV report: {csv_file}")

    with open(csv_file, 'w', newline='') as file:  # Use 'w' mode to overwrite and include headers
        writer = csv.writer(file)
        writer.writerow(['Test Name', 'Start Time', 'Duration (seconds)'])  # Writing headers
        for test_name, timings in TestClassificationAPI.test_timings.items():
            writer.writerow([test_name, timings['start_time'], timings['duration_seconds']])
            print(f"Written row: {[test_name, timings['start_time'], timings['duration_seconds']]}")

if __name__ == '__main__':
    unittest.main(exit=False)  # Make sure to use exit=False so that the script continues after tests
    generate_csv_report()
    print("CSV report generation completed.")
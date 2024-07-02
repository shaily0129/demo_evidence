import unittest
import requests


class TestClassificationAPI(unittest.TestCase):

    BASE_URL = "http://3.82.58.102:8000/interact/classification"

    def make_request(self, interaction_text):
        response = requests.post(
            f"{self.BASE_URL}?interaction_text={interaction_text}",
            headers={"accept": "application/json"},
        )
        return response.json()
    

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


if __name__ == "__main__":
    unittest.main()

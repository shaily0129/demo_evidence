import unittest
import requests
import os
import csv
from datetime import datetime


class TestGetDocs(unittest.TestCase):
    BASE_URL
    test_timings = {}
    def setUp(self):
        self.base_url = "http://3.82.58.102:8000/get_docs"
        self.headers = {"accept": "application/json"}
        self.start_time = datetime.now()

    def tearDown(self):
        duration = datetime.now() - self.start_time
        test_name = self.id().split(".")[-1]
        self.test_timings[test_name] = {
            "start_time": self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "duration_seconds": duration.total_seconds(),
        }

    def test_status_code(self):
        params = {"user_id": "any_string"}
        response = requests.get(self.base_url, headers=self.headers, params=params)
        self.assertEqual(response.status_code, 200)

    def test_content_type(self):
        params = {"user_id": "any_string"}
        response = requests.get(self.base_url, headers=self.headers, params=params)
        self.assertEqual(response.headers["content-type"], "application/json")

    def test_response_structure(self):
        params = {"user_id": "any_string"}
        response = requests.get(self.base_url, headers=self.headers, params=params)
        response_data = response.json()

        # Assert basic structure of the response
        self.assertIn("user_id", response_data)
        self.assertIn("doc_pages", response_data)
        self.assertIsInstance(response_data["doc_pages"], list)

        if response_data["doc_pages"]:
            first_doc = response_data["doc_pages"][0]
            self.assertIn("doc_name", first_doc)
            self.assertIn("pages", first_doc)
            self.assertIsInstance(first_doc["pages"], list)
            self.assertGreater(len(first_doc["pages"]), 0)

    def test_response_content(self):
        params = {"user_id": "any_string"}
        response = requests.get(self.base_url, headers=self.headers, params=params)
        response_data = response.json()

        # Assert content of the response
        self.assertIn("user_id", response_data)
        self.assertIn("doc_pages", response_data)
        self.assertIsInstance(response_data["doc_pages"], list)

        if response_data["doc_pages"]:
            first_doc = response_data["doc_pages"][0]
            self.assertIn("doc_name", first_doc)
            self.assertIn("pages", first_doc)
            self.assertIsInstance(first_doc["pages"], list)
            self.assertGreater(len(first_doc["pages"]), 0)


def generate_csv_report():
    csv_file = "test_report_get_docs.csv"
    print(f"Generating CSV report: {csv_file}")

    with open(
        csv_file, "w", newline=""
    ) as file:  # Use 'w' mode to overwrite and include headers
        writer = csv.writer(file)
        writer.writerow(
            ["Test Name", "Start Time", "Duration (seconds)"]
        )  # Writing headers
        for test_name, timings in TestGetDocs.test_timings.items():
            writer.writerow(
                [test_name, timings["start_time"], timings["duration_seconds"]]
            )
            print(
                f"Written row: {[test_name, timings['start_time'], timings['duration_seconds']]}"
            )


if __name__ == "__main__":
    unittest.main(
        exit=False
    )  # Make sure to use exit=False so that the script continues after tests
    generate_csv_report()
    print("CSV report generation completed.")

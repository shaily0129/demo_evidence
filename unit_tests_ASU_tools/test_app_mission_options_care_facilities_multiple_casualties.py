import unittest
from datetime import datetime
import os
import csv
import sys
from typing import List

# Example classes (replace with your actual classes)
class MissionRequirements:
    def __init__(self, name: str, required_medical_services: List[str], required_medical_specialities: List[str], required_medical_supplies: List[str]):
        self.name = name
        self.required_medical_services = required_medical_services
        self.required_medical_specialities = required_medical_specialities
        self.required_medical_supplies = required_medical_supplies

class CareFacility:
    def __init__(self, cf_name: str, cf_bed_capacity: int, available_medical_services: List[str], available_medical_specialities: List[str], available_medical_supplies: List[str]):
        self.cf_name = cf_name
        self.cf_bed_capacity = cf_bed_capacity
        self.available_medical_services = available_medical_services
        self.available_medical_specialities = available_medical_specialities
        self.available_medical_supplies = available_medical_supplies

# Define your tests
class TestMissionRequirements(unittest.TestCase):

    def test_mission_creation(self):
        mission = MissionRequirements(
            name='Adrian Monk',
            required_medical_services=['emergency_care', 'surgical_services'],
            required_medical_specialities=['trauma_surgery'],
            required_medical_supplies=['blood_bags']
        )
        
        self.assertEqual(mission.name, 'Adrian Monk')
        self.assertIn('emergency_care', mission.required_medical_services)
        self.assertIn('trauma_surgery', mission.required_medical_specialities)
        self.assertIn('blood_bags', mission.required_medical_supplies)

    def test_mission_empty_services(self):
        mission = MissionRequirements(
            name='Jake Peralta',
            required_medical_services=[],
            required_medical_specialities=['general_surgery'],
            required_medical_supplies=['antibiotics']
        )

        self.assertEqual(mission.name, 'Jake Peralta')
        self.assertEqual(len(mission.required_medical_services), 0)
        self.assertIn('general_surgery', mission.required_medical_specialities)
        self.assertIn('antibiotics', mission.required_medical_supplies)

    def test_mission_no_supplies(self):
        mission = MissionRequirements(
            name='Leland Stottlemeyer',
            required_medical_services=['emergency_care', 'surgical_services'],
            required_medical_specialities=[],
            required_medical_supplies=[]
        )

        self.assertEqual(mission.name, 'Leland Stottlemeyer')
        self.assertIn('emergency_care', mission.required_medical_services)
        self.assertIn('surgical_services', mission.required_medical_services)
        self.assertEqual(len(mission.required_medical_specialities), 0)
        self.assertEqual(len(mission.required_medical_supplies), 0)

    def test_mission_with_optional_params(self):
        mission = MissionRequirements(
            name='Sharona Fleming',
            required_medical_services=['surgical_services', 'medical_imaging', 'laboratory_services'],
            required_medical_specialities=['trauma_surgery'],
            required_medical_supplies=[]
        )

        self.assertEqual(mission.name, 'Sharona Fleming')
        self.assertIn('medical_imaging', mission.required_medical_services)
        self.assertIn('trauma_surgery', mission.required_medical_specialities)
        self.assertEqual(len(mission.required_medical_supplies), 0)

class TestCareFacility(unittest.TestCase):

    def test_cf_creation(self):
        cf = CareFacility(
            cf_name='Battlefield Medical Center',
            cf_bed_capacity=50,
            available_medical_services=['emergency_care', 'surgical_services'],
            available_medical_specialities=['trauma_surgery'],
            available_medical_supplies=['blood_bags']
        )
        
        self.assertEqual(cf.cf_name, 'Battlefield Medical Center')
        self.assertEqual(cf.cf_bed_capacity, 50)
        self.assertIn('emergency_care', cf.available_medical_services)
        self.assertIn('trauma_surgery', cf.available_medical_specialities)
        self.assertIn('blood_bags', cf.available_medical_supplies)

    def test_cf_empty_specialities(self):
        cf = CareFacility(
            cf_name='Noble Medical Center',
            cf_bed_capacity=20,
            available_medical_services=['medical_imaging'],
            available_medical_specialities=[],
            available_medical_supplies=['painkillers']
        )

        self.assertEqual(cf.cf_name, 'Noble Medical Center')
        self.assertEqual(cf.cf_bed_capacity, 20)
        self.assertIn('medical_imaging', cf.available_medical_services)
        self.assertEqual(len(cf.available_medical_specialities), 0)
        self.assertIn('painkillers', cf.available_medical_supplies)

    def test_cf_no_supplies(self):
        cf = CareFacility(
            cf_name='Young hearts Medical Center',
            cf_bed_capacity=10,
            available_medical_services=['emergency_care', 'surgical_services', 'medical_imaging', 'laboratory_services'],
            available_medical_specialities=['trauma_surgery', 'emergency_medicine', 'orthopedic_surgery', 'general_surgery'],
            available_medical_supplies=[]
        )

        self.assertEqual(cf.cf_name, 'Young hearts Medical Center')
        self.assertEqual(cf.cf_bed_capacity, 10)
        self.assertIn('laboratory_services', cf.available_medical_services)
        self.assertIn('orthopedic_surgery', cf.available_medical_specialities)
        self.assertEqual(len(cf.available_medical_supplies), 0)

class CustomTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_timings = {}
        self.test_results = {}

    def addSuccess(self, test):
        super().addSuccess(test)
        self.test_results[test.id().split(".")[-1]] = "pass"

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.test_results[test.id().split(".")[-1]] = "fail"

    def addError(self, test, err):
        super().addError(test, err)
        self.test_results[test.id().split(".")[-1]] = "error"

    def startTest(self, test):
        super().startTest(test)
        self.test_timings[test.id().split(".")[-1]] = {
            "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def stopTest(self, test):
        super().stopTest(test)
        test_id = test.id().split(".")[-1]
        start_time = datetime.strptime(self.test_timings[test_id]["start_time"], "%Y-%m-%d %H:%M:%S")
        end_time = datetime.now()
        duration = end_time - start_time
        self.test_timings[test_id]["duration_seconds"] = duration.total_seconds()

class CustomTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return CustomTestResult(self.stream, self.descriptions, self.verbosity)

def generate_csv_report(test_timings, test_results):
    filename = "testing_report_mission_options_cf.csv"
    fieldnames = ["Test Case Name", "Start Date", "Start Time", "Duration (seconds)", "Status"]

    existing_tests = set()

    # Read existing test case names from the CSV file
    if os.path.isfile(filename):
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                existing_tests.add(row["Test Case Name"])

    with open(filename, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header only if file is empty
        if not os.path.isfile(filename) or os.stat(filename).st_size == 0:
            writer.writeheader()

        for test_name, timing in test_timings.items():
            if test_name not in existing_tests:  # Check if test case already exists
                status = test_results.get(test_name, "unknown")
                
                # Splitting timestamp into date and time
                start_date, start_time = timing["start_time"].split()

                writer.writerow({
                    "Test Case Name": test_name,
                    "Start Date": start_date,
                    "Start Time": start_time,
                    "Duration (seconds)": timing["duration_seconds"],
                    "Status": status
                })
                existing_tests.add(test_name)  # Add to set to prevent duplicates

if __name__ == "__main__":
    # Run tests and get the results
    suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    runner = CustomTestRunner()
    result = runner.run(suite)
    
    # Generate CSV report with test timings and results
    generate_csv_report(result.test_timings, result.test_results)


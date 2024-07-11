import unittest
from datetime import datetime
import os
import csv
import sys
from typing import List

# Define the MissionOptionsCFs class
class MissionOptionsCFs:
    def __init__(self, patient_name, care_facilities_possible, triage_score):
        self.patient_name = patient_name
        self.care_facilities_possible = care_facilities_possible
        self.triage_score = triage_score
        self.care_facility = None

# Define the MissionoptionsCFsToMissionfinalCFsAlgoName enumeration
class MissionoptionsCFsToMissionfinalCFsAlgoName:
    BASIC = 'basic'

# Define a mock implementation of the factory
class MissionoptionsCFsToMissionfinalCFsFactory:
    @staticmethod
    def create_missionoptionsCFs_to_missionfinalCFs_algo(mode):
        if mode == MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC:
            return MissionoptionsCFsToMissionfinalCFsAlgo()

# Define a mock implementation of the algorithm
class MissionoptionsCFsToMissionfinalCFsAlgo:
    def return_mission_final_care_facility(self, missions_options):
        # Mock implementation: Assign the first care facility in the list to each mission
        for mission in missions_options:
            mission.care_facility = mission.care_facilities_possible[0]
        return missions_options

class TestMissionOptionsCFs(unittest.TestCase):
    def setUp(self):
        self.mission1 = MissionOptionsCFs(patient_name='Adrian Monk', care_facilities_possible=['Battlefield Medical Center', 'Noble Medical Center', 'Young hearts Medical Center'], triage_score=20)
        self.mission2 = MissionOptionsCFs(patient_name='Natalie Tieger', care_facilities_possible=['Battlefield Medical Center', 'Noble Medical Center', 'Young hearts Medical Center'], triage_score=10)
        self.mission3 = MissionOptionsCFs(patient_name='Leland Stottlemeyer', care_facilities_possible=['Battlefield Medical Center', 'Noble Medical Center', 'Young hearts Medical Center'], triage_score=20)
        self.mission4 = MissionOptionsCFs(patient_name='Jake Peralta', care_facilities_possible=['Battlefield Medical Center', 'Noble Medical Center', 'Young hearts Medical Center'], triage_score=30)
        self.mission5 = MissionOptionsCFs(patient_name='Sharona Fleming', care_facilities_possible=['Battlefield Medical Center', 'Noble Medical Center', 'Young hearts Medical Center'], triage_score=40)
        self.mission6 = MissionOptionsCFs(patient_name='Randy Disher', care_facilities_possible=['Battlefield Medical Center', 'Noble Medical Center', 'Young hearts Medical Center'], triage_score=43)
        self.mission7 = MissionOptionsCFs(patient_name='Trudy Monk', care_facilities_possible=['Battlefield Medical Center', 'Noble Medical Center', 'Young hearts Medical Center'], triage_score=13)
        self.mission8 = MissionOptionsCFs(patient_name='Charles Kroger', care_facilities_possible=['Battlefield Medical Center', 'Noble Medical Center', 'Young hearts Medical Center'], triage_score=95)
        self.mission9 = MissionOptionsCFs(patient_name='Julie Trieger', care_facilities_possible=['Battlefield Medical Center', 'Noble Medical Center', 'Young hearts Medical Center'], triage_score=84)
        self.mission10 = MissionOptionsCFs(patient_name='Benjy Fleming', care_facilities_possible=['Battlefield Medical Center', 'Noble Medical Center', 'Young hearts Medical Center'], triage_score=82)
        
        self.all_mission_options = [
            self.mission1, self.mission2, self.mission3, self.mission4, 
            self.mission5, self.mission6, self.mission7, self.mission8, 
            self.mission9, self.mission10
        ]
        
    def test_mission_creation(self):
        self.assertEqual(self.mission1.patient_name, 'Adrian Monk')
        self.assertEqual(self.mission1.triage_score, 20)
        self.assertListEqual(self.mission1.care_facilities_possible, ['Battlefield Medical Center', 'Noble Medical Center', 'Young hearts Medical Center'])

    def test_mission_assignment(self):
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=self.all_mission_options)
        
        self.assertEqual(len(cfs_all_missions), len(self.all_mission_options))
        for mission_cf in cfs_all_missions:
            self.assertIn(mission_cf.patient_name, [mission.patient_name for mission in self.all_mission_options])
            self.assertIn(mission_cf.care_facility, ['Battlefield Medical Center', 'Noble Medical Center', 'Young hearts Medical Center'])

    def test_highest_triage_score(self):
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=self.all_mission_options)
        
        highest_triage_score = max(self.all_mission_options, key=lambda x: x.triage_score)
        assigned_facility = next(filter(lambda x: x.patient_name == highest_triage_score.patient_name, cfs_all_missions)).care_facility
        
        self.assertEqual(assigned_facility, highest_triage_score.care_facilities_possible[0])

    def test_duplicate_patient_names(self):
        mission_duplicate = MissionOptionsCFs(patient_name='Adrian Monk', care_facilities_possible=['Battlefield Medical Center', 'Noble Medical Center', 'Young hearts Medical Center'], triage_score=30)
        all_missions_with_duplicate = self.all_mission_options + [mission_duplicate]
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=all_missions_with_duplicate)
        
        names = [mission.patient_name for mission in cfs_all_missions]
        self.assertEqual(names.count('Adrian Monk'), 2)

    def test_assign_highest_score(self):
        highest_score_mission = MissionOptionsCFs(patient_name='Highest Score', care_facilities_possible=['Special Care Center'], triage_score=100)
        all_missions_with_highest = self.all_mission_options + [highest_score_mission]
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=all_missions_with_highest)
        
        highest_score_assigned = next(filter(lambda x: x.patient_name == 'Highest Score', cfs_all_missions)).care_facility
        self.assertEqual(highest_score_assigned, 'Special Care Center')

    def test_lowest_triage_score(self):
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=self.all_mission_options)
        
        lowest_triage_score = min(self.all_mission_options, key=lambda x: x.triage_score)
        assigned_facility = next(filter(lambda x: x.patient_name == lowest_triage_score.patient_name, cfs_all_missions)).care_facility
        
        self.assertEqual(assigned_facility, lowest_triage_score.care_facilities_possible[0])

    def test_assign_to_multiple_facilities(self):
        mission_multiple_facilities = MissionOptionsCFs(patient_name='Multiple Facilities', care_facilities_possible=['Facility A', 'Facility B', 'Facility C'], triage_score=50)
        all_missions_with_multiple = self.all_mission_options + [mission_multiple_facilities]
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=all_missions_with_multiple)
        
        assigned_facilities = next(filter(lambda x: x.patient_name == 'Multiple Facilities', cfs_all_missions)).care_facility
        self.assertIn(assigned_facilities, mission_multiple_facilities.care_facilities_possible)

    def test_no_missions(self):
        empty_missions = []
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=empty_missions)
        
        self.assertEqual(len(cfs_all_missions), 0)

    def test_assign_to_single_facility(self):
        single_facility_mission = MissionOptionsCFs(patient_name='Single Facility', care_facilities_possible=['Single Facility'], triage_score=50)
        all_missions_with_single = self.all_mission_options + [single_facility_mission]
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=all_missions_with_single)
        
        assigned_facility = next(filter(lambda x: x.patient_name == 'Single Facility', cfs_all_missions)).care_facility
        self.assertEqual(assigned_facility, 'Single Facility')

    def test_large_number_of_missions(self):
        large_number_of_missions = [
            MissionOptionsCFs(patient_name=f'Patient {i}', care_facilities_possible=['Facility A'], triage_score=50) for i in range(100)
        ]
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=large_number_of_missions)
        
        self.assertEqual(len(cfs_all_missions), 100)
        self.assertTrue(all(mission.care_facility == 'Facility A' for mission in cfs_all_missions))

    def test_single_facility_assignment(self):
        single_facility_mission = MissionOptionsCFs(patient_name='Single Facility', care_facilities_possible=['Specialized Center'], triage_score=50)
        all_missions_with_single = self.all_mission_options + [single_facility_mission]
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=all_missions_with_single)
        
        assigned_facility = next(filter(lambda x: x.patient_name == 'Single Facility', cfs_all_missions)).care_facility
        self.assertEqual(assigned_facility, 'Specialized Center')

    def test_multiple_facilities_assignment(self):
        multiple_facilities_mission = MissionOptionsCFs(patient_name='Multiple Facilities', care_facilities_possible=['Facility X', 'Facility Y', 'Facility Z'], triage_score=70)
        all_missions_with_multiple = self.all_mission_options + [multiple_facilities_mission]
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=all_missions_with_multiple)
        
        assigned_facility = next(filter(lambda x: x.patient_name == 'Multiple Facilities', cfs_all_missions)).care_facility
        self.assertIn(assigned_facility, ['Facility X', 'Facility Y', 'Facility Z'])

    def test_zero_triage_score(self):
        zero_triage_mission = MissionOptionsCFs(patient_name='Zero Triage Score', care_facilities_possible=['Facility A'], triage_score=0)
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=[zero_triage_mission])
        
        self.assertEqual(cfs_all_missions[0].care_facility, 'Facility A')

    def test_high_triage_score(self):
        high_triage_mission = MissionOptionsCFs(patient_name='High Triage Score', care_facilities_possible=['Facility B'], triage_score=100)
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=[high_triage_mission])
        
        self.assertEqual(cfs_all_missions[0].care_facility, 'Facility B')

    def test_random_facility_assignment(self):
        import random
        
        random_facility_mission = MissionOptionsCFs(patient_name='Random Facility', care_facilities_possible=['Facility A', 'Facility B', 'Facility C'], triage_score=60)
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=[random_facility_mission])
        
        assigned_facility = cfs_all_missions[0].care_facility
        self.assertIn(assigned_facility, random_facility_mission.care_facilities_possible)


    def test_long_patient_name(self):
        long_name = 'A' * 100
        long_name_mission = MissionOptionsCFs(patient_name=long_name, care_facilities_possible=['Facility A'], triage_score=70)
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=[long_name_mission])
        
        self.assertEqual(cfs_all_missions[0].care_facility, 'Facility A')

    def test_duplicate_facilities(self):
        duplicate_facilities_mission = MissionOptionsCFs(patient_name='Duplicate Facilities', care_facilities_possible=['Facility A', 'Facility A', 'Facility B'], triage_score=50)
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=[duplicate_facilities_mission])
        
        assigned_facility = cfs_all_missions[0].care_facility
        self.assertIn(assigned_facility, ['Facility A', 'Facility B'])

    def test_facilities_with_special_characters(self):
        special_characters_facility_mission = MissionOptionsCFs(patient_name='Special Characters Facility', care_facilities_possible=['Facility@A', 'Facility$B', 'Facility#C'], triage_score=60)
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=[special_characters_facility_mission])
        
        assigned_facility = cfs_all_missions[0].care_facility
        self.assertIn(assigned_facility, ['Facility@A', 'Facility$B', 'Facility#C'])

    def test_no_missions(self):
        no_missions = []
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=no_missions)
        
        self.assertEqual(len(cfs_all_missions), 0)


    def test_high_triage_score_reassignment(self):
        high_triage_reassignment_mission = MissionOptionsCFs(patient_name='High Triage Reassignment', care_facilities_possible=['Facility Y'], triage_score=100)
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=[high_triage_reassignment_mission])
        
        # Verify the care facility is reassigned due to the high triage score
        self.assertEqual(cfs_all_missions[0].triage_score, 100)
        self.assertIn(cfs_all_missions[0].care_facility, ['Facility Y'])

    def test_large_number_of_missions(self):
        large_number_missions = [
            MissionOptionsCFs(patient_name=f'Patient {i}', care_facilities_possible=['Facility X'], triage_score=60)
            for i in range(100)
        ]
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=large_number_missions)
        
        self.assertEqual(len(cfs_all_missions), 100)
        self.assertEqual(cfs_all_missions[0].patient_name, 'Patient 0')
        self.assertEqual(cfs_all_missions[-1].patient_name, 'Patient 99')

    def test_low_triage_score_assignment(self):
        low_triage_score_mission = MissionOptionsCFs(patient_name='Low Triage Score', care_facilities_possible=['Facility Z'], triage_score=5)
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=[low_triage_score_mission])
        
        self.assertEqual(cfs_all_missions[0].care_facility, 'Facility Z')

    def test_multiple_facility_assignment(self):
        multiple_facilities_mission = MissionOptionsCFs(patient_name='Multiple Facilities', care_facilities_possible=['Facility A', 'Facility B', 'Facility C'], triage_score=70)
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=[multiple_facilities_mission])
        
        assigned_facility = cfs_all_missions[0].care_facility
        self.assertIn(assigned_facility, ['Facility A', 'Facility B', 'Facility C'])

    def test_duplicate_patients(self):
        duplicate_patient_mission = MissionOptionsCFs(patient_name='Adrian Monk', care_facilities_possible=['Facility A', 'Facility B'], triage_score=60)
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=[duplicate_patient_mission] + self.all_mission_options)
        
        assigned_facility = cfs_all_missions[0].care_facility
        self.assertIn(assigned_facility, ['Facility A', 'Facility B'])

    def test_zero_triage_score(self):
        zero_triage_mission = MissionOptionsCFs(patient_name='Zero Triage', care_facilities_possible=['Facility C'], triage_score=0)
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=[zero_triage_mission])
        
        self.assertEqual(cfs_all_missions[0].triage_score, 0)
        self.assertEqual(cfs_all_missions[0].care_facility, 'Facility C')

    def test_negative_triage_score(self):
        negative_triage_mission = MissionOptionsCFs(patient_name='Negative Triage', care_facilities_possible=['Facility D'], triage_score=-10)
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=[negative_triage_mission])
        
        self.assertEqual(cfs_all_missions[0].triage_score, -10)
        self.assertEqual(cfs_all_missions[0].care_facility, 'Facility D')
        

    def test_identical_triage_scores(self):
        identical_triage_missions = [
            MissionOptionsCFs(patient_name=f'Patient {i}', care_facilities_possible=['Facility E'], triage_score=20)
            for i in range(5)
        ]
        
        algo_mission_assets = MissionoptionsCFsToMissionfinalCFsFactory.create_missionoptionsCFs_to_missionfinalCFs_algo(mode=MissionoptionsCFsToMissionfinalCFsAlgoName.BASIC)
        cfs_all_missions = algo_mission_assets.return_mission_final_care_facility(missions_options=identical_triage_missions)
        
        self.assertEqual(len(cfs_all_missions), 5)
        for mission in cfs_all_missions:
            self.assertEqual(mission.triage_score, 20)
            self.assertEqual(mission.care_facility, 'Facility E')



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
    filename = "testing_report_mission_final_cf.csv"
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
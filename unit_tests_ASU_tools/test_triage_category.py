import unittest
import os
import csv
from datetime import datetime

# Mock classes and functions
class MockThreshold:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

class MockPatient:
    def __init__(self, name, triage_score):
        self.name = name
        self.triage_score = triage_score

class MockTriageCategoryPatient:
    def __init__(self, patient_name, triage_category):
        self.patient_name = patient_name
        self.triage_category = triage_category

    def __str__(self):
        return self.triage_category

class MockTriagescoreToTriagecategoryAlgo:
    def __init__(self, thresholds):
        self.thresholds = thresholds

    def return_triage_categories(self, patients):
        # Mock implementation: returns a simple transformation of the input
        return [MockTriageCategoryPatient(patient.name, f"Category for score {patient.triage_score}") for patient in patients]

class MockTriagescoreToTriagecategoryFactory:
    @staticmethod
    def create_triageScore_to_triageCategory_algo(mode, thresholds):
        return MockTriagescoreToTriagecategoryAlgo(thresholds)

# Unit test case
class TestTriageScoreToTriageCategory(unittest.TestCase):
    test_timings = {}
    test_results = {}  # Dictionary to store test results
        

    def tearDown(self):
        duration = datetime.now() - self.start_time
        test_name = self.id().split(".")[-1]
        self.test_timings[test_name] = {
            "start_time": self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "duration_seconds": duration.total_seconds(),
        }
        

    def setUp(self):
        self.start_time = datetime.now()
        # Setting up thresholds and patients
        self.thresholds_data = {
            'triage_score': MockThreshold(min_value=0, max_value=100)
        }

        self.patient1 = MockPatient(name='Adrian Monk', triage_score=33)
        self.patient2 = MockPatient(name='Natalie Tieger', triage_score=40)
        self.patient3 = MockPatient(name='Leland Stottlemeyer', triage_score=43)
        self.patient4 = MockPatient(name='Jake Peralta', triage_score=20)
        self.patient5 = MockPatient(name='Sharona Fleming', triage_score=87)
        self.patient6 = MockPatient(name='Randy Disher', triage_score=1)
        self.patient7 = MockPatient(name='Trudy Monk', triage_score=40)
        self.patient8 = MockPatient(name='Charles Kroger', triage_score=95)
        self.patient9 = MockPatient(name='Julie Trieger', triage_score=80)
        self.patient10 = MockPatient(name='Benjy Fleming', triage_score=87)
        self.all_patients = [self.patient1, self.patient2, self.patient3, self.patient4, self.patient5,
                             self.patient6, self.patient7, self.patient8, self.patient9, self.patient10]

    def test_triage_score_to_category(self):
        print("")
        print("ALGO :: Triage scores -> Triage categories")
        algo_triage_categories = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_category_all_patients = algo_triage_categories.return_triage_categories(self.all_patients)
        
        # Assertions and checks
        for triage_category_patient in triage_category_all_patients:
            self.assertIsNotNone(triage_category_patient.patient_name)
            self.assertIsNotNone(triage_category_patient.triage_category)  # Adjust according to actual properties

        for triage_category_patient in triage_category_all_patients:
            print('\n')
            print(f"Patient {triage_category_patient.patient_name} has the following triage category {triage_category_patient}")

    def test_single_patient(self):
        # Test case for a single patient
        single_patient = [self.patient1]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_category_single = algo.return_triage_categories(single_patient)
        self.assertEqual(len(triage_category_single), 1)
        self.assertEqual(triage_category_single[0].patient_name, 'Adrian Monk')

    def test_high_score_threshold(self):
        # Test case for patients with scores near or at the high score threshold
        high_score_patient = MockPatient(name='High Scorer', triage_score=100)
        patients_with_high_score = self.all_patients + [high_score_patient]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_category_high_score = algo.return_triage_categories(patients_with_high_score)
        self.assertEqual(len(triage_category_high_score), len(patients_with_high_score))
        for patient in triage_category_high_score:
            self.assertTrue(patient.triage_category.startswith('Category for score'))

    def test_low_score_threshold(self):
        # Test case for patients with scores near or at the low score threshold
        low_score_patient = MockPatient(name='Low Scorer', triage_score=0)
        patients_with_low_score = self.all_patients + [low_score_patient]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_category_low_score = algo.return_triage_categories(patients_with_low_score)
        self.assertEqual(len(triage_category_low_score), len(patients_with_low_score))
        for patient in triage_category_low_score:
            self.assertTrue(patient.triage_category.startswith('Category for score'))



    def test_large_patient_data(self):
        # Test case for handling a large number of patients
        large_number_of_patients = [MockPatient(name=f'Patient {i}', triage_score=i) for i in range(1000)]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_large = algo.return_triage_categories(large_number_of_patients)
        self.assertEqual(len(triage_categories_large), 1000)


    def test_empty_thresholds(self):
        # Test case for handling empty thresholds
        empty_thresholds_data = {}
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=empty_thresholds_data)
        with self.assertRaises(KeyError):
            algo.return_triage_categories(self.all_patients)

    def test_no_patients(self):
        # Test case for no patients provided
        empty_patients = []
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_category_empty = algo.return_triage_categories(empty_patients)
        self.assertEqual(len(triage_category_empty), 0)

    def test_negative_scores(self):
        # Test case for handling negative triage scores
        patients_with_negative_scores = [MockPatient(name='Negative Score', triage_score=-10)]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_negative = algo.return_triage_categories(patients_with_negative_scores)
        self.assertEqual(len(triage_categories_negative), 1)
        self.assertTrue(triage_categories_negative[0].triage_category.startswith('Category for score'))

    def test_same_score_different_categories(self):
        # Test case for handling patients with the same triage score but different categories
        same_score_patients = [
            MockPatient(name='Patient 1', triage_score=50),
            MockPatient(name='Patient 2', triage_score=50),
            MockPatient(name='Patient 3', triage_score=50)
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_same_score = algo.return_triage_categories(same_score_patients)
        self.assertEqual(len(triage_categories_same_score), 3)
        categories = set([patient.triage_category for patient in triage_categories_same_score])
        self.assertEqual(len(categories), 1)  # Assert only one unique category for the same score

    def test_empty_patients_list(self):
        # Test case for handling an empty list of patients
        empty_patients = []
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_empty = algo.return_triage_categories(empty_patients)
        self.assertEqual(len(triage_categories_empty), 0)

    def test_high_thresholds(self):
        # Test case for handling very high thresholds
        high_thresholds_data = {
            'triage_score': MockThreshold(min_value=0, max_value=1000)
        }
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=high_thresholds_data)
        triage_categories_high = algo.return_triage_categories(self.all_patients)
        for category_patient in triage_categories_high:
            self.assertTrue(category_patient.triage_category.startswith('Category for score'))

    def test_mixed_scores(self):
        # Test case for handling patients with mixed triage scores
        mixed_scores_patients = [
            MockPatient(name='Patient A', triage_score=30),
            MockPatient(name='Patient B', triage_score=70),
            MockPatient(name='Patient C', triage_score=50),
            MockPatient(name='Patient D', triage_score=10),
            MockPatient(name='Patient E', triage_score=90),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_mixed = algo.return_triage_categories(mixed_scores_patients)
        self.assertEqual(len(triage_categories_mixed), len(mixed_scores_patients))
        for category_patient in triage_categories_mixed:
            self.assertTrue(category_patient.triage_category.startswith('Category for score'))


    def test_high_scores(self):
        # Test case for handling very high triage scores
        high_scores_patients = [
            MockPatient(name='High Score 1', triage_score=1000),
            MockPatient(name='High Score 2', triage_score=1500),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_high = algo.return_triage_categories(high_scores_patients)
        for category_patient in triage_categories_high:
            self.assertTrue(category_patient.triage_category.startswith('Category for score'))

    def test_low_scores(self):
        # Test case for handling very low triage scores
        low_scores_patients = [
            MockPatient(name='Low Score 1', triage_score=-10),
            MockPatient(name='Low Score 2', triage_score=-100),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_low = algo.return_triage_categories(low_scores_patients)
        for category_patient in triage_categories_low:
            self.assertTrue(category_patient.triage_category.startswith('Category for score'))

    def test_edge_case_single_patient(self):
        # Test case for handling a single patient
        single_patient = [MockPatient(name='Single Patient', triage_score=50)]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_single = algo.return_triage_categories(single_patient)
        self.assertEqual(len(triage_categories_single), 1)
        self.assertTrue(triage_categories_single[0].triage_category.startswith('Category for score'))

    def test_different_threshold_values(self):
        # Test case for handling different threshold values
        different_thresholds_data = {
            'triage_score': MockThreshold(min_value=50, max_value=100)
        }
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=different_thresholds_data)
        triage_categories_different = algo.return_triage_categories(self.all_patients)
        for category_patient in triage_categories_different:
            self.assertTrue(category_patient.triage_category.startswith('Category for score'))

    def test_negative_thresholds(self):
        # Test case for handling negative thresholds
        negative_thresholds_data = {
            'triage_score': MockThreshold(min_value=-100, max_value=0)
        }
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=negative_thresholds_data)
        triage_categories_negative = algo.return_triage_categories(self.all_patients)
        for category_patient in triage_categories_negative:
            self.assertTrue(category_patient.triage_category.startswith('Category for score'))

    def test_custom_category_format(self):
        # Test case for custom formatting of triage categories
        custom_format_thresholds = {
            'triage_score': MockThreshold(min_value=0, max_value=100)
        }

        class CustomTriageAlgo(MockTriagescoreToTriagecategoryAlgo):
            def return_triage_categories(self, patients):
                return [MockTriageCategoryPatient(patient.name, f"Custom Category ({patient.triage_score})") for patient in patients]

        algo = CustomTriageAlgo(custom_format_thresholds)
        triage_categories_custom = algo.return_triage_categories(self.all_patients)
        for category_patient in triage_categories_custom:
            self.assertTrue(category_patient.triage_category.startswith('Custom Category'))

    def test_multiple_categories(self):
        # Test case for handling multiple triage categories
        patients_with_multiple_categories = [
            MockPatient(name='Patient 1', triage_score=25),
            MockPatient(name='Patient 2', triage_score=50),
            MockPatient(name='Patient 3', triage_score=75),
            MockPatient(name='Patient 4', triage_score=100),
            MockPatient(name='Patient 5', triage_score=50),
            MockPatient(name='Patient 6', triage_score=25),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_multiple = algo.return_triage_categories(patients_with_multiple_categories)
        categories = set([patient.triage_category for patient in triage_categories_multiple])
        self.assertGreater(len(categories), 1)  # Ensure there are multiple unique categories


    def test_large_dataset(self):
        # Test case for handling a large dataset of patients
        large_dataset_patients = [MockPatient(name=f'Patient {i}', triage_score=i*10) for i in range(1000)]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_large = algo.return_triage_categories(large_dataset_patients)
        self.assertEqual(len(triage_categories_large), len(large_dataset_patients))

    def test_unicode_names(self):
        # Test case for handling patients with unicode names
        unicode_name_patients = [
            MockPatient(name='Patient 日本語', triage_score=80),
            MockPatient(name='Patient العربية', triage_score=70),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_unicode = algo.return_triage_categories(unicode_name_patients)
        for patient in triage_categories_unicode:
            self.assertIsNotNone(patient.patient_name)

    def test_custom_category_names(self):
        # Test case for handling custom category names based on scores
        custom_names_thresholds = {
            'triage_score': MockThreshold(min_value=0, max_value=100)
        }

        class CustomTriageAlgo(MockTriagescoreToTriagecategoryAlgo):
            def return_triage_categories(self, patients):
                categories = []
                for patient in patients:
                    if patient.triage_score < 50:
                        categories.append(MockTriageCategoryPatient(patient.name, 'Low Risk'))
                    else:
                        categories.append(MockTriageCategoryPatient(patient.name, 'High Risk'))
                return categories

        algo = CustomTriageAlgo(custom_names_thresholds)
        custom_names_patients = [
            MockPatient(name='Patient 1', triage_score=25),
            MockPatient(name='Patient 2', triage_score=75),
        ]
        triage_categories_custom_names = algo.return_triage_categories(custom_names_patients)
        self.assertEqual(triage_categories_custom_names[0].triage_category, 'Low Risk')
        self.assertEqual(triage_categories_custom_names[1].triage_category, 'High Risk')

    def test_edge_case_min_threshold(self):
        # Test case for handling patients with minimum triage score threshold
        min_threshold_patient = MockPatient(name='Min Threshold Patient', triage_score=0)
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_min_threshold = algo.return_triage_categories([min_threshold_patient])
        self.assertTrue(triage_categories_min_threshold[0].triage_category.startswith('Category for score'))

    def test_edge_case_max_threshold(self):
        # Test case for handling patients with maximum triage score threshold
        max_threshold_patient = MockPatient(name='Max Threshold Patient', triage_score=100)
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_max_threshold = algo.return_triage_categories([max_threshold_patient])
        self.assertTrue(triage_categories_max_threshold[0].triage_category.startswith('Category for score'))

    def test_multiple_thresholds(self):
        # Test case for handling multiple thresholds and categories
        multiple_thresholds_data = {
            'triage_score_low': MockThreshold(min_value=0, max_value=50),
            'triage_score_high': MockThreshold(min_value=51, max_value=100),
        }

        class MultipleThresholdsAlgo(MockTriagescoreToTriagecategoryAlgo):
            def return_triage_categories(self, patients):
                categories = []
                for patient in patients:
                    if 0 <= patient.triage_score <= 50:
                        categories.append(MockTriageCategoryPatient(patient.name, 'Low Risk'))
                    else:
                        categories.append(MockTriageCategoryPatient(patient.name, 'High Risk'))
                return categories

        algo = MultipleThresholdsAlgo(multiple_thresholds_data)
        multiple_thresholds_patients = [
            MockPatient(name='Patient 1', triage_score=25),
            MockPatient(name='Patient 2', triage_score=75),
        ]
        triage_categories_multiple_thresholds = algo.return_triage_categories(multiple_thresholds_patients)
        self.assertEqual(triage_categories_multiple_thresholds[0].triage_category, 'Low Risk')
        self.assertEqual(triage_categories_multiple_thresholds[1].triage_category, 'High Risk')

    def test_large_range_thresholds(self):
        # Test case for handling large range thresholds
        large_range_thresholds_data = {
            'triage_score': MockThreshold(min_value=-1000, max_value=1000),
        }
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=large_range_thresholds_data)
        large_range_patients = [
            MockPatient(name='Patient 1', triage_score=-500),
            MockPatient(name='Patient 2', triage_score=500),
        ]
        triage_categories_large_range = algo.return_triage_categories(large_range_patients)
        self.assertTrue(all(category.triage_category.startswith('Category for score') for category in triage_categories_large_range))


    def test_mixed_data_types(self):
        # Test case for handling patients with mixed data types in triage scores
        mixed_data_patients = [
            MockPatient(name='Patient 1', triage_score=55),
            MockPatient(name='Patient 2', triage_score='60'),  # Score as string
            MockPatient(name='Patient 3', triage_score=70.0),  # Score as float
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_mixed_data = algo.return_triage_categories(mixed_data_patients)
        self.assertEqual(len(triage_categories_mixed_data), len(mixed_data_patients))
        for patient in triage_categories_mixed_data:
            self.assertTrue(patient.triage_category.startswith('Category for score'))


    def test_empty_thresholds(self):
        # Test case for handling empty or undefined thresholds
        empty_thresholds_data = {}
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=empty_thresholds_data)
        empty_thresholds_patients = [
            MockPatient(name='Patient 1', triage_score=60),
            MockPatient(name='Patient 2', triage_score=70),
        ]
        triage_categories_empty_thresholds = algo.return_triage_categories(empty_thresholds_patients)
        self.assertEqual(len(triage_categories_empty_thresholds), len(empty_thresholds_patients))
        for patient in triage_categories_empty_thresholds:
            self.assertTrue(patient.triage_category.startswith('Category for score'))

    def test_large_number_of_patients(self):
        # Test case for handling a large number of patients
        large_number_patients = []
        for i in range(1000):
            large_number_patients.append(MockPatient(name=f'Patient {i}', triage_score=i % 100))
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_large_number = algo.return_triage_categories(large_number_patients)
        self.assertEqual(len(triage_categories_large_number), len(large_number_patients))

    def test_null_or_empty_category(self):
        # Test case for handling null or empty triage categories
        class NullOrEmptyCategoryAlgo(MockTriagescoreToTriagecategoryAlgo):
            def return_triage_categories(self, patients):
                categories = []
                for patient in patients:
                    if patient.triage_score < 50:
                        categories.append(MockTriageCategoryPatient(patient.name, None))
                    else:
                        categories.append(MockTriageCategoryPatient(patient.name, ''))
                return categories

        null_or_empty_patients = [
            MockPatient(name='Patient with Null Category', triage_score=40),
            MockPatient(name='Patient with Empty Category', triage_score=60),
        ]
        algo = NullOrEmptyCategoryAlgo(self.thresholds_data)
        triage_categories_null_or_empty = algo.return_triage_categories(null_or_empty_patients)
        self.assertTrue(all(category.triage_category is None or category.triage_category == '' for category in triage_categories_null_or_empty))

    def test_complex_threshold_logic(self):
        # Test case for complex threshold logic combining multiple conditions
        class ComplexThresholdLogicAlgo(MockTriagescoreToTriagecategoryAlgo):
            def return_triage_categories(self, patients):
                categories = []
                for patient in patients:
                    if patient.triage_score < 50 and patient.name.startswith('Patient'):
                        categories.append(MockTriageCategoryPatient(patient.name, 'Low Risk'))
                    elif patient.triage_score >= 50 and 'Patient' in patient.name:
                        categories.append(MockTriageCategoryPatient(patient.name, 'High Risk'))
                    else:
                        categories.append(MockTriageCategoryPatient(patient.name, 'Undefined Risk'))
                return categories

        complex_logic_patients = [
            MockPatient(name='Patient 1', triage_score=40),
            MockPatient(name='High Risk Patient 2', triage_score=70),
            MockPatient(name='Undefined Patient 3', triage_score=30),
        ]
        algo = ComplexThresholdLogicAlgo(self.thresholds_data)
        triage_categories_complex_logic = algo.return_triage_categories(complex_logic_patients)
        self.assertEqual(triage_categories_complex_logic[0].triage_category, 'Low Risk')
        self.assertEqual(triage_categories_complex_logic[1].triage_category, 'High Risk')
        self.assertEqual(triage_categories_complex_logic[2].triage_category, 'Undefined Risk')

    def test_edge_case_max_threshold_inclusive(self):
        # Test case for handling edge case where max threshold is inclusive
        inclusive_thresholds_data = {
            'triage_score': MockThreshold(min_value=0, max_value=100),
        }

        class InclusiveThresholdsAlgo(MockTriagescoreToTriagecategoryAlgo):
            def return_triage_categories(self, patients):
                categories = []
                for patient in patients:
                    if patient.triage_score == 100:
                        categories.append(MockTriageCategoryPatient(patient.name, 'Maximum Score Category'))
                    elif patient.triage_score > 50:
                        categories.append(MockTriageCategoryPatient(patient.name, 'High Score Category'))
                    else:
                        categories.append(MockTriageCategoryPatient(patient.name, 'Low Score Category'))
                return categories

        algo = InclusiveThresholdsAlgo(inclusive_thresholds_data)
        inclusive_thresholds_patients = [
            MockPatient(name='Patient 1', triage_score=50),
            MockPatient(name='Patient 2', triage_score=100),
        ]
        triage_categories_inclusive_thresholds = algo.return_triage_categories(inclusive_thresholds_patients)
        self.assertEqual(triage_categories_inclusive_thresholds[0].triage_category, 'Low Score Category')
        self.assertEqual(triage_categories_inclusive_thresholds[1].triage_category, 'Maximum Score Category')

    def test_edge_case_min_threshold_exclusive(self):
        # Test case for handling edge case where min threshold is exclusive
        exclusive_thresholds_data = {
            'triage_score': MockThreshold(min_value=1, max_value=100),
        }

        class ExclusiveThresholdsAlgo(MockTriagescoreToTriagecategoryAlgo):
            def return_triage_categories(self, patients):
                categories = []
                for patient in patients:
                    if patient.triage_score <= 1:
                        categories.append(MockTriageCategoryPatient(patient.name, 'Minimum Score Category'))
                    elif patient.triage_score > 50:
                        categories.append(MockTriageCategoryPatient(patient.name, 'High Score Category'))
                    else:
                        categories.append(MockTriageCategoryPatient(patient.name, 'Medium Score Category'))
                return categories

        algo = ExclusiveThresholdsAlgo(exclusive_thresholds_data)
        exclusive_thresholds_patients = [
            MockPatient(name='Patient 1', triage_score=1),
            MockPatient(name='Patient 2', triage_score=50),
            MockPatient(name='Patient 3', triage_score=100),
        ]
        triage_categories_exclusive_thresholds = algo.return_triage_categories(exclusive_thresholds_patients)
        self.assertEqual(triage_categories_exclusive_thresholds[0].triage_category, 'Minimum Score Category')
        self.assertEqual(triage_categories_exclusive_thresholds[1].triage_category, 'Medium Score Category')
        self.assertEqual(triage_categories_exclusive_thresholds[2].triage_category, 'High Score Category')

    def test_large_threshold_range(self):
        # Test case for handling a large threshold range
        large_range_thresholds_data = {
            'triage_score': MockThreshold(min_value=0, max_value=1000),
        }

        class LargeRangeAlgo(MockTriagescoreToTriagecategoryAlgo):
            def return_triage_categories(self, patients):
                categories = []
                for patient in patients:
                    if patient.triage_score < 500:
                        categories.append(MockTriageCategoryPatient(patient.name, 'Low Risk'))
                    else:
                        categories.append(MockTriageCategoryPatient(patient.name, 'High Risk'))
                return categories

        algo = LargeRangeAlgo(large_range_thresholds_data)
        large_range_patients = [
            MockPatient(name='Patient 1', triage_score=250),
            MockPatient(name='Patient 2', triage_score=750),
        ]
        triage_categories_large_range = algo.return_triage_categories(large_range_patients)
        self.assertEqual(triage_categories_large_range[0].triage_category, 'Low Risk')
        self.assertEqual(triage_categories_large_range[1].triage_category, 'High Risk')

    def test_all_patients_with_same_score(self):
        # Test case for handling all patients with the same triage score
        same_score_patients = [
            MockPatient(name='Patient 1', triage_score=50),
            MockPatient(name='Patient 2', triage_score=50),
            MockPatient(name='Patient 3', triage_score=50),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_same_scores = algo.return_triage_categories(same_score_patients)
        for category in triage_categories_same_scores:
            self.assertEqual(category.triage_category, 'Category for score 50')

    def test_patients_with_negative_scores(self):
        # Test case for handling patients with negative triage scores
        negative_score_patients = [
            MockPatient(name='Patient Negative 1', triage_score=-10),
            MockPatient(name='Patient Negative 2', triage_score=-20),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_negative_scores = algo.return_triage_categories(negative_score_patients)
        self.assertEqual(triage_categories_negative_scores[0].triage_category, 'Category for score -10')
        self.assertEqual(triage_categories_negative_scores[1].triage_category, 'Category for score -20')

    def test_case_sensitive_names(self):
        # Test case for handling case-sensitive patient names
        case_sensitive_patients = [
            MockPatient(name='Patient John', triage_score=60),
            MockPatient(name='patient Jane', triage_score=70),
            MockPatient(name='PATIENT Alex', triage_score=80),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_case_sensitive = algo.return_triage_categories(case_sensitive_patients)
        self.assertEqual(triage_categories_case_sensitive[0].triage_category, 'Category for score 60')
        self.assertEqual(triage_categories_case_sensitive[1].triage_category, 'Category for score 70')
        self.assertEqual(triage_categories_case_sensitive[2].triage_category, 'Category for score 80')

    def test_unexpected_data_type_scores(self):
        # Test case for handling unexpected data types in triage scores
        unexpected_data_type_patients = [
            MockPatient(name='Patient 1', triage_score='70'),
            MockPatient(name='Patient 2', triage_score=None),
            MockPatient(name='Patient 3', triage_score=True),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_unexpected_data_type = algo.return_triage_categories(unexpected_data_type_patients)
        self.assertEqual(triage_categories_unexpected_data_type[0].triage_category, 'Category for score 70')
        self.assertEqual(triage_categories_unexpected_data_type[1].triage_category, 'Category for score None')
        self.assertEqual(triage_categories_unexpected_data_type[2].triage_category, 'Category for score True')

    def test_patients_below_min_threshold(self):
        # Test case for handling patients with scores below the minimum threshold
        below_min_threshold_patients = [
            MockPatient(name='Patient 1', triage_score=-5),
            MockPatient(name='Patient 2', triage_score=-10),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_below_min = algo.return_triage_categories(below_min_threshold_patients)
        self.assertEqual(triage_categories_below_min[0].triage_category, 'Category for score -5')
        self.assertEqual(triage_categories_below_min[1].triage_category, 'Category for score -10')

    def test_all_patients_same_score(self):
        # Test case for handling all patients having the same triage score
        same_score_patients = [
            MockPatient(name='Patient A', triage_score=50),
            MockPatient(name='Patient B', triage_score=50),
            MockPatient(name='Patient C', triage_score=50),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_same_score = algo.return_triage_categories(same_score_patients)
        self.assertEqual(triage_categories_same_score[0].triage_category, 'Category for score 50')
        self.assertEqual(triage_categories_same_score[1].triage_category, 'Category for score 50')
        self.assertEqual(triage_categories_same_score[2].triage_category, 'Category for score 50')

    def test_patients_below_min_threshold(self):
        # Test case for handling patients with scores below the minimum threshold
        below_min_threshold_patients = [
            MockPatient(name='Patient 1', triage_score=-5),
            MockPatient(name='Patient 2', triage_score=-10),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_below_min = algo.return_triage_categories(below_min_threshold_patients)
        self.assertEqual(triage_categories_below_min[0].triage_category, 'Category for score -5')
        self.assertEqual(triage_categories_below_min[1].triage_category, 'Category for score -10')

    def test_patients_above_max_threshold(self):
        # Test case for handling patients with scores above the maximum threshold
        above_max_threshold_patients = [
            MockPatient(name='Patient 1', triage_score=150),
            MockPatient(name='Patient 2', triage_score=200),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_above_max = algo.return_triage_categories(above_max_threshold_patients)
        self.assertEqual(triage_categories_above_max[0].triage_category, 'Category for score 150')
        self.assertEqual(triage_categories_above_max[1].triage_category, 'Category for score 200')

    def test_patient_with_zero_score(self):
        # Test case for handling a patient with a triage score of zero
        zero_score_patients = [
            MockPatient(name='Patient 1', triage_score=0),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_zero_score = algo.return_triage_categories(zero_score_patients)
        self.assertEqual(triage_categories_zero_score[0].triage_category, 'Category for score 0')

    def test_non_integer_scores(self):
        # Test case for handling non-integer triage scores
        non_integer_patients = [
            MockPatient(name='Patient 1', triage_score=10.5),
            MockPatient(name='Patient 2', triage_score=20.75),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_non_integer = algo.return_triage_categories(non_integer_patients)
        self.assertEqual(triage_categories_non_integer[0].triage_category, 'Category for score 10.5')
        self.assertEqual(triage_categories_non_integer[1].triage_category, 'Category for score 20.75')

    def test_patients_with_edge_case_scores(self):
        # Test case for handling patients with edge case scores at the boundaries of the thresholds
        edge_case_patients = [
            MockPatient(name='Patient 1', triage_score=self.thresholds_data['triage_score'].min_value),
            MockPatient(name='Patient 2', triage_score=self.thresholds_data['triage_score'].max_value),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_edge_cases = algo.return_triage_categories(edge_case_patients)
        self.assertEqual(triage_categories_edge_cases[0].triage_category, f'Category for score {self.thresholds_data["triage_score"].min_value}')
        self.assertEqual(triage_categories_edge_cases[1].triage_category, f'Category for score {self.thresholds_data["triage_score"].max_value}')

    def test_patients_with_extreme_scores(self):
        # Test case for handling patients with extremely high or low scores
        extreme_score_patients = [
            MockPatient(name='Patient 1', triage_score=-99999),
            MockPatient(name='Patient 2', triage_score=99999),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_extreme_scores = algo.return_triage_categories(extreme_score_patients)
        self.assertEqual(triage_categories_extreme_scores[0].triage_category, 'Category for score -99999')
        self.assertEqual(triage_categories_extreme_scores[1].triage_category, 'Category for score 99999')

    def test_patients_with_invalid_name_types(self):
        # Test case for handling patients with non-string names
        invalid_name_patients = [
            MockPatient(name=123, triage_score=10),
            MockPatient(name=True, triage_score=20),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_invalid_names = algo.return_triage_categories(invalid_name_patients)
        self.assertEqual(triage_categories_invalid_names[0].triage_category, 'Category for score 10')
        self.assertEqual(triage_categories_invalid_names[1].triage_category, 'Category for score 20')

    def test_patients_with_large_names(self):
        # Test case for handling patients with extremely large names
        large_name_patients = [
            MockPatient(name='Patient' * 1000, triage_score=30),
            MockPatient(name='A' * 1000, triage_score=40),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_large_names = algo.return_triage_categories(large_name_patients)
        self.assertEqual(triage_categories_large_names[0].triage_category, 'Category for score 30')
        self.assertEqual(triage_categories_large_names[1].triage_category, 'Category for score 40')

    def test_patients_with_special_characters_in_names(self):
        # Test case for handling patients with special characters in their names
        special_char_patients = [
            MockPatient(name='Patient!@#$', triage_score=50),
            MockPatient(name='Jane*(&^', triage_score=60),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_special_chars = algo.return_triage_categories(special_char_patients)
        self.assertEqual(triage_categories_special_chars[0].triage_category, 'Category for score 50')
        self.assertEqual(triage_categories_special_chars[1].triage_category, 'Category for score 60')

    def test_patients_with_unicode_characters_in_names(self):
        # Test case for handling patients with Unicode characters in their names
        unicode_patients = [
            MockPatient(name='患者一', triage_score=70),
            MockPatient(name='患者二', triage_score=80),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_unicode_names = algo.return_triage_categories(unicode_patients)
        self.assertEqual(triage_categories_unicode_names[0].triage_category, 'Category for score 70')
        self.assertEqual(triage_categories_unicode_names[1].triage_category, 'Category for score 80')

    def test_patients_with_empty_names(self):
        # Test case for handling patients with empty names
        empty_name_patients = [
            MockPatient(name='', triage_score=90),
            MockPatient(name=None, triage_score=100),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_empty_names = algo.return_triage_categories(empty_name_patients)
        self.assertEqual(triage_categories_empty_names[0].triage_category, 'Category for score 90')
        self.assertEqual(triage_categories_empty_names[1].triage_category, 'Category for score 100')

    def test_all_patients_with_maximum_score(self):
        # Test case for handling all patients with the maximum triage score
        max_score_patients = [
            MockPatient(name='Patient Max 1', triage_score=self.thresholds_data['triage_score'].max_value),
            MockPatient(name='Patient Max 2', triage_score=self.thresholds_data['triage_score'].max_value),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_max_scores = algo.return_triage_categories(max_score_patients)
        for category in triage_categories_max_scores:
            self.assertEqual(category.triage_category, f'Category for score {self.thresholds_data["triage_score"].max_value}')

    def test_all_patients_with_minimum_score(self):
        # Test case for handling all patients with the minimum triage score
        min_score_patients = [
            MockPatient(name='Patient Min 1', triage_score=self.thresholds_data['triage_score'].min_value),
            MockPatient(name='Patient Min 2', triage_score=self.thresholds_data['triage_score'].min_value),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_min_scores = algo.return_triage_categories(min_score_patients)
        for category in triage_categories_min_scores:
            self.assertEqual(category.triage_category, f'Category for score {self.thresholds_data["triage_score"].min_value}')

    def test_single_patient(self):
        # Test case for handling a single patient
        single_patient = MockPatient(name='Single Patient', triage_score=45)
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_category_single = algo.return_triage_categories([single_patient])
        self.assertEqual(triage_category_single[0].triage_category, 'Category for score 45')

    def test_large_number_of_identical_patients(self):
        # Test case for handling a large number of identical patients
        identical_patients = [MockPatient(name=f'Patient {i}', triage_score=50) for i in range(100)]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_identical = algo.return_triage_categories(identical_patients)
        for category in triage_categories_identical:
            self.assertEqual(category.triage_category, 'Category for score 50')
        self.assertEqual(len(triage_categories_identical), 100)

    def test_patients_with_increasing_scores(self):
        # Test case for handling patients with incrementally increasing triage scores
        increasing_score_patients = [MockPatient(name=f'Patient {i}', triage_score=i) for i in range(10)]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_increasing_scores = algo.return_triage_categories(increasing_score_patients)
        for i, category in enumerate(triage_categories_increasing_scores):
            self.assertEqual(category.triage_category, f'Category for score {i}')

    def test_patients_with_decreasing_scores(self):
        # Test case for handling patients with decrementally decreasing triage scores
        decreasing_score_patients = [MockPatient(name=f'Patient {i}', triage_score=100 - i) for i in range(10)]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_decreasing_scores = algo.return_triage_categories(decreasing_score_patients)
        for i, category in enumerate(triage_categories_decreasing_scores):
            self.assertEqual(category.triage_category, f'Category for score {100 - i}')

    def test_patients_with_random_scores(self):
        # Test case for handling patients with random triage scores
        import random
        random.seed(0)  # Set seed for reproducibility
        random_score_patients = [MockPatient(name=f'Patient {i}', triage_score=random.randint(0, 100)) for i in range(10)]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_random_scores = algo.return_triage_categories(random_score_patients)
        self.assertEqual(len(triage_categories_random_scores), 10)

    def test_negative_and_positive_scores(self):
        # Test case for handling a mix of negative and positive triage scores
        mixed_score_patients = [
            MockPatient(name='Patient Negative', triage_score=-10),
            MockPatient(name='Patient Positive', triage_score=25),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_mixed_scores = algo.return_triage_categories(mixed_score_patients)
        self.assertEqual(triage_categories_mixed_scores[0].triage_category, 'Category for score -10')
        self.assertEqual(triage_categories_mixed_scores[1].triage_category, 'Category for score 25')

    def test_duplicate_scores(self):
        # Test case for handling duplicate triage scores
        duplicate_score_patients = [
            MockPatient(name='Patient 1', triage_score=50),
            MockPatient(name='Patient 2', triage_score=50),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_duplicate_scores = algo.return_triage_categories(duplicate_score_patients)
        self.assertEqual(triage_categories_duplicate_scores[0].triage_category, 'Category for score 50')
        self.assertEqual(triage_categories_duplicate_scores[1].triage_category, 'Category for score 50')

    def test_mixed_types_in_scores(self):
        # Test case for handling mixed types in triage scores (integers and floats)
        mixed_type_score_patients = [
            MockPatient(name='Patient Int', triage_score=50),
            MockPatient(name='Patient Float', triage_score=50.5),
        ]
        algo = MockTriagescoreToTriagecategoryFactory.create_triageScore_to_triageCategory_algo(mode="BASIC", thresholds=self.thresholds_data)
        triage_categories_mixed_types = algo.return_triage_categories(mixed_type_score_patients)
        self.assertEqual(triage_categories_mixed_types[0].triage_category, 'Category for score 50')
        self.assertEqual(triage_categories_mixed_types[1].triage_category, 'Category for score 50.5')

class CustomTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

class CustomTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return CustomTestResult(self.stream, self.descriptions, self.verbosity)

def generate_csv_report(test_timings, test_results):
    filename = "testing_report_triage_category.csv"
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
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTriageScoreToTriageCategory)
    runner = CustomTestRunner()
    result = runner.run(suite)
    generate_csv_report(TestTriageScoreToTriageCategory.test_timings, result.test_results)
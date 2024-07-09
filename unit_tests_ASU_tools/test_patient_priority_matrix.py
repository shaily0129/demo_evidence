import unittest
import csv
import os
from datetime import datetime

# Mock classes and functions

class MockPatient:
    def __init__(self, name, category):
        self.name = name
        self.category = category

class MockTriagecategoryToPatientMatrixAlgo:
    def return_patient_priority_matrix(self, patients):
        # Mock implementation: returns a simple transformation of the input
        return [MockMatrixPatient(patient.name, f"Priority for {patient.category}") for patient in patients]

class MockTriagecategoryToPatientmatrixFactory:
    @staticmethod
    def create_triageCategory_to_patientMatrix_algo(mode):
        return MockTriagecategoryToPatientMatrixAlgo()

class MockMatrixPatient:
    def __init__(self, patient_name, priority_details):
        self.patient_name = patient_name
        self.priority_details = priority_details

    def __str__(self):
        return self.priority_details

# Unit test case
class TestPatientPriorityMatrix(unittest.TestCase):

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
        # Setting up patients
        self.start_time = datetime.now()
        self.patient1_cat = MockPatient(name='Adrian Monk', category='immediate')
        self.patient2_cat = MockPatient(name='Natalie Tieger', category='immediate')
        self.patient3_cat = MockPatient(name='Leland Stottlemeyer', category='immediate')
        self.patient4_cat = MockPatient(name='Jake Peralta', category='expectant')
        self.patient5_cat = MockPatient(name='Sharona Fleming', category='delayed')
        self.patient6_cat = MockPatient(name='Randy Disher', category='expectant')
        self.patient7_cat = MockPatient(name='Trudy Monk', category='immediate')
        self.patient8_cat = MockPatient(name='Charles Kroger', category='minor')
        self.patient9_cat = MockPatient(name='Julie Trieger', category='delayed')
        self.patient10_cat = MockPatient(name='Benjy Fleming', category='delayed')
        self.all_patients_cat = [self.patient1_cat, self.patient2_cat, self.patient3_cat, self.patient4_cat, self.patient5_cat,
                                 self.patient6_cat, self.patient7_cat, self.patient8_cat, self.patient9_cat, self.patient10_cat]

    def test_patient_priority_matrix(self):
        print("")
        print("ALGO :: Patients Triage categories -> Patients priority matrix")
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(self.all_patients_cat)
        
        # Assertions and checks
        for matrix_patient in matrix_all_patients:
            self.assertIsNotNone(matrix_patient.patient_name)
            self.assertIsNotNone(matrix_patient.priority_details)  # Adjust according to actual properties

        for matrix_patient in matrix_all_patients:
            print('\n')
            print(f"Patient {matrix_patient.patient_name} has the following priority details: {matrix_patient}")

    def test_empty_patient_list(self):
        print("")
        print("ALGO :: Empty patient list")
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix([])
        
        self.assertEqual(matrix_all_patients, [])

    def test_invalid_category(self):
        print("")
        print("ALGO :: Invalid patient category")
        invalid_patient = MockPatient(name='Invalid Patient', category='unknown')
        patients = self.all_patients_cat + [invalid_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(matrix_all_patients[-1].priority_details, "Priority for unknown")

    def test_large_number_of_patients(self):
        print("")
        print("ALGO :: Large number of patients")
        large_patients_list = self.all_patients_cat * 1000  # 1000 times the current list
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(large_patients_list)
        
        self.assertEqual(len(matrix_all_patients), len(large_patients_list))

    def test_duplicate_patient_names(self):
        print("")
        print("ALGO :: Duplicate patient names")
        duplicate_patient = MockPatient(name='Adrian Monk', category='delayed')
        patients = self.all_patients_cat + [duplicate_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(len(matrix_all_patients), len(patients))
        duplicate_entries = [patient for patient in matrix_all_patients if patient.patient_name == 'Adrian Monk']
        self.assertEqual(len(duplicate_entries), 2)

    def test_single_patient(self):
        print("")
        print("ALGO :: Single patient")
        single_patient = [self.patient1_cat]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(single_patient)
        
        self.assertEqual(len(matrix_all_patients), 1)
        self.assertEqual(matrix_all_patients[0].patient_name, 'Adrian Monk')
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for immediate')

    def test_multiple_algorithms(self):
        print("")
        print("ALGO :: Multiple algorithms")
        algo_names = ["BASIC", "ADVANCED"]
        for algo_name in algo_names:
            algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode=algo_name)
            matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(self.all_patients_cat)
            
            for matrix_patient in matrix_all_patients:
                self.assertIsNotNone(matrix_patient.patient_name)
                self.assertIsNotNone(matrix_patient.priority_details)

    def test_patients_with_all_categories(self):
        print("")
        print("ALGO :: Patients with all categories")
        categories = ['immediate', 'delayed', 'minor', 'expectant']
        patients = [MockPatient(name=f'Patient {i}', category=cat) for i, cat in enumerate(categories)]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(len(matrix_all_patients), len(patients))
        for i, matrix_patient in enumerate(matrix_all_patients):
            self.assertEqual(matrix_patient.priority_details, f"Priority for {categories[i]}")

    def test_randomized_patient_list(self):
        import random
        print("")
        print("ALGO :: Randomized patient list")
        randomized_patients = self.all_patients_cat[:]
        random.shuffle(randomized_patients)
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(randomized_patients)
        
        self.assertEqual(len(matrix_all_patients), len(randomized_patients))
        for matrix_patient in matrix_all_patients:
            self.assertIsNotNone(matrix_patient.patient_name)
            self.assertIsNotNone(matrix_patient.priority_details)

    def test_edge_case_category_values(self):
        print("")
        print("ALGO :: Edge case category values")
        edge_case_patient = MockPatient(name='Edge Case', category='')
        patients = self.all_patients_cat + [edge_case_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(matrix_all_patients[-1].priority_details, "Priority for ")

    def test_patient_with_missing_data(self):
        print("")
        print("ALGO :: Patient with missing data")
        missing_data_patient = MockPatient(name='Missing Data', category=None)
        patients = self.all_patients_cat + [missing_data_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertIsNotNone(matrix_all_patients[-1].patient_name)
        self.assertEqual(matrix_all_patients[-1].priority_details, "Priority for None")

    def test_duplicate_patients(self):
        print("")
        print("ALGO :: Duplicate patients")
        duplicate_patient = MockPatient(name='Adrian Monk', category='immediate')
        patients = self.all_patients_cat + [duplicate_patient, duplicate_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(len(matrix_all_patients), len(patients))
        self.assertEqual(matrix_all_patients[-1].patient_name, 'Adrian Monk')
        self.assertEqual(matrix_all_patients[-1].priority_details, 'Priority for immediate')

    def test_empty_patient_list(self):
        print("")
        print("ALGO :: Empty patient list")
        patients = []
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(len(matrix_all_patients), 0)

    def test_mixed_valid_and_invalid_categories(self):
        print("")
        print("ALGO :: Mixed valid and invalid categories")
        valid_invalid_patients = self.all_patients_cat + [MockPatient(name='Invalid Patient', category='unknown')]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(valid_invalid_patients)
        
        self.assertEqual(len(matrix_all_patients), len(valid_invalid_patients))
        self.assertEqual(matrix_all_patients[-1].priority_details, 'Priority for unknown')

    def test_all_patients_same_category(self):
        print("")
        print("ALGO :: All patients same category")
        same_category_patients = [MockPatient(name=f'Patient {i}', category='immediate') for i in range(10)]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(same_category_patients)
        
        self.assertEqual(len(matrix_all_patients), len(same_category_patients))
        for matrix_patient in matrix_all_patients:
            self.assertEqual(matrix_patient.priority_details, "Priority for immediate")

    def test_patients_with_long_names(self):
        print("")
        print("ALGO :: Patients with long names")
        long_name_patient = MockPatient(name='A' * 1000, category='immediate')
        patients = self.all_patients_cat + [long_name_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(matrix_all_patients[-1].patient_name, 'A' * 1000)
        self.assertEqual(matrix_all_patients[-1].priority_details, 'Priority for immediate')

    def test_changing_algorithm_mode(self):
        print("")
        print("ALGO :: Changing algorithm mode")
        algo_modes = ["BASIC", "ADVANCED"]
        for mode in algo_modes:
            algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode=mode)
            matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(self.all_patients_cat)
            
            self.assertEqual(len(matrix_all_patients), len(self.all_patients_cat))
            for matrix_patient in matrix_all_patients:
                self.assertIsNotNone(matrix_patient.patient_name)
                self.assertIsNotNone(matrix_patient.priority_details)

    def test_patients_with_special_characters_in_names(self):
        print("")
        print("ALGO :: Patients with special characters in names")
        special_char_patient = MockPatient(name='@drian_Monk!', category='immediate')
        patients = self.all_patients_cat + [special_char_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(matrix_all_patients[-1].patient_name, '@drian_Monk!')
        self.assertEqual(matrix_all_patients[-1].priority_details, 'Priority for immediate')

    def test_patients_with_numeric_names(self):
        print("")
        print("ALGO :: Patients with numeric names")
        numeric_name_patient = MockPatient(name='12345', category='immediate')
        patients = self.all_patients_cat + [numeric_name_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(matrix_all_patients[-1].patient_name, '12345')
        self.assertEqual(matrix_all_patients[-1].priority_details, 'Priority for immediate')

    def test_patients_with_mixed_case_categories(self):
        print("")
        print("ALGO :: Patients with mixed case categories")
        mixed_case_patient = MockPatient(name='Mixed Case', category='ImMeDiAtE')
        patients = self.all_patients_cat + [mixed_case_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(matrix_all_patients[-1].patient_name, 'Mixed Case')
        self.assertEqual(matrix_all_patients[-1].priority_details, 'Priority for ImMeDiAtE')

    def test_patients_with_empty_string_names(self):
        print("")
        print("ALGO :: Patients with empty string names")
        empty_string_name_patient = MockPatient(name='', category='immediate')
        patients = self.all_patients_cat + [empty_string_name_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(matrix_all_patients[-1].patient_name, '')
        self.assertEqual(matrix_all_patients[-1].priority_details, 'Priority for immediate')

    def test_very_large_number_of_patients(self):
        print("")
        print("ALGO :: Very large number of patients")
        large_number_patients = [MockPatient(name=f'Patient {i}', category='immediate') for i in range(1000)]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(large_number_patients)
        
        self.assertEqual(len(matrix_all_patients), len(large_number_patients))
        for matrix_patient in matrix_all_patients:
            self.assertEqual(matrix_patient.priority_details, 'Priority for immediate')

    def test_patients_with_mixed_valid_and_invalid_names(self):
        print("")
        print("ALGO :: Patients with mixed valid and invalid names")
        valid_invalid_name_patients = self.all_patients_cat + [MockPatient(name=None, category='immediate'), MockPatient(name='', category='delayed')]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(valid_invalid_name_patients)
        
        self.assertEqual(matrix_all_patients[-2].patient_name, None)
        self.assertEqual(matrix_all_patients[-2].priority_details, 'Priority for immediate')
        self.assertEqual(matrix_all_patients[-1].patient_name, '')
        self.assertEqual(matrix_all_patients[-1].priority_details, 'Priority for delayed')

    def test_patients_with_boundary_case_categories(self):
        print("")
        print("ALGO :: Patients with boundary case categories")
        boundary_case_patients = [MockPatient(name=f'Patient {i}', category='critical') for i in range(5)]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(boundary_case_patients)
        
        self.assertEqual(len(matrix_all_patients), len(boundary_case_patients))
        for matrix_patient in matrix_all_patients:
            self.assertEqual(matrix_patient.priority_details, 'Priority for critical')

    def test_patients_with_different_categories_and_same_names(self):
        print("")
        print("ALGO :: Patients with different categories and same names")
        same_name_patients = [MockPatient(name='Patient', category='immediate'), MockPatient(name='Patient', category='delayed')]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(same_name_patients)
        
        self.assertEqual(len(matrix_all_patients), len(same_name_patients))
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for immediate')
        self.assertEqual(matrix_all_patients[1].priority_details, 'Priority for delayed')

    def test_empty_patients_list(self):
        print("")
        print("ALGO :: Empty patients list")
        empty_patients = []
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(empty_patients)
        
        self.assertEqual(len(matrix_all_patients), 0)

    def test_patients_with_special_character_names(self):
        print("")
        print("ALGO :: Patients with special character names")
        special_char_patient = MockPatient(name='!@#$', category='immediate')
        patients = self.all_patients_cat + [special_char_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(matrix_all_patients[-1].patient_name, '!@#$')
        self.assertEqual(matrix_all_patients[-1].priority_details, 'Priority for immediate')

    def test_patients_with_extremely_long_names(self):
        print("")
        print("ALGO :: Patients with extremely long names")
        long_name_patient = MockPatient(name='A' * 1000, category='immediate')
        patients = self.all_patients_cat + [long_name_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(matrix_all_patients[-1].patient_name, 'A' * 1000)
        self.assertEqual(matrix_all_patients[-1].priority_details, 'Priority for immediate')

    def test_patients_with_null_category(self):
        print("")
        print("ALGO :: Patients with null category")
        null_category_patient = MockPatient(name='Null Category', category=None)
        patients = self.all_patients_cat + [null_category_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(matrix_all_patients[-1].patient_name, 'Null Category')
        self.assertEqual(matrix_all_patients[-1].priority_details, 'Priority for None')

    def test_patients_with_same_name_different_cases(self):
        print("")
        print("ALGO :: Patients with same name but different cases")
        same_name_diff_case_patients = [MockPatient(name='Patient', category='immediate'), MockPatient(name='patient', category='delayed')]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(same_name_diff_case_patients)
        
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for immediate')
        self.assertEqual(matrix_all_patients[1].priority_details, 'Priority for delayed')

    def test_patients_with_white_space_in_names(self):
        print("")
        print("ALGO :: Patients with white space in names")
        white_space_patient = MockPatient(name='Patient With Space', category='immediate')
        patients = self.all_patients_cat + [white_space_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(matrix_all_patients[-1].patient_name, 'Patient With Space')
        self.assertEqual(matrix_all_patients[-1].priority_details, 'Priority for immediate')

    def test_patients_with_trailing_white_space_in_names(self):
        print("")
        print("ALGO :: Patients with trailing white space in names")
        trailing_space_patient = MockPatient(name='TrailingSpace ', category='immediate')
        patients = self.all_patients_cat + [trailing_space_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(matrix_all_patients[-1].patient_name, 'TrailingSpace ')
        self.assertEqual(matrix_all_patients[-1].priority_details, 'Priority for immediate')

    def test_patients_with_mixed_valid_and_invalid_categories(self):
        print("")
        print("ALGO :: Patients with mixed valid and invalid categories")
        mixed_categories_patients = [MockPatient(name='Valid Category', category='immediate'), MockPatient(name='Invalid Category', category='unknown')]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(mixed_categories_patients)
        
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for immediate')
        self.assertEqual(matrix_all_patients[1].priority_details, 'Priority for unknown')

    def test_patients_with_non_string_categories(self):
        print("")
        print("ALGO :: Patients with non-string categories")
        non_string_category_patient = MockPatient(name='Non String Category', category=123)
        patients = self.all_patients_cat + [non_string_category_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(matrix_all_patients[-1].patient_name, 'Non String Category')
        self.assertEqual(matrix_all_patients[-1].priority_details, 'Priority for 123')

    def test_patients_with_all_categories_same(self):
        print("")
        print("ALGO :: Patients with all categories same")
        same_category_patients = [MockPatient(name=f'Patient{i}', category='immediate') for i in range(1, 11)]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(same_category_patients)
        
        for patient in matrix_all_patients:
            self.assertEqual(patient.priority_details, 'Priority for immediate')

    def test_patients_with_numeric_names(self):
        print("")
        print("ALGO :: Patients with numeric names")
        numeric_name_patients = [MockPatient(name=str(i), category='immediate') for i in range(1, 6)]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(numeric_name_patients)
        
        for patient in matrix_all_patients:
            self.assertEqual(patient.priority_details, 'Priority for immediate')

    def test_patients_with_numeric_names(self):
        print("")
        print("ALGO :: Patients with numeric names")
        numeric_name_patients = [MockPatient(name=str(i), category='immediate') for i in range(1, 6)]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(numeric_name_patients)
        
        for patient in matrix_all_patients:
            self.assertEqual(patient.priority_details, 'Priority for immediate')

    def test_patients_with_no_name(self):
        print("")
        print("ALGO :: Patients with no name")
        no_name_patient = MockPatient(name='', category='immediate')
        patients = self.all_patients_cat + [no_name_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertEqual(matrix_all_patients[-1].patient_name, '')
        self.assertEqual(matrix_all_patients[-1].priority_details, 'Priority for immediate')

    def test_duplicate_patients(self):
        print("")
        print("ALGO :: Duplicate patients")
        duplicate_patients = [MockPatient(name='Duplicate Patient', category='immediate'), MockPatient(name='Duplicate Patient', category='immediate')]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(duplicate_patients)
        
        for patient in matrix_all_patients:
            self.assertEqual(patient.priority_details, 'Priority for immediate')

    def test_patients_with_null_name(self):
        print("")
        print("ALGO :: Patients with null name")
        null_name_patient = MockPatient(name=None, category='immediate')
        patients = self.all_patients_cat + [null_name_patient]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients)
        
        self.assertIsNone(matrix_all_patients[-1].patient_name)
        self.assertEqual(matrix_all_patients[-1].priority_details, 'Priority for immediate')

    def test_patients_with_mixed_data_types_in_categories(self):
        print("")
        print("ALGO :: Patients with mixed data types in categories")
        mixed_data_type_patients = [
            MockPatient(name='Patient1', category='immediate'),
            MockPatient(name='Patient2', category=123),
            MockPatient(name='Patient3', category=45.6)
        ]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(mixed_data_type_patients)
        
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for immediate')
        self.assertEqual(matrix_all_patients[1].priority_details, 'Priority for 123')
        self.assertEqual(matrix_all_patients[2].priority_details, 'Priority for 45.6')

    def test_patients_with_very_long_names(self):
        print("")
        print("ALGO :: Patients with very long names")
        long_name_patient = MockPatient(name='A' * 1000, category='immediate')
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix([long_name_patient])
        
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for immediate')

    def test_patients_with_empty_list(self):
        print("")
        print("ALGO :: Patients with empty list")
        empty_patients_list = []
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(empty_patients_list)
        
        self.assertEqual(len(matrix_all_patients), 0)

    def test_patients_with_none_as_category(self):
        print("")
        print("ALGO :: Patients with None as category")
        none_category_patients = [MockPatient(name='Patient1', category=None)]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(none_category_patients)
        
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for None')

    def test_patients_with_mixed_data_types_in_names(self):
        print("")
        print("ALGO :: Patients with mixed data types in names")
        mixed_name_patients = [
            MockPatient(name='Patient1', category='immediate'),
            MockPatient(name=123, category='immediate'),
            MockPatient(name=45.6, category='immediate')
        ]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(mixed_name_patients)
        
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for immediate')
        self.assertEqual(matrix_all_patients[1].priority_details, 'Priority for immediate')
        self.assertEqual(matrix_all_patients[2].priority_details, 'Priority for immediate')

    def test_large_number_of_mixed_categories(self):
        print("")
        print("ALGO :: Large number of mixed categories")
        mixed_category_patients = [MockPatient(name=f'Patient{i}', category='immediate' if i % 2 == 0 else 'delayed') for i in range(1, 101)]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(mixed_category_patients)
        
        self.assertEqual(len(matrix_all_patients), 100)
        for i, patient in enumerate(matrix_all_patients):
            expected_category = 'immediate' if (i + 1) % 2 == 0 else 'delayed'
            self.assertEqual(patient.priority_details, f'Priority for {expected_category}')

    def test_patients_with_special_category_names(self):
        print("")
        print("ALGO :: Patients with special category names")
        special_category_patients = [MockPatient(name='PatientSpecial', category='@#$%')]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(special_category_patients)
        
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for @#$%')

    def test_patients_with_duplicate_names(self):
        print("")
        print("ALGO :: Patients with duplicate names")
        duplicate_name_patients = [
            MockPatient(name='PatientDuplicate', category='immediate'),
            MockPatient(name='PatientDuplicate', category='delayed')
        ]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(duplicate_name_patients)
        
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for immediate')
        self.assertEqual(matrix_all_patients[1].priority_details, 'Priority for delayed')

    def test_patients_with_whitespace_in_names(self):
        print("")
        print("ALGO :: Patients with whitespace in names")
        whitespace_name_patients = [MockPatient(name='Patient With Space', category='immediate')]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(whitespace_name_patients)
        
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for immediate')

    def test_patients_with_numbers_in_category(self):
        print("")
        print("ALGO :: Patients with numbers in category")
        number_category_patients = [MockPatient(name='PatientNumberCategory', category='1234')]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(number_category_patients)
        
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for 1234')

    def test_patients_with_leading_trailing_whitespace_in_names(self):
        print("")
        print("ALGO :: Patients with leading/trailing whitespace in names")
        whitespace_name_patients = [MockPatient(name='  PatientWhitespace  ', category='immediate')]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(whitespace_name_patients)
        
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for immediate')
        self.assertEqual(matrix_all_patients[0].patient_name.strip(), 'PatientWhitespace')

    def test_patients_with_various_data_types_in_category(self):
        print("")
        print("ALGO :: Patients with various data types in category")
        various_data_patients = [
            MockPatient(name='PatientString', category='delayed'),
            MockPatient(name='PatientInt', category=123),
            MockPatient(name='PatientFloat', category=12.34),
            MockPatient(name='PatientNone', category=None),
        ]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(various_data_patients)
        
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for delayed')
        self.assertEqual(matrix_all_patients[1].priority_details, 'Priority for 123')
        self.assertEqual(matrix_all_patients[2].priority_details, 'Priority for 12.34')
        self.assertEqual(matrix_all_patients[3].priority_details, 'Priority for None')

    def test_patients_with_mixed_valid_and_invalid_data(self):
        print("")
        print("ALGO :: Patients with mixed valid and invalid data")
        mixed_data_patients = [
            MockPatient(name='Valid Patient', category='immediate'),
            MockPatient(name='Invalid Patient', category=None),
            MockPatient(name='Another Valid Patient', category='delayed'),
        ]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(mixed_data_patients)
        
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for immediate')
        self.assertEqual(matrix_all_patients[1].priority_details, 'Priority for None')
        self.assertEqual(matrix_all_patients[2].priority_details, 'Priority for delayed')

    def test_patients_with_non_string_names(self):
        print("")
        print("ALGO :: Patients with non-string names")
        non_string_name_patients = [
            MockPatient(name=123, category='immediate'),
            MockPatient(name=12.34, category='delayed'),
            MockPatient(name=None, category='expectant'),
        ]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(non_string_name_patients)
        
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for immediate')
        self.assertEqual(matrix_all_patients[1].priority_details, 'Priority for delayed')
        self.assertEqual(matrix_all_patients[2].priority_details, 'Priority for expectant')

    def test_patients_with_large_variability_in_priority_details(self):
        print("")
        print("ALGO :: Patients with large variability in priority details")
        patients_with_large_variability = [
            MockPatient(name='Patient1', category='immediate'),
            MockPatient(name='Patient2', category='expectant'),
            MockPatient(name='Patient3', category='delayed'),
            MockPatient(name='Patient4', category='minor'),
            MockPatient(name='Patient5', category='immediate'),
            MockPatient(name='Patient6', category='expectant'),
            MockPatient(name='Patient7', category='minor'),
            MockPatient(name='Patient8', category='delayed'),
        ]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients_with_large_variability)
        
        self.assertEqual(len(matrix_all_patients), 8)
        self.assertIn(matrix_all_patients[0].priority_details, ['Priority for immediate', 'Priority for expectant', 'Priority for delayed', 'Priority for minor'])
        self.assertIn(matrix_all_patients[1].priority_details, ['Priority for immediate', 'Priority for expectant', 'Priority for delayed', 'Priority for minor'])
        self.assertIn(matrix_all_patients[2].priority_details, ['Priority for immediate', 'Priority for expectant', 'Priority for delayed', 'Priority for minor'])
        self.assertIn(matrix_all_patients[3].priority_details, ['Priority for immediate', 'Priority for expectant', 'Priority for delayed', 'Priority for minor'])
        self.assertIn(matrix_all_patients[4].priority_details, ['Priority for immediate', 'Priority for expectant', 'Priority for delayed', 'Priority for minor'])
        self.assertIn(matrix_all_patients[5].priority_details, ['Priority for immediate', 'Priority for expectant', 'Priority for delayed', 'Priority for minor'])
        self.assertIn(matrix_all_patients[6].priority_details, ['Priority for immediate', 'Priority for expectant', 'Priority for delayed', 'Priority for minor'])
        self.assertIn(matrix_all_patients[7].priority_details, ['Priority for immediate', 'Priority for expectant', 'Priority for delayed', 'Priority for minor'])


    def test_patients_with_unknown_categories(self):
        print("")
        print("ALGO :: Patients with unknown categories")
        patients_with_unknown_categories = [
            MockPatient(name='Patient1', category='unknown'),
            MockPatient(name='Patient2', category='unknown'),
            MockPatient(name='Patient3', category='unknown'),
        ]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients_with_unknown_categories)
        
        for patient in matrix_all_patients:
            self.assertEqual(patient.priority_details, 'Priority for unknown')


    def test_patients_with_no_categories_provided(self):
        print("")
        print("ALGO :: Patients with no categories provided")
        patients_with_no_categories = [
            MockPatient(name='Patient1', category=None),
            MockPatient(name='Patient2', category=None),
            MockPatient(name='Patient3', category=None),
        ]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(patients_with_no_categories)
        
        for patient in matrix_all_patients:
            self.assertEqual(patient.priority_details, 'Priority for None')


    def return_patient_priority_matrix(self, patients):
        matrix_patients = []
        for patient in patients:
            if patient.category == 'immediate':
                priority_details = 'Custom priority for immediate'
            elif patient.category == 'delayed':
                priority_details = 'Custom priority for delayed'
            elif patient.category == 'expectant':
                priority_details = 'Custom priority for expectant'
            else:
                priority_details = f'Priority for {patient.category}'
            
            matrix_patients.append(MockMatrixPatient(patient.name, priority_details))
        
        return matrix_patients


    def test_patients_with_edge_case_categories(self):
        print("")
        print("ALGO :: Patients with edge case categories")
        edge_case_category_patients = [
            MockPatient(name='Patient1', category=''),
            MockPatient(name='Patient2', category=' '),
            MockPatient(name='Patient3', category='  '),
            MockPatient(name='Patient4', category='minor  '),
            MockPatient(name='Patient5', category='   delayed   '),
        ]
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix(edge_case_category_patients)
        
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for ')
        self.assertEqual(matrix_all_patients[1].priority_details, 'Priority for  ')
        self.assertEqual(matrix_all_patients[2].priority_details, 'Priority for   ')
        self.assertEqual(matrix_all_patients[3].priority_details, 'Priority for minor  ')
        self.assertEqual(matrix_all_patients[4].priority_details, 'Priority for    delayed   ')

    def test_patients_with_non_ascii_characters_in_names(self):
        print("")
        print("ALGO :: Patients with non-ASCII characters in names")
        non_ascii_name_patient = MockPatient(name='Patient with ñôn-ÃSCÏÏ Çhárãçtérs', category='immediate')
        
        algo_patient_matrix = MockTriagecategoryToPatientmatrixFactory.create_triageCategory_to_patientMatrix_algo(mode="BASIC")
        matrix_all_patients = algo_patient_matrix.return_patient_priority_matrix([non_ascii_name_patient])
        
        self.assertEqual(matrix_all_patients[0].priority_details, 'Priority for immediate')
        self.assertEqual(matrix_all_patients[0].patient_name, 'Patient with ñôn-ÃSCÏÏ Çhárãçtérs')


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
    filename = "testing_report_patient_priority_matrix.csv"
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
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPatientPriorityMatrix)
    runner = CustomTestRunner()
    result = runner.run(suite)
    generate_csv_report(TestPatientPriorityMatrix.test_timings, result.test_results)
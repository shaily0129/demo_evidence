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
    def __init__(self, name, **kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)


class MockTriageAlgo:
    def __init__(self, thresholds):
        self.thresholds = thresholds

    def triage(self, patients):
        # Mock implementation: returns a simple transformation of the input
        return [
            MockTriageScore(
                patient.name,
                sum([getattr(patient, attr, 0) for attr in self.thresholds]),
            )
            for patient in patients
        ]


class MockTriageFactory:
    @staticmethod
    def create_triage_algo(algo_name, thresholds):
        return MockTriageAlgo(thresholds)


class MockTriageScore:
    def __init__(self, patient_name, score):
        self.patient_name = patient_name
        self.score = score

    def __str__(self):
        return f"Score: {self.score}"


# Unit test case
class TestPatientTriage(unittest.TestCase):
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
        self.thresholds_data_algo3 = {
            "external_hemorrhage": MockThreshold(min_value=1, max_value=6),
            "tension_pneumothorax": MockThreshold(min_value=1, max_value=6),
            "traumatic_brain_injury": MockThreshold(min_value=1, max_value=6),
            "burn": MockThreshold(min_value=1, max_value=6),
            "gcs": MockThreshold(min_value=3, max_value=15),
            "sbp": MockThreshold(min_value=0, max_value=219),
            "rr": MockThreshold(min_value=0, max_value=100),
        }

        self.patient1 = MockPatient(
            name="Adrian Monk",
            external_hemorrhage=3,
            tension_pneumothorax=4,
            traumatic_brain_injury=6,
            burn=2,
            gcs=10,
            sbp=60,
            rr=20,
        )
        self.patient2 = MockPatient(
            name="Natalie Tieger", splenic_laceration=6, gcs=6, sbp=100, rr=40
        )
        self.patient3 = MockPatient(
            name="Leland Stottlemeyer", external_hemorrhage=5, burn=6
        )
        self.patient4 = MockPatient(
            name="Jake Peralta",
            liver_hematoma=4,
            tension_pneumothorax=6,
            traumatic_brain_injury=4,
            burn=6,
            gcs=5,
            sbp=120,
            rr=88,
        )
        self.patient5 = MockPatient(name="Sharona Fleming", gcs=12, sbp=120, rr=89)
        self.patient6 = MockPatient(
            name="Randy Disher",
            external_hemorrhage=5,
            tension_pneumothorax=6,
            traumatic_brain_injury=6,
            burn=2,
            gcs=15,
            sbp=80,
            rr=60,
        )
        self.patient7 = MockPatient(
            name="Trudy Monk", splenic_laceration=6, gcs=6, sbp=100, rr=40
        )
        self.patient8 = MockPatient(
            name="Charles Kroger", external_hemorrhage=2, burn=1
        )
        self.patient9 = MockPatient(
            name="Julie Trieger",
            liver_hematoma=1,
            tension_pneumothorax=1,
            traumatic_brain_injury=1,
            burn=1,
            gcs=4,
            sbp=40,
            rr=20,
        )
        self.patient10 = MockPatient(name="Benjy Fleming", gcs=12, sbp=120, rr=89)
        self.all_patients = [
            self.patient1,
            self.patient2,
            self.patient3,
            self.patient4,
            self.patient5,
            self.patient6,
            self.patient7,
            self.patient8,
            self.patient9,
            self.patient10,
        ]

    def test_patient_triage(self):
        print("")
        print("ALGO 3- LIFETriage")
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_score_all_patients = triage_life_algo.triage(self.all_patients)

        # Assertions and checks
        for triage_score_patient in triage_score_all_patients:
            self.assertIsNotNone(triage_score_patient.patient_name)
            self.assertIsNotNone(
                triage_score_patient.score
            )  # Adjust according to actual properties

        for triage_score_patient in triage_score_all_patients:
            print("\n\n")
            print(
                f"Patient has the following LIFE Triage Scores {triage_score_patient}"
            )

    def test_empty_patient_list(self):
        # Test case for an empty list of patients
        empty_patient_list = []
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage(empty_patient_list)
        self.assertEqual(triage_scores, [])

    def test_patient_with_missing_attributes(self):
        # Test case for a patient missing some attributes
        patient_with_missing_attrs = MockPatient(name="John Doe")
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage([patient_with_missing_attrs])
        self.assertEqual(triage_scores[0].score, 0)

    def test_patient_with_extra_attributes(self):
        # Test case for a patient with extra attributes not in thresholds
        patient_with_extra_attrs = MockPatient(
            name="Jane Doe", gcs=14, sbp=110, rr=22, extra_attr=5
        )
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage([patient_with_extra_attrs])
        self.assertEqual(triage_scores[0].score, 146)  # Sum of gcs, sbp, rr

    def test_threshold_bounds(self):
        # Test case for patients with attributes exactly at threshold bounds
        patient_at_bounds = MockPatient(
            name="Bounds Patient",
            external_hemorrhage=1,
            tension_pneumothorax=6,
            traumatic_brain_injury=6,
            burn=1,
            gcs=3,
            sbp=0,
            rr=100,
        )
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage([patient_at_bounds])
        self.assertEqual(triage_scores[0].score, 117)  # Sum of all attributes

    def test_all_zero_scores(self):
        # Test case for a patient with all zero scores
        patient_all_zero = MockPatient(
            name="Zero Patient",
            external_hemorrhage=0,
            tension_pneumothorax=0,
            traumatic_brain_injury=0,
            burn=0,
            gcs=0,
            sbp=0,
            rr=0,
        )
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage([patient_all_zero])
        self.assertEqual(triage_scores[0].score, 0)

    def test_single_patient(self):
        # Test case for a single patient
        single_patient = MockPatient(
            name="Single Patient", gcs=10, sbp=80, rr=30
        )
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage([single_patient])
        self.assertEqual(triage_scores[0].score, 120)  # Sum of gcs, sbp, rr

    def test_no_patients(self):
        # Test case for no patients provided
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage([])
        self.assertEqual(len(triage_scores), 0)


    def test_patients_with_identical_scores(self):
        # Test case for multiple patients with identical scores
        identical_score_patients = [
            MockPatient(name='Identical Patient 1', gcs=10, sbp=80, rr=30),
            MockPatient(name='Identical Patient 2', gcs=10, sbp=80, rr=30),
        ]
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage(identical_score_patients)
        self.assertEqual(triage_scores[0].score, 120)
        self.assertEqual(triage_scores[1].score, 120)

    def test_mixed_patient_scores(self):
        # Test case for patients with mixed scores (some attributes missing)
        mixed_score_patients = [
            MockPatient(name='Mixed Patient 1', gcs=10, sbp=80, rr=30),
            MockPatient(name='Mixed Patient 2', gcs=10, sbp=80),
        ]
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage(mixed_score_patients)
        self.assertEqual(triage_scores[0].score, 120)
        self.assertEqual(triage_scores[1].score, 90)  # Missing rr defaults to 0
        

    def test_patients_with_negative_scores(self):
        # Test case for a patient with negative attribute scores
        patient_with_negative_scores = MockPatient(
            name="Negative Score Patient", gcs=-5, sbp=-20, rr=-10
        )
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage([patient_with_negative_scores])
        self.assertEqual(triage_scores[0].score, -35)  # Sum of gcs, sbp, rr

    def test_patients_with_non_numeric_scores(self):
        # Test case for a patient with non-numeric attribute scores
        patient_with_non_numeric_scores = MockPatient(
            name="Non Numeric Score Patient", gcs="high", sbp="normal", rr="low"
        )
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        with self.assertRaises(TypeError):
            triage_life_algo.triage([patient_with_non_numeric_scores])

    def test_large_number_of_patients(self):
        # Test case for handling a large number of patients
        large_number_of_patients = [MockPatient(name=f"Patient {i}", gcs=10, sbp=80, rr=30) for i in range(1000)]
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage(large_number_of_patients)
        self.assertEqual(len(triage_scores), 1000)


    def test_patients_with_mixed_data_types(self):
        # Test case for patients with mixed data types in attributes
        mixed_data_type_patients = [
            MockPatient(name="Mixed Type Patient 1", gcs=10, sbp="eighty", rr=30),
            MockPatient(name="Mixed Type Patient 2", gcs="ten", sbp=80, rr=30),
        ]
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        with self.assertRaises(TypeError):
            triage_life_algo.triage(mixed_data_type_patients)

    def test_duplicate_patients(self):
        # Test case for duplicate patients
        duplicate_patients = [
            MockPatient(name="Duplicate Patient", gcs=10, sbp=80, rr=30),
            MockPatient(name="Duplicate Patient", gcs=10, sbp=80, rr=30),
        ]
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage(duplicate_patients)
        self.assertEqual(len(triage_scores), 2)
        self.assertEqual(triage_scores[0].score, 120)
        self.assertEqual(triage_scores[1].score, 120)

    def test_invalid_attribute_name(self):
        # Test case for an invalid attribute name
        patient_with_invalid_attr = MockPatient(
            name="Invalid Attr Patient", invalid_attr=10
        )
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage([patient_with_invalid_attr])
        self.assertEqual(triage_scores[0].score, 0)  # Attribute not in thresholds

    def test_empty_patients(self):
        # Test case for empty list of patients
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage([])
        self.assertEqual(len(triage_scores), 0)

    def test_single_patient(self):
        # Test case for a single patient
        single_patient = MockPatient(
            name="Single Patient", gcs=10, sbp=80, rr=30
        )
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage([single_patient])
        self.assertEqual(len(triage_scores), 1)
        self.assertEqual(triage_scores[0].score, 120)

    def test_patients_with_no_common_attributes(self):
        # Test case for patients with no common attributes
        patients_no_common_attrs = [
            MockPatient(name="Patient 1", attribute1=10),
            MockPatient(name="Patient 2", attribute2=20),
        ]
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage(patients_no_common_attrs)
        self.assertEqual(len(triage_scores), 2)
        self.assertEqual(triage_scores[0].score, 0)
        self.assertEqual(triage_scores[1].score, 0)

    def test_patients_with_all_attributes(self):
        # Test case for patients with all attributes
        patients_with_all_attributes = [
            MockPatient(name="Patient 1", **{
                key: 5 for key in self.thresholds_data_algo3.keys()
            }),
            MockPatient(name="Patient 2", **{
                key: 6 for key in self.thresholds_data_algo3.keys()
            }),
        ]
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage(patients_with_all_attributes)
        self.assertEqual(len(triage_scores), 2)
        self.assertEqual(triage_scores[0].score, 35)  # Sum of all attributes
        self.assertEqual(triage_scores[1].score, 42)  # Sum of all attributes

    def test_multiple_triage_algorithms(self):
        # Test case for handling multiple triage algorithms
        thresholds_algo1 = {
            "gcs": MockThreshold(min_value=3, max_value=15),
            "sbp": MockThreshold(min_value=80, max_value=120),
            "rr": MockThreshold(min_value=12, max_value=25),
        }
        thresholds_algo2 = {
            "gcs": MockThreshold(min_value=3, max_value=12),
            "sbp": MockThreshold(min_value=90, max_value=140),
            "rr": MockThreshold(min_value=10, max_value=30),
        }
        patients = [
            MockPatient(name="Patient 1", gcs=10, sbp=100, rr=20),
            MockPatient(name="Patient 2", gcs=15, sbp=110, rr=25),
        ]

        triage_algo1 = MockTriageFactory.create_triage_algo(
            algo_name="Algorithm 1", thresholds=thresholds_algo1
        )
        triage_algo2 = MockTriageFactory.create_triage_algo(
            algo_name="Algorithm 2", thresholds=thresholds_algo2
        )

        triage_scores_algo1 = triage_algo1.triage(patients)
        triage_scores_algo2 = triage_algo2.triage(patients)

        self.assertEqual(len(triage_scores_algo1), 2)
        self.assertEqual(len(triage_scores_algo2), 2)
        self.assertEqual(triage_scores_algo1[0].score, 130)  # Sum of scores
        self.assertEqual(triage_scores_algo1[1].score, 150)  # Sum of scores
        self.assertEqual(triage_scores_algo2[0].score, 130)  # Sum of scores
        self.assertEqual(triage_scores_algo2[1].score, 150)  # Sum of scores

    def test_high_threshold_values(self):
        # Test case for high threshold values
        thresholds_high_values = {
            "gcs": MockThreshold(min_value=0, max_value=9999),
            "sbp": MockThreshold(min_value=0, max_value=9999),
            "rr": MockThreshold(min_value=0, max_value=9999),
        }
        patient_high_values = MockPatient(name="High Values Patient", gcs=5000, sbp=8000, rr=6000)
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=thresholds_high_values
        )
        triage_scores = triage_life_algo.triage([patient_high_values])
        self.assertEqual(len(triage_scores), 1)
        self.assertEqual(triage_scores[0].score, 19000)  # Sum of scores

    def test_no_patients(self):
        # Test case for handling no patients
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage([])
        self.assertEqual(len(triage_scores), 0)

    def test_single_attribute_threshold(self):
        # Test case for a single attribute in thresholds
        thresholds_single_attr = {
            "gcs": MockThreshold(min_value=3, max_value=15),
        }
        patients = [
            MockPatient(name="Patient 1", gcs=10),
            MockPatient(name="Patient 2", gcs=5),
        ]
        triage_algo_single_attr = MockTriageFactory.create_triage_algo(
            algo_name="Single Attribute", thresholds=thresholds_single_attr
        )
        triage_scores = triage_algo_single_attr.triage(patients)
        self.assertEqual(len(triage_scores), 2)
        self.assertEqual(triage_scores[0].score, 10)
        self.assertEqual(triage_scores[1].score, 5)

    def test_no_common_attributes(self):
        # Test case for patients with no common attributes in thresholds
        patients_no_common_attrs = [
            MockPatient(name="Patient 1", attribute1=10),
            MockPatient(name="Patient 2", attribute2=20),
        ]
        thresholds_no_common_attrs = {
            "gcs": MockThreshold(min_value=3, max_value=15),
            "sbp": MockThreshold(min_value=80, max_value=120),
            "rr": MockThreshold(min_value=12, max_value=25),
        }
        triage_algo_no_common_attrs = MockTriageFactory.create_triage_algo(
            algo_name="No Common Attributes", thresholds=thresholds_no_common_attrs
        )
        triage_scores = triage_algo_no_common_attrs.triage(patients_no_common_attrs)
        self.assertEqual(len(triage_scores), 2)
        self.assertEqual(triage_scores[0].score, 0)
        self.assertEqual(triage_scores[1].score, 0)

    def test_large_number_of_patients(self):
        # Test case for handling a large number of patients
        large_number_of_patients = [
            MockPatient(name=f"Patient {i}", gcs=10, sbp=120, rr=20)
            for i in range(1000)
        ]
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage(large_number_of_patients)
        self.assertEqual(len(triage_scores), 1000)
        for score in triage_scores:
            self.assertEqual(score.score, 150)

    def test_single_patient_single_attribute(self):
        # Test case for a single patient with a single attribute
        thresholds_single_attr = {
            "gcs": MockThreshold(min_value=3, max_value=15),
        }
        single_patient_single_attr = [
            MockPatient(name="Patient 1", gcs=10),
        ]
        triage_algo_single_attr = MockTriageFactory.create_triage_algo(
            algo_name="Single Patient Single Attribute", thresholds=thresholds_single_attr
        )
        triage_scores = triage_algo_single_attr.triage(single_patient_single_attr)
        self.assertEqual(len(triage_scores), 1)
        self.assertEqual(triage_scores[0].score, 10)

    def test_all_patients_below_threshold(self):
        # Test case for all patients scoring below thresholds
        thresholds_all_below = {
            "gcs": MockThreshold(min_value=3, max_value=15),
            "sbp": MockThreshold(min_value=80, max_value=120),
            "rr": MockThreshold(min_value=12, max_value=25),
        }
        patients_all_below = [
            MockPatient(name="Patient 1", gcs=2, sbp=79, rr=11),
            MockPatient(name="Patient 2", gcs=1, sbp=60, rr=10),
        ]
        triage_algo_all_below = MockTriageFactory.create_triage_algo(
            algo_name="All Patients Below Threshold", thresholds=thresholds_all_below
        )
        triage_scores = triage_algo_all_below.triage(patients_all_below)
        self.assertEqual(len(triage_scores), 2)
        self.assertEqual(triage_scores[0].score, 92)
        self.assertEqual(triage_scores[1].score, 71)

    def test_large_range_thresholds(self):
        # Test case for large range thresholds
        thresholds_large_range = {
            "gcs": MockThreshold(min_value=0, max_value=1000),
            "sbp": MockThreshold(min_value=0, max_value=200),
            "rr": MockThreshold(min_value=0, max_value=50),
        }
        patients_large_range = [
            MockPatient(name="Patient 1", gcs=500, sbp=150, rr=25),
            MockPatient(name="Patient 2", gcs=800, sbp=180, rr=35),
        ]
        triage_algo_large_range = MockTriageFactory.create_triage_algo(
            algo_name="Large Range Thresholds", thresholds=thresholds_large_range
        )
        triage_scores = triage_algo_large_range.triage(patients_large_range)
        self.assertEqual(len(triage_scores), 2)
        self.assertEqual(triage_scores[0].score, 675)
        self.assertEqual(triage_scores[1].score, 1015)

    def test_single_attribute_single_patient(self):
        # Test case for a single patient with a single attribute
        thresholds_single_attr = {
            "gcs": MockThreshold(min_value=3, max_value=15),
        }
        patient_single_attr = MockPatient(name="Patient 1", gcs=10)
        triage_algo_single_attr = MockTriageFactory.create_triage_algo(
            algo_name="Single Attribute Single Patient", thresholds=thresholds_single_attr
        )
        triage_scores = triage_algo_single_attr.triage([patient_single_attr])
        self.assertEqual(len(triage_scores), 1)
        self.assertEqual(triage_scores[0].score, 10)

    def test_multiple_attributes_single_patient(self):
        # Test case for a single patient with multiple attributes
        thresholds_multiple_attrs = {
            "gcs": MockThreshold(min_value=3, max_value=15),
            "sbp": MockThreshold(min_value=80, max_value=120),
            "rr": MockThreshold(min_value=12, max_value=25),
        }
        patient_multiple_attrs = MockPatient(name="Patient 1", gcs=10, sbp=100, rr=20)
        triage_algo_multiple_attrs = MockTriageFactory.create_triage_algo(
            algo_name="Multiple Attributes Single Patient", thresholds=thresholds_multiple_attrs
        )
        triage_scores = triage_algo_multiple_attrs.triage([patient_multiple_attrs])
        self.assertEqual(len(triage_scores), 1)
        self.assertEqual(triage_scores[0].score, 130)

    def test_no_common_thresholds(self):
        # Test case for patients with no common thresholds
        thresholds_no_common = {
            "temperature": MockThreshold(min_value=36, max_value=38),
            "heart_rate": MockThreshold(min_value=60, max_value=100),
            "respiratory_rate": MockThreshold(min_value=12, max_value=20),
        }
        patients_no_common = [
            MockPatient(name="Patient 1", temperature=37, heart_rate=80),
            MockPatient(name="Patient 2", respiratory_rate=18),
        ]
        triage_algo_no_common = MockTriageFactory.create_triage_algo(
            algo_name="No Common Thresholds", thresholds=thresholds_no_common
        )
        triage_scores = triage_algo_no_common.triage(patients_no_common)
        self.assertEqual(len(triage_scores), 2)
        self.assertEqual(triage_scores[0].score, 117)
        self.assertEqual(triage_scores[1].score, 18)

    def test_different_attributes_order(self):
        # Test case for patients with attributes in different order than thresholds
        thresholds_diff_order = {
            "gcs": MockThreshold(min_value=3, max_value=15),
            "sbp": MockThreshold(min_value=80, max_value=120),
            "rr": MockThreshold(min_value=12, max_value=25),
        }
        patient_diff_order = MockPatient(name="Patient 1", sbp=100, rr=20, gcs=10)
        triage_algo_diff_order = MockTriageFactory.create_triage_algo(
            algo_name="Different Order Attributes", thresholds=thresholds_diff_order
        )
        triage_scores = triage_algo_diff_order.triage([patient_diff_order])
        self.assertEqual(len(triage_scores), 1)
        self.assertEqual(triage_scores[0].score, 130)

    def test_multiple_patients_multiple_attributes(self):
        # Test case for multiple patients with multiple attributes
        thresholds_multiple_patients = {
            "gcs": MockThreshold(min_value=3, max_value=15),
            "sbp": MockThreshold(min_value=80, max_value=120),
            "rr": MockThreshold(min_value=12, max_value=25),
        }
        patients_multiple_patients = [
            MockPatient(name="Patient 1", gcs=10, sbp=100, rr=20),
            MockPatient(name="Patient 2", gcs=15, sbp=110, rr=25),
            MockPatient(name="Patient 3", gcs=5, sbp=90, rr=15),
        ]
        triage_algo_multiple_patients = MockTriageFactory.create_triage_algo(
            algo_name="Multiple Patients Multiple Attributes", thresholds=thresholds_multiple_patients
        )
        triage_scores = triage_algo_multiple_patients.triage(patients_multiple_patients)
        self.assertEqual(len(triage_scores), 3)
        self.assertEqual(triage_scores[0].score, 130)
        self.assertEqual(triage_scores[1].score, 150)
        self.assertEqual(triage_scores[2].score, 110)



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
    filename = "testing_report_triage_score.csv"
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
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPatientTriage)
    runner = CustomTestRunner()
    result = runner.run(suite)
    generate_csv_report(TestPatientTriage.test_timings, result.test_results)
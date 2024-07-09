    def test_patients_with_empty_values(self):
        # Test case for patients with some attributes having empty values
        patient_with_empty_values = MockPatient(
            name="Empty Value Patient", gcs=10, sbp=None, rr=30
        )
        triage_life_algo = MockTriageFactory.create_triage_algo(
            algo_name="LIFE", thresholds=self.thresholds_data_algo3
        )
        triage_scores = triage_life_algo.triage([patient_with_empty_values])
        self.assertEqual(len(triage_scores), 1)
        self.assertEqual(triage_scores[0].score, 40)  # Sum of gcs and rr
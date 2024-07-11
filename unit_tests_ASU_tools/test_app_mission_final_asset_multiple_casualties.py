import unittest
from datetime import datetime
import os
import csv
import sys
from typing import List

# Mock implementation for testing purposes

class MissionOptionsAssets:
    def __init__(self, patient_name, assets_possible, triage_score):
        self.patient_name = patient_name
        self.assets_possible = assets_possible
        self.triage_score = triage_score

    def __repr__(self):
        return f"MissionOptionsAssets(patient_name={self.patient_name}, assets_possible={self.assets_possible}, triage_score={self.triage_score})"

class MissionoptionsAssetsToMissionfinalAssetsAlgoName:
    BASIC = "BASIC"

class MissionoptionsAssetsToMissionfinalAssetsFactory:
    @staticmethod
    def create_missionoptionsAssets_to_missionfinalAssets_algo(mode):
        return MissionoptionsAssetsToMissionfinalAssetsAlgo()

class MissionoptionsAssetsToMissionfinalAssetsAlgo:
    def return_mission_final_asset(self, missions_options):
        return missions_options  # Mock implementation, just returning the input

# Unit tests

class TestMissionAssets(unittest.TestCase):
    def setUp(self):
        self.mission1 = MissionOptionsAssets(patient_name='Adrian Monk', assets_possible=['Black hawk HH60M', 'Chinook CH47', 'Chinook CH99', 'Truck M1165', 'Ambulance M997A3'], triage_score = 20)
        self.mission2 = MissionOptionsAssets(patient_name='Natalie Tieger', assets_possible=['Black hawk HH60M', 'Chinook CH47', 'Chinook CH99', 'Truck M1165'], triage_score = 10)
        self.mission3 = MissionOptionsAssets(patient_name='Leland Stottlemeyer', assets_possible=['Black hawk HH60M', 'Chinook CH47', 'Chinook CH99', 'Truck M1165'], triage_score = 20)
        self.mission4 = MissionOptionsAssets(patient_name='Jake Peralta', assets_possible=['Chinook CH99', 'Truck M1165', 'Ambulance M997A3'], triage_score = 30)
        self.mission5 = MissionOptionsAssets(patient_name='Sharona Fleming', assets_possible=['Chinook CH99', 'Truck M1165'], triage_score = 40)
        self.mission6 = MissionOptionsAssets(patient_name='Randy Disher', assets_possible=['Black hawk HH60M', 'Chinook CH47'], triage_score = 43)
        self.mission7 = MissionOptionsAssets(patient_name='Trudy Monk', assets_possible=['Chinook CH47', 'Chinook CH99'], triage_score = 13)
        self.mission8 = MissionOptionsAssets(patient_name='Charles Kroger', assets_possible=['Black hawk HH60M', 'Chinook CH47', 'Chinook CH99', 'Truck M1165', 'Ambulance M997A3'], triage_score = 95)
        self.mission9 = MissionOptionsAssets(patient_name='Julie Trieger', assets_possible=['Black hawk HH60M', 'Chinook CH47', 'Chinook CH99', 'Truck M1165', 'Ambulance M997A3'], triage_score = 84)
        self.mission10 = MissionOptionsAssets(patient_name='Benjy Fleming', assets_possible=['Black hawk HH60M', 'Chinook CH47', 'Chinook CH99', 'Truck M1165', 'Ambulance M997A3'], triage_score = 82)

        self.all_mission_options = [self.mission1, self.mission2, self.mission3, self.mission4, self.mission5, self.mission6, self.mission7, self.mission8, self.mission9, self.mission10]

    def test_mission_final_asset_assignment(self):
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=self.all_mission_options)
        self.assertEqual(len(assets_all_missions), len(self.all_mission_options))
        for mission_asset, original_mission in zip(assets_all_missions, self.all_mission_options):
            self.assertEqual(mission_asset, original_mission)

    def test_mode_advanced_return(self):
        # Test a different algorithm mode (ADVANCED)
        class AdvancedMissionoptionsAssetsAlgo:
            def return_mission_final_asset(self, missions_options):
                return missions_options[::-1]  # Reverse the list for testing purposes
        
        class AdvancedMissionoptionsAssetsToMissionfinalAssetsFactory:
            @staticmethod
            def create_missionoptionsAssets_to_missionfinalAssets_algo(mode):
                return AdvancedMissionoptionsAssetsAlgo()

        algo_mission_assets = AdvancedMissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode="ADVANCED")
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=self.all_mission_options)
        self.assertEqual(len(assets_all_missions), len(self.all_mission_options))
        self.assertEqual(assets_all_missions, self.all_mission_options[::-1])


    def test_mission_final_asset_assignment(self):
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=self.all_mission_options)
        self.assertEqual(len(assets_all_missions), len(self.all_mission_options))
        for mission_asset, original_mission in zip(assets_all_missions, self.all_mission_options):
            self.assertEqual(mission_asset.patient_name, original_mission.patient_name)
            self.assertEqual(mission_asset.assets_possible, original_mission.assets_possible)
            self.assertEqual(mission_asset.triage_score, original_mission.triage_score)

    def test_empty_mission_options(self):
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=[])
        self.assertEqual(len(assets_all_missions), 0)

    def test_duplicate_missions(self):
        duplicate_missions = [self.mission1, self.mission1, self.mission2, self.mission2]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=duplicate_missions)
        self.assertEqual(len(assets_all_missions), len(duplicate_missions))
        for mission_asset, original_mission in zip(assets_all_missions, duplicate_missions):
            self.assertEqual(mission_asset.patient_name, original_mission.patient_name)
            self.assertEqual(mission_asset.assets_possible, original_mission.assets_possible)
            self.assertEqual(mission_asset.triage_score, original_mission.triage_score)

    def test_single_asset_mission(self):
        single_asset_mission = MissionOptionsAssets(patient_name='Solo Asset', assets_possible=['Truck M1165'], triage_score=50)
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=[single_asset_mission])
        self.assertEqual(len(assets_all_missions), 1)
        self.assertEqual(assets_all_missions[0].patient_name, single_asset_mission.patient_name)
        self.assertEqual(assets_all_missions[0].assets_possible, single_asset_mission.assets_possible)
        self.assertEqual(assets_all_missions[0].triage_score, single_asset_mission.triage_score)

    def test_same_triage_score_order(self):
        same_score_missions = [self.mission1, self.mission3, self.mission2]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=same_score_missions)
        self.assertEqual(len(assets_all_missions), len(same_score_missions))
        for mission_asset, original_mission in zip(assets_all_missions, same_score_missions):
            self.assertEqual(mission_asset.patient_name, original_mission.patient_name)
            self.assertEqual(mission_asset.assets_possible, original_mission.assets_possible)
            self.assertEqual(mission_asset.triage_score, original_mission.triage_score)

    def test_no_assets_possible(self):
        no_assets_mission = MissionOptionsAssets(patient_name='No Assets', assets_possible=[], triage_score=50)
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=[no_assets_mission])
        self.assertEqual(len(assets_all_missions), 1)
        self.assertEqual(assets_all_missions[0].patient_name, no_assets_mission.patient_name)
        self.assertEqual(assets_all_missions[0].assets_possible, no_assets_mission.assets_possible)
        self.assertEqual(assets_all_missions[0].triage_score, no_assets_mission.triage_score)

    def test_negative_triage_scores(self):
        negative_triage_mission1 = MissionOptionsAssets(patient_name='Negative Score 1', assets_possible=['Truck M1165'], triage_score=-10)
        negative_triage_mission2 = MissionOptionsAssets(patient_name='Negative Score 2', assets_possible=['Ambulance M997A3'], triage_score=-20)
        missions_with_negative_scores = [negative_triage_mission1, negative_triage_mission2]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=missions_with_negative_scores)
        self.assertEqual(len(assets_all_missions), len(missions_with_negative_scores))
        for mission_asset, original_mission in zip(assets_all_missions, missions_with_negative_scores):
            self.assertEqual(mission_asset.patient_name, original_mission.patient_name)
            self.assertEqual(mission_asset.assets_possible, original_mission.assets_possible)
            self.assertEqual(mission_asset.triage_score, original_mission.triage_score)

    def test_same_assets_possible(self):
        same_assets_mission1 = MissionOptionsAssets(patient_name='Same Assets 1', assets_possible=['Black hawk HH60M', 'Chinook CH47'], triage_score=10)
        same_assets_mission2 = MissionOptionsAssets(patient_name='Same Assets 2', assets_possible=['Black hawk HH60M', 'Chinook CH47'], triage_score=20)
        missions_with_same_assets = [same_assets_mission1, same_assets_mission2]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=missions_with_same_assets)
        self.assertEqual(len(assets_all_missions), len(missions_with_same_assets))
        for mission_asset, original_mission in zip(assets_all_missions, missions_with_same_assets):
            self.assertEqual(mission_asset.patient_name, original_mission.patient_name)
            self.assertEqual(mission_asset.assets_possible, original_mission.assets_possible)
            self.assertEqual(mission_asset.triage_score, original_mission.triage_score)

    def test_varying_assets_length(self):
        short_assets_mission = MissionOptionsAssets(patient_name='Short Assets', assets_possible=['Truck M1165'], triage_score=50)
        long_assets_mission = MissionOptionsAssets(patient_name='Long Assets', assets_possible=['Black hawk HH60M', 'Chinook CH47', 'Chinook CH99', 'Truck M1165', 'Ambulance M997A3'], triage_score=30)
        missions_with_varying_assets_length = [short_assets_mission, long_assets_mission]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=missions_with_varying_assets_length)
        self.assertEqual(len(assets_all_missions), len(missions_with_varying_assets_length))
        for mission_asset, original_mission in zip(assets_all_missions, missions_with_varying_assets_length):
            self.assertEqual(mission_asset.patient_name, original_mission.patient_name)
            self.assertEqual(mission_asset.assets_possible, original_mission.assets_possible)
            self.assertEqual(mission_asset.triage_score, original_mission.triage_score)

    def test_all_same_triage_score(self):
        # All missions have the same triage score
        same_score_mission1 = MissionOptionsAssets(patient_name='Patient 1', assets_possible=['Truck M1165'], triage_score=50)
        same_score_mission2 = MissionOptionsAssets(patient_name='Patient 2', assets_possible=['Ambulance M997A3'], triage_score=50)
        missions_with_same_scores = [same_score_mission1, same_score_mission2]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=missions_with_same_scores)
        self.assertEqual(len(assets_all_missions), len(missions_with_same_scores))
        for mission_asset, original_mission in zip(assets_all_missions, missions_with_same_scores):
            self.assertEqual(mission_asset.patient_name, original_mission.patient_name)
            self.assertEqual(mission_asset.assets_possible, original_mission.assets_possible)
            self.assertEqual(mission_asset.triage_score, original_mission.triage_score)

    def test_empty_patient_name(self):
        # Test mission with an empty patient name
        empty_name_mission = MissionOptionsAssets(patient_name='', assets_possible=['Truck M1165'], triage_score=30)
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=[empty_name_mission])
        self.assertEqual(len(assets_all_missions), 1)
        self.assertEqual(assets_all_missions[0].patient_name, empty_name_mission.patient_name)
        self.assertEqual(assets_all_missions[0].assets_possible, empty_name_mission.assets_possible)
        self.assertEqual(assets_all_missions[0].triage_score, empty_name_mission.triage_score)

    def test_large_number_of_missions(self):
        # Test with a large number of mission options
        large_number_of_missions = [MissionOptionsAssets(patient_name=f'Patient {i}', assets_possible=['Truck M1165'], triage_score=i) for i in range(1000)]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=large_number_of_missions)
        self.assertEqual(len(assets_all_missions), len(large_number_of_missions))
        for mission_asset, original_mission in zip(assets_all_missions, large_number_of_missions):
            self.assertEqual(mission_asset.patient_name, original_mission.patient_name)
            self.assertEqual(mission_asset.assets_possible, original_mission.assets_possible)
            self.assertEqual(mission_asset.triage_score, original_mission.triage_score)

    def test_mixed_triage_scores(self):
        # Test with a mix of positive, negative, and zero triage scores
        mixed_triage_mission1 = MissionOptionsAssets(patient_name='Positive Score', assets_possible=['Truck M1165'], triage_score=30)
        mixed_triage_mission2 = MissionOptionsAssets(patient_name='Negative Score', assets_possible=['Ambulance M997A3'], triage_score=-10)
        mixed_triage_mission3 = MissionOptionsAssets(patient_name='Zero Score', assets_possible=['Chinook CH47'], triage_score=0)
        missions_with_mixed_triage_scores = [mixed_triage_mission1, mixed_triage_mission2, mixed_triage_mission3]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=missions_with_mixed_triage_scores)
        self.assertEqual(len(assets_all_missions), len(missions_with_mixed_triage_scores))
        for mission_asset, original_mission in zip(assets_all_missions, missions_with_mixed_triage_scores):
            self.assertEqual(mission_asset.patient_name, original_mission.patient_name)
            self.assertEqual(mission_asset.assets_possible, original_mission.assets_possible)
            self.assertEqual(mission_asset.triage_score, original_mission.triage_score)

    def test_duplicate_patient_names(self):
        # Test with duplicate patient names but different assets and scores
        duplicate_name_mission1 = MissionOptionsAssets(patient_name='Duplicate Name', assets_possible=['Truck M1165'], triage_score=20)
        duplicate_name_mission2 = MissionOptionsAssets(patient_name='Duplicate Name', assets_possible=['Ambulance M997A3'], triage_score=40)
        missions_with_duplicate_names = [duplicate_name_mission1, duplicate_name_mission2]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=missions_with_duplicate_names)
        self.assertEqual(len(assets_all_missions), len(missions_with_duplicate_names))
        for mission_asset, original_mission in zip(assets_all_missions, missions_with_duplicate_names):
            self.assertEqual(mission_asset.patient_name, original_mission.patient_name)
            self.assertEqual(mission_asset.assets_possible, original_mission.assets_possible)
            self.assertEqual(mission_asset.triage_score, original_mission.triage_score)

    def test_all_zero_triage_scores(self):
        # Test with all missions having zero triage scores
        zero_score_mission1 = MissionOptionsAssets(patient_name='Zero Score 1', assets_possible=['Truck M1165'], triage_score=0)
        zero_score_mission2 = MissionOptionsAssets(patient_name='Zero Score 2', assets_possible=['Ambulance M997A3'], triage_score=0)
        missions_with_zero_scores = [zero_score_mission1, zero_score_mission2]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=missions_with_zero_scores)
        self.assertEqual(len(assets_all_missions), len(missions_with_zero_scores))
        for mission_asset, original_mission in zip(assets_all_missions, missions_with_zero_scores):
            self.assertEqual(mission_asset.patient_name, original_mission.patient_name)
            self.assertEqual(mission_asset.assets_possible, original_mission.assets_possible)
            self.assertEqual(mission_asset.triage_score, original_mission.triage_score)

    def test_empty_assets_possible_list(self):
        # Test with empty assets possible list
        empty_assets_mission = MissionOptionsAssets(patient_name='Empty Assets', assets_possible=[], triage_score=50)
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=[empty_assets_mission])
        self.assertEqual(len(assets_all_missions), 1)
        self.assertEqual(assets_all_missions[0].assets_possible, [])


    def test_duplicate_mission_entries(self):
        # Test with duplicate mission entries
        duplicate_mission = MissionOptionsAssets(patient_name='Duplicate', assets_possible=['Truck M1165'], triage_score=50)
        missions_with_duplicates = [duplicate_mission, duplicate_mission]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=missions_with_duplicates)
        self.assertEqual(len(assets_all_missions), 2)
        self.assertEqual(assets_all_missions[0], assets_all_missions[1])


    def test_large_triage_scores(self):
        # Test with very large triage scores
        large_score_mission1 = MissionOptionsAssets(patient_name='Large Score 1', assets_possible=['Truck M1165'], triage_score=9999999)
        large_score_mission2 = MissionOptionsAssets(patient_name='Large Score 2', assets_possible=['Ambulance M997A3'], triage_score=8888888)
        missions_with_large_scores = [large_score_mission1, large_score_mission2]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=missions_with_large_scores)
        self.assertEqual(len(assets_all_missions), len(missions_with_large_scores))
        for mission_asset, original_mission in zip(assets_all_missions, missions_with_large_scores):
            self.assertEqual(mission_asset.triage_score, original_mission.triage_score)

    def test_zero_and_negative_triage_scores(self):
        # Test with zero and negative triage scores
        zero_score_mission = MissionOptionsAssets(patient_name='Zero Score', assets_possible=['Truck M1165'], triage_score=0)
        negative_score_mission = MissionOptionsAssets(patient_name='Negative Score', assets_possible=['Ambulance M997A3'], triage_score=-5)
        missions_with_zero_and_negative_scores = [zero_score_mission, negative_score_mission]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=missions_with_zero_and_negative_scores)
        self.assertEqual(len(assets_all_missions), len(missions_with_zero_and_negative_scores))
        for mission_asset, original_mission in zip(assets_all_missions, missions_with_zero_and_negative_scores):
            self.assertEqual(mission_asset.triage_score, original_mission.triage_score)

    def test_empty_mission_list(self):
        # Test with an empty list of missions
        empty_mission_list = []
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=empty_mission_list)
        self.assertEqual(len(assets_all_missions), 0)

    def test_single_mission(self):
        # Test with a single mission
        single_mission = [MissionOptionsAssets(patient_name='Single Mission', assets_possible=['Black hawk HH60M'], triage_score=50)]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=single_mission)
        self.assertEqual(len(assets_all_missions), 1)
        self.assertEqual(assets_all_missions[0], single_mission[0])

    def test_identical_triage_scores(self):
        # Test with multiple missions having identical triage scores
        identical_triage_missions = [
            MissionOptionsAssets(patient_name='Patient 1', assets_possible=['Black hawk HH60M'], triage_score=30),
            MissionOptionsAssets(patient_name='Patient 2', assets_possible=['Chinook CH47'], triage_score=30),
            MissionOptionsAssets(patient_name='Patient 3', assets_possible=['Ambulance M997A3'], triage_score=30)
        ]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=identical_triage_missions)
        self.assertEqual(len(assets_all_missions), len(identical_triage_missions))
        for mission_asset, original_mission in zip(assets_all_missions, identical_triage_missions):
            self.assertEqual(mission_asset.triage_score, original_mission.triage_score)

    def test_unusual_characters_in_patient_name(self):
        # Test with unusual characters in patient names
        unusual_characters_missions = [
            MissionOptionsAssets(patient_name='Patient_!@#$', assets_possible=['Black hawk HH60M'], triage_score=20),
            MissionOptionsAssets(patient_name='Patient_%^&*', assets_possible=['Chinook CH47'], triage_score=30)
        ]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=unusual_characters_missions)
        self.assertEqual(len(assets_all_missions), len(unusual_characters_missions))
        for mission_asset, original_mission in zip(assets_all_missions, unusual_characters_missions):
            self.assertEqual(mission_asset.patient_name, original_mission.patient_name)

    def test_assets_possible_with_duplicates(self):
        # Test with assets_possible containing duplicate entries
        duplicate_assets_mission = MissionOptionsAssets(patient_name='Duplicate Assets', assets_possible=['Black hawk HH60M', 'Black hawk HH60M'], triage_score=50)
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=[duplicate_assets_mission])
        self.assertEqual(len(assets_all_missions), 1)
        self.assertEqual(assets_all_missions[0].assets_possible, ['Black hawk HH60M', 'Black hawk HH60M'])

    def test_all_assets_assigned(self):
        # Ensure all missions have at least one asset assigned
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=self.all_mission_options)
        for mission_asset in assets_all_missions:
            self.assertGreater(len(mission_asset.assets_possible), 0)

    def test_mission_with_special_characters(self):
        # Test missions with special characters in patient names
        special_character_mission = MissionOptionsAssets(patient_name='患者-测试', assets_possible=['Chinook CH47'], triage_score=50)
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=[special_character_mission])
        self.assertEqual(assets_all_missions[0].patient_name, '患者-测试')

    def test_mission_with_long_patient_name(self):
        # Test missions with an unusually long patient name
        long_name_mission = MissionOptionsAssets(patient_name='A' * 1000, assets_possible=['Ambulance M997A3'], triage_score=20)
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=[long_name_mission])
        self.assertEqual(assets_all_missions[0].patient_name, 'A' * 1000)

    def test_mission_with_empty_patient_name(self):
        # Test missions with an empty patient name
        empty_name_mission = MissionOptionsAssets(patient_name='', assets_possible=['Chinook CH47'], triage_score=30)
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=[empty_name_mission])
        self.assertEqual(assets_all_missions[0].patient_name, '')

    def test_assets_assignment_consistency(self):
        # Test if assets assignment remains consistent over multiple calls
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        first_assignment = algo_mission_assets.return_mission_final_asset(missions_options=self.all_mission_options)
        second_assignment = algo_mission_assets.return_mission_final_asset(missions_options=self.all_mission_options)
        self.assertEqual(first_assignment, second_assignment)

    def test_mission_with_invalid_assets(self):
        # Test missions with invalid asset names
        invalid_assets_mission = MissionOptionsAssets(patient_name='Invalid Assets', assets_possible=['Invalid Asset 1', 'Invalid Asset 2'], triage_score=15)
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=[invalid_assets_mission])
        self.assertEqual(assets_all_missions[0].assets_possible, ['Invalid Asset 1', 'Invalid Asset 2'])

    def test_extreme_triage_score_values(self):
        # Test missions with extremely high or low triage scores
        extreme_triage_missions = [
            MissionOptionsAssets(patient_name='Low Triage', assets_possible=['Ambulance M997A3'], triage_score=-9999),
            MissionOptionsAssets(patient_name='High Triage', assets_possible=['Chinook CH47'], triage_score=9999)
        ]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=extreme_triage_missions)
        self.assertEqual(assets_all_missions[0].triage_score, -9999)
        self.assertEqual(assets_all_missions[1].triage_score, 9999)

    def test_empty_mission_options_list(self):
        # Test with an empty list of mission options
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=[])
        self.assertEqual(assets_all_missions, [])

    def test_single_mission_option(self):
        # Test with a single mission option
        single_mission = [MissionOptionsAssets(patient_name='Single Patient', assets_possible=['Ambulance M997A3'], triage_score=50)]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=single_mission)
        self.assertEqual(len(assets_all_missions), 1)
        self.assertEqual(assets_all_missions[0].patient_name, 'Single Patient')

    def test_mission_with_duplicate_names(self):
        # Test missions with duplicate patient names
        duplicate_name_mission1 = MissionOptionsAssets(patient_name='Duplicate Name', assets_possible=['Chinook CH47'], triage_score=20)
        duplicate_name_mission2 = MissionOptionsAssets(patient_name='Duplicate Name', assets_possible=['Ambulance M997A3'], triage_score=40)
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=[duplicate_name_mission1, duplicate_name_mission2])
        self.assertEqual(len(assets_all_missions), 2)
        self.assertEqual(assets_all_missions[0].patient_name, 'Duplicate Name')
        self.assertEqual(assets_all_missions[1].patient_name, 'Duplicate Name')

    def test_return_type_is_list(self):
        # Ensure the return type is a list
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=self.all_mission_options)
        self.assertIsInstance(assets_all_missions, list)

    def test_all_assets_assigned_to_each_mission(self):
        # Test to ensure all possible assets are assigned to each mission
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=self.all_mission_options)
        for mission_asset, original_mission in zip(assets_all_missions, self.all_mission_options):
            self.assertEqual(set(mission_asset.assets_possible), set(original_mission.assets_possible))

    def test_triage_score_unaffected(self):
        # Ensure that the triage score remains unaffected after processing
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=self.all_mission_options)
        for mission_asset, original_mission in zip(assets_all_missions, self.all_mission_options):
            self.assertEqual(mission_asset.triage_score, original_mission.triage_score)

    def test_return_order_same_as_input(self):
        # Ensure the return order is the same as the input order
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=self.all_mission_options)
        self.assertEqual(assets_all_missions, self.all_mission_options)

    def test_no_side_effects_on_input(self):
        # Ensure the input list is not modified
        original_missions_copy = self.all_mission_options[:]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        _ = algo_mission_assets.return_mission_final_asset(missions_options=self.all_mission_options)
        self.assertEqual(self.all_mission_options, original_missions_copy)

    def test_handling_of_large_asset_lists(self):
        # Test handling of missions with very large asset lists
        large_assets_mission = MissionOptionsAssets(patient_name='Large Assets', assets_possible=['Asset ' + str(i) for i in range(1000)], triage_score=25)
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=[large_assets_mission])
        self.assertEqual(len(assets_all_missions[0].assets_possible), 1000)

    def test_no_missions_provided(self):
        # Test when no missions are provided
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=[])
        self.assertEqual(assets_all_missions, [])

    def test_single_mission_one_asset(self):
        # Test with a single mission having only one asset
        single_asset_mission = [MissionOptionsAssets(patient_name='Single Asset Patient', assets_possible=['Ambulance M997A3'], triage_score=30)]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=single_asset_mission)
        self.assertEqual(len(assets_all_missions), 1)
        self.assertEqual(assets_all_missions[0].assets_possible, ['Ambulance M997A3'])

    def test_mission_with_empty_assets(self):
        # Test a mission with an empty list of possible assets
        empty_assets_mission = [MissionOptionsAssets(patient_name='Empty Assets Patient', assets_possible=[], triage_score=15)]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=empty_assets_mission)
        self.assertEqual(len(assets_all_missions), 1)
        self.assertEqual(assets_all_missions[0].assets_possible, [])

    def test_mission_with_same_asset_multiple_times(self):
        # Test a mission with the same asset listed multiple times
        repeated_asset_mission = [MissionOptionsAssets(patient_name='Repeated Assets Patient', assets_possible=['Ambulance M997A3', 'Ambulance M997A3'], triage_score=25)]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=repeated_asset_mission)
        self.assertEqual(len(assets_all_missions), 1)
        self.assertEqual(assets_all_missions[0].assets_possible, ['Ambulance M997A3', 'Ambulance M997A3'])

    def test_multiple_missions_same_patient_name(self):
        # Test multiple missions with the same patient name
        same_patient_missions = [
            MissionOptionsAssets(patient_name='Adrian Monk', assets_possible=['Black hawk HH60M', 'Chinook CH47'], triage_score=20),
            MissionOptionsAssets(patient_name='Adrian Monk', assets_possible=['Chinook CH99', 'Truck M1165'], triage_score=30)
        ]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=same_patient_missions)
        self.assertEqual(len(assets_all_missions), 2)
        self.assertEqual(assets_all_missions[0].patient_name, 'Adrian Monk')
        self.assertEqual(assets_all_missions[1].patient_name, 'Adrian Monk')

    def test_mission_with_same_triage_score(self):
        # Test missions with the same triage score
        same_triage_score_missions = [
            MissionOptionsAssets(patient_name='Patient 1', assets_possible=['Ambulance M997A3'], triage_score=25),
            MissionOptionsAssets(patient_name='Patient 2', assets_possible=['Truck M1165'], triage_score=25)
        ]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=same_triage_score_missions)
        self.assertEqual(len(assets_all_missions), 2)
        self.assertEqual(assets_all_missions[0].triage_score, 25)
        self.assertEqual(assets_all_missions[1].triage_score, 25) 

    def test_empty_missions_list(self):
        # Test when an empty list of missions is provided
        empty_missions = []
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=empty_missions)
        self.assertEqual(assets_all_missions, [])

    def test_large_number_of_missions(self):
        # Test with a large number of missions
        large_number_missions = [MissionOptionsAssets(patient_name=f'Patient {i}', assets_possible=['Ambulance M997A3', 'Truck M1165'], triage_score=i) for i in range(1000)]
        algo_mission_assets = MissionoptionsAssetsToMissionfinalAssetsFactory.create_missionoptionsAssets_to_missionfinalAssets_algo(mode=MissionoptionsAssetsToMissionfinalAssetsAlgoName.BASIC)
        assets_all_missions = algo_mission_assets.return_mission_final_asset(missions_options=large_number_missions)
        self.assertEqual(len(assets_all_missions), 1000)



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
    filename = "testing_report_mission_final_asset.csv"
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
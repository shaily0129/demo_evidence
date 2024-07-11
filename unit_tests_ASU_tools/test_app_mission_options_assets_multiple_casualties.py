import unittest
from datetime import datetime
import os
import csv
import sys
from typing import List

class MissionRequirements:
    def __init__(self, name, medevac_needed, evac_needed, resupply_needed, require_vtol, require_ctol, require_ground_vehicle,
                 litters_spaces_required, ambulatory_spaces_required, weather_condition, day_mission, night_mission, require_iv_provisions,
                 require_medical_monitoring_system, require_life_support_equipment, require_oxygen_generation_system, require_patient_litter_lift_system):
        self.name = name
        self.medevac_needed = medevac_needed
        self.evac_needed = evac_needed
        self.resupply_needed = resupply_needed
        self.require_vtol = require_vtol
        self.require_ctol = require_ctol
        self.require_ground_vehicle = require_ground_vehicle
        self.litters_spaces_required = litters_spaces_required
        self.ambulatory_spaces_required = ambulatory_spaces_required
        self.weather_condition = weather_condition
        self.day_mission = day_mission
        self.night_mission = night_mission
        self.require_iv_provisions = require_iv_provisions
        self.require_medical_monitoring_system = require_medical_monitoring_system
        self.require_life_support_equipment = require_life_support_equipment
        self.require_oxygen_generation_system = require_oxygen_generation_system
        self.require_patient_litter_lift_system = require_patient_litter_lift_system

class TestMissionRequirements(unittest.TestCase):
    
    def test_mission_creation(self):
        mission = MissionRequirements(
            name='Adrian Monk',
            medevac_needed=True,
            evac_needed=False,
            resupply_needed=False,
            require_vtol=True,
            require_ctol=False,
            require_ground_vehicle=False,
            litters_spaces_required=2,
            ambulatory_spaces_required=3,
            weather_condition='clear',
            day_mission=True,
            night_mission=False,
            require_iv_provisions=False,
            require_medical_monitoring_system=False,
            require_life_support_equipment=False,
            require_oxygen_generation_system=False,
            require_patient_litter_lift_system=False
        )
        
        self.assertEqual(mission.name, 'Adrian Monk')
        self.assertTrue(mission.medevac_needed)
        self.assertFalse(mission.evac_needed)
        self.assertTrue(mission.require_vtol)
        self.assertEqual(mission.litters_spaces_required, 2)
        self.assertEqual(mission.weather_condition, 'clear')

class Asset:
    def __init__(self, asset_name, asset_type, asset_status, asset_mission_type, crew, litter_capacity,
                 ambulatory_capacity, operational_day, operational_night, operational_adverse_weather, has_iv_provisions,
                 has_medical_monitoring_system, has_life_support_equipment, has_oxygen_generation_system, has_patient_litter_lift_system):
        self.asset_name = asset_name
        self.asset_type = asset_type
        self.asset_status = asset_status
        self.asset_mission_type = asset_mission_type
        self.crew = crew
        self.litter_capacity = litter_capacity
        self.ambulatory_capacity = ambulatory_capacity
        self.operational_day = operational_day
        self.operational_night = operational_night
        self.operational_adverse_weather = operational_adverse_weather
        self.has_iv_provisions = has_iv_provisions
        self.has_medical_monitoring_system = has_medical_monitoring_system
        self.has_life_support_equipment = has_life_support_equipment
        self.has_oxygen_generation_system = has_oxygen_generation_system
        self.has_patient_litter_lift_system = has_patient_litter_lift_system

class TestAsset(unittest.TestCase):

    def test_asset_creation(self):
        asset = Asset(
            asset_name='Black hawk HH60M',
            asset_type='vtol',
            asset_status='available',
            asset_mission_type='medevac',
            crew=['pilot', 'copilot', 'crew_chief', 'medic_1'],
            litter_capacity=6,
            ambulatory_capacity=6,
            operational_day=True,
            operational_night=True,
            operational_adverse_weather=True,
            has_iv_provisions=True,
            has_medical_monitoring_system=True,
            has_life_support_equipment=True,
            has_oxygen_generation_system=True,
            has_patient_litter_lift_system=True
        )
        
        self.assertEqual(asset.asset_name, 'Black hawk HH60M')
        self.assertEqual(asset.asset_type, 'vtol')
        self.assertEqual(asset.asset_status, 'available')
        self.assertEqual(asset.crew, ['pilot', 'copilot', 'crew_chief', 'medic_1'])
        self.assertTrue(asset.operational_night)
        self.assertTrue(asset.has_iv_provisions)

    def test_asset_operational_status(self):
        asset = Asset(
            asset_name='Ambulance M997A3',
            asset_type='ground',
            asset_status='available',
            asset_mission_type='medevac',
            crew=['driver', 'medic_1', 'crew_chief'],
            litter_capacity=4,
            ambulatory_capacity=4,
            operational_day=True,
            operational_night=True,
            operational_adverse_weather=False,
            has_iv_provisions=True,
            has_medical_monitoring_system=True,
            has_life_support_equipment=True,
            has_oxygen_generation_system=True,
            has_patient_litter_lift_system=True
        )
        
        self.assertTrue(asset.operational_day)
        self.assertTrue(asset.operational_night)
        self.assertFalse(asset.operational_adverse_weather)

    def test_mission_with_asset_compatibility(self):
        mission = MissionRequirements(
            name='Jake Peralta',
            medevac_needed=True,
            evac_needed=False,
            resupply_needed=False,
            require_vtol=True,
            require_ctol=False,
            require_ground_vehicle=False,
            litters_spaces_required=1,
            ambulatory_spaces_required=0,
            weather_condition='clear',
            day_mission=True,
            night_mission=True,
            require_iv_provisions=True,
            require_medical_monitoring_system=True,
            require_life_support_equipment=False,
            require_oxygen_generation_system=False,
            require_patient_litter_lift_system=True
        )
        
        asset = Asset(
            asset_name='Chinook CH47',
            asset_type='vtol',
            asset_status='available',
            asset_mission_type='medevac',
            crew=['pilot', 'copilot', 'crew_chief', 'medic_1'],
            litter_capacity=24,
            ambulatory_capacity=24,
            operational_day=True,
            operational_night=True,
            operational_adverse_weather=True,
            has_iv_provisions=True,
            has_medical_monitoring_system=True,
            has_life_support_equipment=True,
            has_oxygen_generation_system=True,
            has_patient_litter_lift_system=True
        )
        
        self.assertTrue(asset.asset_type == 'vtol' and mission.require_vtol)
        self.assertTrue(asset.operational_day and mission.day_mission)
        self.assertTrue(asset.operational_night and mission.night_mission)
        self.assertTrue(asset.has_iv_provisions and mission.require_iv_provisions)
        self.assertTrue(asset.has_medical_monitoring_system and mission.require_medical_monitoring_system)
        self.assertTrue(asset.has_patient_litter_lift_system and mission.require_patient_litter_lift_system)

class TestMissionRequirementsAdditional(unittest.TestCase):

    def test_default_values(self):
        mission = MissionRequirements(
            name='Default Test',
            medevac_needed=False,
            evac_needed=False,
            resupply_needed=False,
            require_vtol=False,
            require_ctol=False,
            require_ground_vehicle=False,
            litters_spaces_required=0,
            ambulatory_spaces_required=0,
            weather_condition='clear',
            day_mission=False,
            night_mission=False,
            require_iv_provisions=False,
            require_medical_monitoring_system=False,
            require_life_support_equipment=False,
            require_oxygen_generation_system=False,
            require_patient_litter_lift_system=False
        )

        self.assertFalse(mission.medevac_needed)
        self.assertFalse(mission.evac_needed)
        self.assertFalse(mission.resupply_needed)
        self.assertFalse(mission.require_vtol)
        self.assertEqual(mission.litters_spaces_required, 0)
        self.assertFalse(mission.day_mission)
        self.assertFalse(mission.night_mission)

    def test_mission_edge_cases(self):
        mission = MissionRequirements(
            name='Edge Case Test',
            medevac_needed=True,
            evac_needed=True,
            resupply_needed=True,
            require_vtol=True,
            require_ctol=True,
            require_ground_vehicle=True,
            litters_spaces_required=100,
            ambulatory_spaces_required=100,
            weather_condition='extreme',
            day_mission=True,
            night_mission=True,
            require_iv_provisions=True,
            require_medical_monitoring_system=True,
            require_life_support_equipment=True,
            require_oxygen_generation_system=True,
            require_patient_litter_lift_system=True
        )

        self.assertTrue(mission.medevac_needed)
        self.assertTrue(mission.evac_needed)
        self.assertTrue(mission.resupply_needed)
        self.assertTrue(mission.require_vtol)
        self.assertTrue(mission.require_ctol)
        self.assertTrue(mission.require_ground_vehicle)
        self.assertEqual(mission.litters_spaces_required, 100)
        self.assertEqual(mission.weather_condition, 'extreme')
        self.assertTrue(mission.day_mission)
        self.assertTrue(mission.night_mission)

class TestAssetAdditional7(unittest.TestCase):

    def test_asset_edge_cases(self):
        asset = Asset(
            asset_name='Edge Case Asset',
            asset_type='ctol',
            asset_status='unavailable',
            asset_mission_type='resupply',
            crew=[],
            litter_capacity=0,
            ambulatory_capacity=0,
            operational_day=False,
            operational_night=False,
            operational_adverse_weather=False,
            has_iv_provisions=False,
            has_medical_monitoring_system=False,
            has_life_support_equipment=False,
            has_oxygen_generation_system=False,
            has_patient_litter_lift_system=False
        )

        self.assertEqual(asset.asset_name, 'Edge Case Asset')
        self.assertEqual(asset.asset_status, 'unavailable')
        self.assertEqual(asset.crew, [])
        self.assertFalse(asset.operational_day)
        self.assertFalse(asset.operational_night)
        self.assertFalse(asset.operational_adverse_weather)

    def test_asset_large_crew(self):
        asset = Asset(
            asset_name='Large Crew Asset',
            asset_type='vtol',
            asset_status='available',
            asset_mission_type='evac',
            crew=['pilot', 'copilot', 'crew_chief', 'medic_1', 'medic_2', 'medic_3', 'medic_4', 'medic_5'],
            litter_capacity=2,
            ambulatory_capacity=4,
            operational_day=True,
            operational_night=True,
            operational_adverse_weather=True,
            has_iv_provisions=True,
            has_medical_monitoring_system=True,
            has_life_support_equipment=True,
            has_oxygen_generation_system=True,
            has_patient_litter_lift_system=True
        )

        self.assertEqual(len(asset.crew), 8)
        self.assertEqual(asset.crew[0], 'pilot')
        self.assertEqual(asset.crew[-1], 'medic_5')
        self.assertTrue(asset.has_iv_provisions)

class TestMissionRequirementsAdditional2(unittest.TestCase):

    def test_missing_values(self):
        with self.assertRaises(TypeError):
            MissionRequirements()


class TestAssetAdditional6(unittest.TestCase):

    def test_asset_mission_type(self):
        asset = Asset(
            asset_name='Mission Type Test',
            asset_type='vtol',
            asset_status='available',
            asset_mission_type='unknown',  # invalid mission type
            crew=['pilot'],
            litter_capacity=1,
            ambulatory_capacity=1,
            operational_day=True,
            operational_night=True,
            operational_adverse_weather=True,
            has_iv_provisions=True,
            has_medical_monitoring_system=True,
            has_life_support_equipment=True,
            has_oxygen_generation_system=True,
            has_patient_litter_lift_system=True
        )

        self.assertNotIn(asset.asset_mission_type, ['medevac', 'evac', 'resupply'])

    def test_asset_empty_crew(self):
        asset = Asset(
            asset_name='Empty Crew Test',
            asset_type='ground',
            asset_status='available',
            asset_mission_type='evac',
            crew=[],  # empty crew
            litter_capacity=0,
            ambulatory_capacity=10,
            operational_day=True,
            operational_night=False,
            operational_adverse_weather=True,
            has_iv_provisions=False,
            has_medical_monitoring_system=False,
            has_life_support_equipment=False,
            has_oxygen_generation_system=False,
            has_patient_litter_lift_system=False
        )

        self.assertEqual(asset.crew, [])
        self.assertEqual(asset.ambulatory_capacity, 10)

class TestMissionRequirementsAdditional3(unittest.TestCase):

    def test_mission_name(self):
        mission = MissionRequirements(
            name='Test Mission Name',
            medevac_needed=True,
            evac_needed=False,
            resupply_needed=False,
            require_vtol=True,
            require_ctol=False,
            require_ground_vehicle=False,
            litters_spaces_required=1,
            ambulatory_spaces_required=1,
            weather_condition='clear',
            day_mission=True,
            night_mission=False,
            require_iv_provisions=False,
            require_medical_monitoring_system=False,
            require_life_support_equipment=False,
            require_oxygen_generation_system=False,
            require_patient_litter_lift_system=False
        )

        self.assertEqual(mission.name, 'Test Mission Name')

    def test_mission_day_night(self):
        mission = MissionRequirements(
            name='Day and Night Mission',
            medevac_needed=False,
            evac_needed=False,
            resupply_needed=False,
            require_vtol=False,
            require_ctol=False,
            require_ground_vehicle=False,
            litters_spaces_required=0,
            ambulatory_spaces_required=0,
            weather_condition='clear',
            day_mission=True,
            night_mission=True,
            require_iv_provisions=False,
            require_medical_monitoring_system=False,
            require_life_support_equipment=False,
            require_oxygen_generation_system=False,
            require_patient_litter_lift_system=False
        )

        self.assertTrue(mission.day_mission)
        self.assertTrue(mission.night_mission)

class TestAssetAdditional5(unittest.TestCase):

    def test_asset_name(self):
        asset = Asset(
            asset_name='Test Asset Name',
            asset_type='vtol',
            asset_status='available',
            asset_mission_type='medevac',
            crew=['pilot', 'copilot'],
            litter_capacity=2,
            ambulatory_capacity=4,
            operational_day=True,
            operational_night=True,
            operational_adverse_weather=True,
            has_iv_provisions=True,
            has_medical_monitoring_system=True,
            has_life_support_equipment=True,
            has_oxygen_generation_system=True,
            has_patient_litter_lift_system=True
        )

        self.assertEqual(asset.asset_name, 'Test Asset Name')

    def test_asset_ambulatory_capacity(self):
        asset = Asset(
            asset_name='Ambulatory Capacity Test',
            asset_type='ground',
            asset_status='available',
            asset_mission_type='evac',
            crew=['driver'],
            litter_capacity=0,
            ambulatory_capacity=15,
            operational_day=True,
            operational_night=False,
            operational_adverse_weather=False,
            has_iv_provisions=False,
            has_medical_monitoring_system=False,
            has_life_support_equipment=False,
            has_oxygen_generation_system=False,
            has_patient_litter_lift_system=False
        )

        self.assertEqual(asset.ambulatory_capacity, 15)
        self.assertEqual(asset.litter_capacity, 0)

class TestMissionRequirementsAdditional4(unittest.TestCase):

    def test_weather_conditions(self):
        mission = MissionRequirements(
            name='Weather Conditions Test',
            medevac_needed=True,
            evac_needed=False,
            resupply_needed=False,
            require_vtol=True,
            require_ctol=False,
            require_ground_vehicle=False,
            litters_spaces_required=1,
            ambulatory_spaces_required=1,
            weather_condition='rainy',  # testing a different weather condition
            day_mission=True,
            night_mission=False,
            require_iv_provisions=False,
            require_medical_monitoring_system=False,
            require_life_support_equipment=False,
            require_oxygen_generation_system=False,
            require_patient_litter_lift_system=False
        )

        self.assertEqual(mission.weather_condition, 'rainy')

    def test_mission_requirements_combination(self):
        mission = MissionRequirements(
            name='Combined Requirements Test',
            medevac_needed=True,
            evac_needed=True,
            resupply_needed=True,
            require_vtol=True,
            require_ctol=False,
            require_ground_vehicle=False,
            litters_spaces_required=2,
            ambulatory_spaces_required=2,
            weather_condition='clear',
            day_mission=True,
            night_mission=True,
            require_iv_provisions=True,
            require_medical_monitoring_system=True,
            require_life_support_equipment=True,
            require_oxygen_generation_system=True,
            require_patient_litter_lift_system=True
        )

        self.assertTrue(mission.medevac_needed and mission.evac_needed)
        self.assertTrue(mission.resupply_needed)
        self.assertTrue(mission.require_iv_provisions and mission.require_medical_monitoring_system)
        self.assertTrue(mission.require_life_support_equipment and mission.require_oxygen_generation_system)
        self.assertTrue(mission.day_mission and mission.night_mission)

class TestAssetAdditional4(unittest.TestCase):

    def test_asset_crew(self):
        asset = Asset(
            asset_name='Crew Test Asset',
            asset_type='ground',
            asset_status='available',
            asset_mission_type='evac',
            crew=['driver', 'medic_1', 'medic_2'],  # testing different crew members
            litter_capacity=0,
            ambulatory_capacity=4,
            operational_day=True,
            operational_night=True,
            operational_adverse_weather=True,
            has_iv_provisions=True,
            has_medical_monitoring_system=True,
            has_life_support_equipment=True,
            has_oxygen_generation_system=True,
            has_patient_litter_lift_system=True
        )

        self.assertIn('driver', asset.crew)
        self.assertIn('medic_1', asset.crew)
        self.assertIn('medic_2', asset.crew)
        self.assertEqual(len(asset.crew), 3)

class TestMissionRequirementsAdditional5(unittest.TestCase):

    def test_require_ground_vehicle(self):
        mission = MissionRequirements(
            name='Ground Vehicle Test',
            medevac_needed=False,
            evac_needed=False,
            resupply_needed=True,
            require_vtol=False,
            require_ctol=False,
            require_ground_vehicle=True,  # testing requirement for ground vehicle
            litters_spaces_required=0,
            ambulatory_spaces_required=10,
            weather_condition='clear',
            day_mission=True,
            night_mission=False,
            require_iv_provisions=False,
            require_medical_monitoring_system=False,
            require_life_support_equipment=False,
            require_oxygen_generation_system=False,
            require_patient_litter_lift_system=False
        )

        self.assertTrue(mission.require_ground_vehicle)

    def test_mission_name_length(self):
        mission = MissionRequirements(
            name='Short Name',
            medevac_needed=False,
            evac_needed=False,
            resupply_needed=False,
            require_vtol=False,
            require_ctol=False,
            require_ground_vehicle=False,
            litters_spaces_required=0,
            ambulatory_spaces_required=0,
            weather_condition='clear',
            day_mission=True,
            night_mission=False,
            require_iv_provisions=False,
            require_medical_monitoring_system=False,
            require_life_support_equipment=False,
            require_oxygen_generation_system=False,
            require_patient_litter_lift_system=False
        )

        self.assertLessEqual(len(mission.name), 20)  # testing maximum name length

class TestAssetAdditional3(unittest.TestCase):

    def test_asset_status(self):
        asset = Asset(
            asset_name='Status Test Asset',
            asset_type='ground',
            asset_status='maintenance',  # testing asset status different from available or unavailable
            asset_mission_type='evac',
            crew=['driver'],
            litter_capacity=2,
            ambulatory_capacity=4,
            operational_day=True,
            operational_night=True,
            operational_adverse_weather=True,
            has_iv_provisions=True,
            has_medical_monitoring_system=True,
            has_life_support_equipment=True,
            has_oxygen_generation_system=True,
            has_patient_litter_lift_system=True
        )

        self.assertNotIn(asset.asset_status, ['available', 'unavailable'])
        self.assertEqual(asset.asset_status, 'maintenance')

    def test_asset_capacity_overflow(self):
        asset = Asset(
            asset_name='Capacity Overflow Asset',
            asset_type='ground',
            asset_status='available',
            asset_mission_type='medevac',
            crew=['driver', 'medic_1'],
            litter_capacity=3,
            ambulatory_capacity=5,  # testing capacity overflow
            operational_day=True,
            operational_night=True,
            operational_adverse_weather=True,
            has_iv_provisions=True,
            has_medical_monitoring_system=True,
            has_life_support_equipment=True,
            has_oxygen_generation_system=True,
            has_patient_litter_lift_system=True
        )

        self.assertGreaterEqual(asset.ambulatory_capacity, len(asset.crew))

class TestMissionRequirementsAdditional6(unittest.TestCase):

    def test_medical_requirements(self):
        mission = MissionRequirements(
            name='Medical Requirements Test',
            medevac_needed=True,
            evac_needed=False,
            resupply_needed=False,
            require_vtol=True,
            require_ctol=False,
            require_ground_vehicle=False,
            litters_spaces_required=1,
            ambulatory_spaces_required=1,
            weather_condition='clear',
            day_mission=True,
            night_mission=False,
            require_iv_provisions=True,
            require_medical_monitoring_system=True,
            require_life_support_equipment=False,
            require_oxygen_generation_system=False,
            require_patient_litter_lift_system=False
        )

        self.assertTrue(mission.medevac_needed)
        self.assertTrue(mission.require_vtol)
        self.assertTrue(mission.require_iv_provisions)
        self.assertTrue(mission.require_medical_monitoring_system)
        self.assertFalse(mission.require_life_support_equipment)

    def test_mission_availability(self):
        mission = MissionRequirements(
            name='Mission Availability Test',
            medevac_needed=True,
            evac_needed=False,
            resupply_needed=True,
            require_vtol=True,
            require_ctol=False,
            require_ground_vehicle=False,
            litters_spaces_required=2,
            ambulatory_spaces_required=2,
            weather_condition='clear',
            day_mission=True,
            night_mission=False,
            require_iv_provisions=True,
            require_medical_monitoring_system=True,
            require_life_support_equipment=True,
            require_oxygen_generation_system=True,
            require_patient_litter_lift_system=True
        )

        self.assertTrue(mission.medevac_needed)
        self.assertTrue(mission.resupply_needed)
        self.assertTrue(mission.day_mission)
        self.assertFalse(mission.night_mission)

class TestAssetAdditional2(unittest.TestCase):

    def test_asset_type(self):
        asset = Asset(
            asset_name='Asset Type Test',
            asset_type='ground',
            asset_status='available',
            asset_mission_type='medevac',
            crew=['driver'],
            litter_capacity=2,
            ambulatory_capacity=4,
            operational_day=True,
            operational_night=True,
            operational_adverse_weather=True,
            has_iv_provisions=True,
            has_medical_monitoring_system=True,
            has_life_support_equipment=True,
            has_oxygen_generation_system=True,
            has_patient_litter_lift_system=True
        )

        self.assertEqual(asset.asset_type, 'ground')
        self.assertNotEqual(asset.asset_type, 'air')  # checking different asset types

    def test_asset_mission_type_availability(self):
        asset = Asset(
            asset_name='Mission Type Availability Asset',
            asset_type='vtol',
            asset_status='available',
            asset_mission_type='evac',  # testing a different mission type
            crew=['pilot', 'copilot'],
            litter_capacity=2,
            ambulatory_capacity=4,
            operational_day=True,
            operational_night=True,
            operational_adverse_weather=True,
            has_iv_provisions=True,
            has_medical_monitoring_system=True,
            has_life_support_equipment=True,
            has_oxygen_generation_system=True,
            has_patient_litter_lift_system=True
        )

        self.assertNotIn(asset.asset_mission_type, ['medevac', 'resupply'])

class TestMissionRequirementsAdditional7(unittest.TestCase):

    def test_ground_vehicle_requirement(self):
        mission = MissionRequirements(
            name='Ground Vehicle Requirement Test',
            medevac_needed=True,
            evac_needed=False,
            resupply_needed=True,
            require_vtol=False,
            require_ctol=False,
            require_ground_vehicle=True,
            litters_spaces_required=2,
            ambulatory_spaces_required=2,
            weather_condition='clear',
            day_mission=True,
            night_mission=False,
            require_iv_provisions=True,
            require_medical_monitoring_system=True,
            require_life_support_equipment=False,
            require_oxygen_generation_system=False,
            require_patient_litter_lift_system=False
        )

        self.assertTrue(mission.require_ground_vehicle)
        self.assertFalse(mission.require_vtol)

    def test_mission_litters_capacity(self):
        mission = MissionRequirements(
            name='Litters Capacity Test',
            medevac_needed=True,
            evac_needed=False,
            resupply_needed=False,
            require_vtol=True,
            require_ctol=False,
            require_ground_vehicle=False,
            litters_spaces_required=4,
            ambulatory_spaces_required=0,
            weather_condition='clear',
            day_mission=True,
            night_mission=False,
            require_iv_provisions=True,
            require_medical_monitoring_system=True,
            require_life_support_equipment=False,
            require_oxygen_generation_system=False,
            require_patient_litter_lift_system=False
        )

        self.assertEqual(mission.litters_spaces_required, 4)
        self.assertTrue(mission.medevac_needed)
        self.assertTrue(mission.require_vtol)

class TestAssetAdditional1(unittest.TestCase):

    def test_asset_operational_weather(self):
        asset = Asset(
            asset_name='Operational Weather Test',
            asset_type='ground',
            asset_status='available',
            asset_mission_type='medevac',
            crew=['driver', 'medic_1'],
            litter_capacity=2,
            ambulatory_capacity=4,
            operational_day=True,
            operational_night=True,
            operational_adverse_weather=True,  # testing adverse weather capability
            has_iv_provisions=True,
            has_medical_monitoring_system=True,
            has_life_support_equipment=True,
            has_oxygen_generation_system=True,
            has_patient_litter_lift_system=True
        )

        self.assertTrue(asset.operational_day)
        self.assertTrue(asset.operational_night)
        self.assertTrue(asset.operational_adverse_weather)

    def test_asset_crew_roles(self):
        asset = Asset(
            asset_name='Crew Roles Test',
            asset_type='vtol',
            asset_status='available',
            asset_mission_type='evac',
            crew=['pilot', 'copilot', 'medic_1'],  # testing different crew roles
            litter_capacity=2,
            ambulatory_capacity=4,
            operational_day=True,
            operational_night=True,
            operational_adverse_weather=False,
            has_iv_provisions=True,
            has_medical_monitoring_system=True,
            has_life_support_equipment=True,
            has_oxygen_generation_system=True,
            has_patient_litter_lift_system=True
        )

        self.assertIn('pilot', asset.crew)
        self.assertIn('medic_1', asset.crew)
        self.assertEqual(len(asset.crew), 3)

class TestMissionRequirementsAdditional0(unittest.TestCase):

    def test_ground_vehicle_requirement(self):
        mission = MissionRequirements(
            name='Ground Vehicle Requirement Test',
            medevac_needed=False,
            evac_needed=True,
            resupply_needed=False,
            require_vtol=False,
            require_ctol=False,
            require_ground_vehicle=True,  # Testing ground vehicle requirement
            litters_spaces_required=0,
            ambulatory_spaces_required=2,
            weather_condition='clear',
            day_mission=True,
            night_mission=False,
            require_iv_provisions=False,
            require_medical_monitoring_system=True,
            require_life_support_equipment=False,
            require_oxygen_generation_system=False,
            require_patient_litter_lift_system=False
        )

        self.assertTrue(mission.evac_needed)
        self.assertTrue(mission.require_ground_vehicle)
        self.assertEqual(mission.ambulatory_spaces_required, 2)

    def test_weather_conditions_edge_cases(self):
        mission = MissionRequirements(
            name='Weather Conditions Edge Cases Test',
            medevac_needed=True,
            evac_needed=False,
            resupply_needed=True,
            require_vtol=True,
            require_ctol=False,
            require_ground_vehicle=False,
            litters_spaces_required=1,
            ambulatory_spaces_required=1,
            weather_condition='extreme',  # testing extreme weather condition
            day_mission=True,
            night_mission=False,
            require_iv_provisions=True,
            require_medical_monitoring_system=True,
            require_life_support_equipment=True,
            require_oxygen_generation_system=True,
            require_patient_litter_lift_system=True
        )

        self.assertEqual(mission.weather_condition, 'extreme')
        self.assertTrue(mission.medevac_needed)
        self.assertTrue(mission.resupply_needed)
        self.assertTrue(mission.require_iv_provisions)

class TestAssetAdditional11(unittest.TestCase):

    def test_asset_operational_status(self):
        asset = Asset(
            asset_name='Operational Status Test Asset',
            asset_type='ground',
            asset_status='available',
            asset_mission_type='medevac',
            crew=['driver', 'medic_1'],
            litter_capacity=2,
            ambulatory_capacity=4,
            operational_day=True,
            operational_night=True,
            operational_adverse_weather=False,  # testing adverse weather condition
            has_iv_provisions=True,
            has_medical_monitoring_system=True,
            has_life_support_equipment=True,
            has_oxygen_generation_system=True,
            has_patient_litter_lift_system=True
        )

        self.assertTrue(asset.operational_day)
        self.assertTrue(asset.operational_night)
        self.assertFalse(asset.operational_adverse_weather)

    def test_asset_crew_capacity(self):
        asset = Asset(
            asset_name='Crew Capacity Test Asset',
            asset_type='vtol',
            asset_status='available',
            asset_mission_type='medevac',
            crew=['pilot', 'copilot', 'medic_1', 'medic_2'],
            litter_capacity=4,
            ambulatory_capacity=4,
            operational_day=True,
            operational_night=True,
            operational_adverse_weather=True,
            has_iv_provisions=True,
            has_medical_monitoring_system=True,
            has_life_support_equipment=True,
            has_oxygen_generation_system=True,
            has_patient_litter_lift_system=True
        )

        self.assertEqual(len(asset.crew), 4)
        self.assertIn('medic_1', asset.crew)
        self.assertIn('medic_2', asset.crew)
        self.assertEqual(asset.litter_capacity, 4)

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
    filename = "testing_report_mission_options_asserts.csv"
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












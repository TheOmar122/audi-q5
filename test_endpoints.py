import unittest
from app import app

class TestDL501Simulator(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'AUDI Q5 2.0 TFSI', res.data)
        self.assertIn(b'DL501 / 0B5', res.data)

    def test_specs(self):
        res = self.client.get('/api/specs')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['vehicle']['nominal_power_hp'], 211)
        self.assertEqual(data['transmission']['model'], 'DL501 (0B5)')

    def test_gears(self):
        res = self.client.get('/api/gears')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn('D', data['gears'])
        self.assertIn('M8', data['gears'])

    def test_gear_D(self):
        res = self.client.get('/api/gear/D')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['gear'], 'D')
        self.assertEqual(len(data['solenoids']), 10)
        self.assertIn('N433', data['solenoids'])
        self.assertIn('N472', data['solenoids'])
        self.assertEqual(data['clutches']['K1']['engagement_pct'], 100)

    def test_gear_M1(self):
        res = self.client.get('/api/gear/M1')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['gear'], 'M1')
        self.assertEqual(data['clutches']['K1']['engagement_pct'], 100)
        self.assertEqual(data['clutches']['K2']['engagement_pct'], 0)
        self.assertEqual(data['shift_forks']['1-3']['position_mm'], 8.5)

    def test_telemetry_get(self):
        res = self.client.get('/api/telemetry?gear=M1&speed=30&throttle=50')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertGreater(data['engine_rpm'], 800)
        self.assertGreater(data['wheel_torque_nm'], 1000)
        self.assertAlmostEqual(data['front_axle_torque_nm'] + data['rear_axle_torque_nm'], data['wheel_torque_nm'], places=1)

    def test_telemetry_post(self):
        payload = {"gear": "M2", "speed_kmh": 50, "throttle_pct": 70}
        res = self.client.post('/api/telemetry', json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['gear'], 'M2')
        self.assertGreater(data['engine_rpm'], 1000)

    def test_diagnostics(self):
        res = self.client.get('/api/diagnostics')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['protocol'], 'UDS (ISO 14229) over CAN')
        self.assertGreaterEqual(len(data['checks']), 5)

if __name__ == '__main__':
    unittest.main()

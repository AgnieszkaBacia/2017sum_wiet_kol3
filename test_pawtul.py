#source: https://github.com/pawtul/2017sum_wiet_kol1
from simulators import PlaneSimulator
from planes import Plane
import unittest



class TestPlaneFunctions(unittest.TestCase):
  def test_default_correct_position(self):
    plane = Plane()
    self.assertEqual(plane.correct_position, 0)

  def test_position(self):
    plane = Plane(2)
    self.assertEqual(plane.correct_position, 2)

  def test_negative_position(self):
    plane = Plane(-20)
    self.assertEqual(plane.correct_position, -20)

  def test_float_position(self):
    plane = Plane(9.123)
    self.assertEqual(plane.correct_position, 9.123)

  def test_apply_tilt(self):
    plane = Plane()
    plane.apply_tilt(-1)
    self.assertEqual(plane.position, -1)

  def test_apply_tilt_with_not_zero_correct_position(self):
    plane = Plane(-3)
    plane.apply_tilt(30)
    self.assertEqual(plane.position, 27)

  def test_correct_flight(self):
    plane = Plane()
    plane.apply_tilt(-23)
    self.assertEqual(plane.correct_flight(), 23)

  def test_correct_flight_float_tilt(self):
    plane = Plane(2)
    plane.apply_tilt(12.12)
    self.assertEqual(plane.correct_flight(), 12.12)

  def test_correct_flight_position(self):
    plane = Plane(-5)
    plane.apply_tilt(10)
    plane.correct_flight()
    self.assertEqual(plane.position, -5)


class TestSimulatorFinctions(unittest.TestCase):
  def test_generate_tilt_lower_limit(self):
    plane = Plane()
    sim = PlaneSimulator(plane)
    tilt = sim.generate_tilt()
    self.assertTrue(tilt > -45)
    
  def test_generate_tilt_upper_limit(self):
    plane = Plane()
    sim = PlaneSimulator(plane)
    tilt = sim.generate_tilt()
    self.assertTrue(tilt < 45)

  def test_simulator_initialization(self):
    plane = Plane(0)
    sim = PlaneSimulator(plane)
    self.assertIs(sim.plane, plane)

if __name__ == '__main__':
  unittest.main()

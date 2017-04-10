#source: https://github.com/pawtul/2017sum_wiet_kol1
from simulators import PlaneSimulator
from planes import Plane
import unittest



class TestPlaneFunctions(unittest.TestCase):

  def test_correct_flight(self):
    plane = Plane(2)
    self.assertEqual(plane.correct_flight(), 0)

if __name__ == '__main__':
  unittest.main()
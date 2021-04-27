import unittest
import battery_charge_ranges

class test_battery_charge_ranges(unittest.TestCase):
    def test_charge_ranges_no(self):
        ranges = battery_charge_ranges.charge_ranges([1,2,3])
        self.assertEqual(len(ranges), 1)
    def test_charge_ranges_to_value(self):
        ranges = battery_charge_ranges.charge_ranges([1, 2, 3, 7])
        self.assertEqual(ranges[0][-1], 3)


if __name__ == '__main__':
    unittest.main()

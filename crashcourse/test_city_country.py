import unittest
from city_functions import city_country

class TestCityCounty(unittest.TestCase):
  def test_city_country(self):
    output = city_country('santiago','chile', 50000)
    self.assertEqual(output, "Santiago, Chile, population=50000")
    output = city_country('santiago','chile')
    self.assertEqual(output, "Santiago, Chile")

unittest.main()


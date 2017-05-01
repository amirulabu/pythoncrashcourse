import unittest

from city_function import city_country

class CityTestCase(unittest.TestCase):

	def test_city_country(self):
		formatted_city = city_country("bangkok", "thailand", 500000)
		self.assertEqual(formatted_city, "Bangkok, Thailand - population 500000")

unittest.main()
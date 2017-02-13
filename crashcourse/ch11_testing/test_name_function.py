import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
  # must inherit unittest.TestCase
  """tests for 'name_function.py"""
  def test_first_last(self):
    formatted = get_formatted_name('janis','joplin')
    self.assertEqual(formatted, 'Janis Joplin')

  def test_first_middle_last(self):
    formatted = get_formatted_name('wolfgang','mozart', 'amadeus')
    self.assertEqual(formatted, 'Wolfgang Amadeus Mozart')
    formatted = get_formatted_name('wolfgang','mozart')
    self.assertEqual(formatted, 'Wolfgang Mozart')

unittest.main()

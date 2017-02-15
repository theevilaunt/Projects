import unittest
from Employee import employee

class EmployeeTestCase(unittest.TestCase):
  def setUp(self):
    self.first = "tom"
    self.last = "jones"
    self.salary = 50000
    self.my_employee = \
      employee(self.first,self.last, self.salary)

  def test_name(self):
    self.assertEqual(self.my_employee.first, self.first.title())
    self.assertEqual(self.my_employee.last, self.last.title())

  def test_salary(self):
    self.assertEqual(self.my_employee.salary, self.salary)

  def test_raise_default(self):
    self.my_employee.give_raise()
    self.assertEqual(self.my_employee.salary, 55000)

  def test_raise_specified(self):
    self.my_employee.give_raise(10000)
    self.assertEqual(self.my_employee.salary, 60000)

unittest.main()

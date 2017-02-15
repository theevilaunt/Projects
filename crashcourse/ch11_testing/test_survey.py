import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
  """Tests for class Anonymous Survey"""
  def setUp(self):
    """create survey/response for test methods"""
    question = "first language?"
    self.test_survey = AnonymousSurvey(question)
    self.responses = ['English','Spanish','Mandarin']

  def test_store_single_response(self):
    """test single response"""
    self.test_survey.store_response(self.responses[0])
    self.assertIn(self.responses[0],self.test_survey.responses)

  def test_store_multiple_response(self):
    """test multiple response"""
    for response in self.responses:
      self.test_survey.store_response(response)
    for response in self.responses:
      self.assertIn(response,self.test_survey.responses)

unittest.main()

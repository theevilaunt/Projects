class AnonymousSurvey():
  """Collect anonymous answer to a survey question"""

  def __init__(self, question):
    """store question/prepare to store responses"""
    self.question = question
    self.responses = []

  def show_question(self):
    """Show survey question"""
    print(self.question)

  def store_response(self, new_response):
    """store single survey response"""
    self.responses.append(new_response)

  def show_results(self):
    """show all the responses given"""
    print("Survey results:")
    for response in self.responses:
      print("--" + response)

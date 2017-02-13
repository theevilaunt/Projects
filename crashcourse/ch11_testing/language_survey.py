from survey import AnonymousSurvey

# define question, make survey

question = "Your first language?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter q to quit.")

while True:
  response = input("Language? ")
  if response == 'q':
    break
  my_survey.store_response(response)

#Show survey results
print("Thanks for participating.")
my_survey.show_results()

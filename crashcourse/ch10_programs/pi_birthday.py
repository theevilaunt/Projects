filename = "PythonCrashCourseSourceFiles/chapter_10/pi_million_digits.txt"

with open(filename) as fp:
  lines = fp.readlines()

pi_string = ''

for line in lines:
  pi_string += line.rstrip()

print(pi_string[:52])

bday = input("enter bday in mmddyy: ")

if bday in pi_string:
  print("success")
else:
  print("failure")

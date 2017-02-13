from name_function import get_formatted_name

print("enter 'q' to quit")
while True:
  first = input("first name: ")
  if first == 'q':
    break
  last = input("last name: ")
  if last == 'q':
    break
  print("result: '%s'" % get_formatted_name(first,last))

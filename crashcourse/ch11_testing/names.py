from name_function import get_formatted_name

print("Enter 'q' to quit")

while True:
  first = input("\nFirst Name: ")
  if first == 'q':
    break

  last = input("\nLast Name: ")
  if last == 'q':
    break

  print("formatted: %s" % get_formatted_name(first,last))

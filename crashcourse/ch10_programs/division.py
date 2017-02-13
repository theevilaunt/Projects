print("divide 2 numbers or q to quit")
while True:
  first = input("\nfirst number: ")
  if first == 'q':
    break
  try:
    first_num = int(first)
  except ValueError:
    print("only numeric input allowed ")
    continue

  while True:
    second = input("\nsecond number: ")
    if second == 'q':
      break
    try:
      second_num = int(second)
      break
    except ValueError:
      print("only numeric input allowed ")

  if second == 'q':
    break
  try:
    answer = int(first)/int(second)
  except ZeroDivisionError:
    print("you can't divide by zero!")
  else:
    print(answer)

fn = "ch10_data/guest_book1.txt"
with open(fn, 'w') as fp:
  while True:
    answer = input("your name? [q to quit]: ")
    if answer != 'q'.lower():
      fp.write("%s\n" % answer)
    else:
      break

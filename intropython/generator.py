def my_range(first=0, last=10, step=1):
  number = first
  while number < last:
    yield number
    number += step

def gen():
  for number in range(1,10):
    yield "Got %d" % number

print([number for number in gen()]) # test 4.7 not sure if right


#print(sum(range(1,101)))

# a = my_range(1,21)
# for number in a:
#   print(number)

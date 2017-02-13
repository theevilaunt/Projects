fp = 'ch10_data/pi_digits.txt'
with open(fp) as file_object:
  contents = file_object.read()
  print(contents.rstrip())

print()

with open(fp) as file_object:
  for line in file_object:
    print(line.rstrip())

print()

with open(fp) as file_object:
  lines = file_object.readlines()

pi_string = ''

for line in lines:
  #print('"%s" (%d)' % (line.rstrip(), len(line.rstrip())))
  pi_string += line.rstrip()

print('\n"%s" (%d)' % (pi_string, len(pi_string)))

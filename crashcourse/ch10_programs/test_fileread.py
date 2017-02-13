filename = 'ch10_data/about_python.txt'
print("all at once")
with open(filename) as fp:
  lines_all = fp.read()
print(lines_all)
print("\ncopy into array, then print")
with open(filename) as fp:
  lines = fp.readlines()
for line in lines:
  print(line.rstrip())
print("\nline at a time without intermediate storage")
with open(filename) as fp:
  for line in fp:
    print(line.rstrip().replace('python','java'))

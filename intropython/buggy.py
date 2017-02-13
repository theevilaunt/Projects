def buggy(arg, result=[]):
  result.append(arg)
  print(result)

buggy('a')
buggy('b')

def works(arg):
  result = []
  result.append(arg)
  return result

print("%s" % works('a'))
print("%s" % works('b'))

def nonbuggy(arg, result=None):
  if result is None:
    result = []
  result.append(arg)
  print(result)

nonbuggy('a')
nonbuggy('b')

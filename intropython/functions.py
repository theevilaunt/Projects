def make_a_sound(sound):
  return  sound

print(make_a_sound('quack'))
print(make_a_sound('cheep'))

def is_none(thing):
  if thing is None:
    #print("NONE")
    return "NONE"
  elif thing:
    #print("TRUE")
    return "TRUE"
  else:
    #print("FALSE")
    return "FALSE"


print("None: %s" % is_none(None))
print("True: %s" % is_none(True))
print("False: %s" % is_none(False))
print("0: %s" % is_none(0))
print("1: %s" % is_none(1))

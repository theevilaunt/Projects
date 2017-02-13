import json

fn = 'ch10_data/favorite_number2.txt'

def get_saved_number(fn):
  try:
    with open(fn) as fo:
      saved_number = json.load(fo)
    return int(saved_number)
  except:
    return None

def save_number(fn, number):
  with open(fn, 'w') as fo:
    json.dump(number, fo)


favorite_number = get_saved_number(fn)
if favorite_number != None:
  print("your favorite number is %d" % favorite_number)
else:
  favorite_number = input("your favorite number? ")
  try:
    save_this = int(favorite_number)
  except:
    print("invalid input")
  else:
    print("saving your favorite number %d" % save_this)
    save_number(fn, save_this)

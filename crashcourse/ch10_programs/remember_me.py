import json

fn = 'ch10_data/username4.json'

def get_stored_username(fn):
  try:
    with open(fn) as fo:
      username = json.load(fo)
    return username
  except:
    return None

def get_new_username(fn):
    username = input("name: ")
    print("welcome %s" % username)
    with open(fn, 'w') as fo:
      json.dump(username, fo)
      print("will remember %s on return" % username)

def greet_user(fn):
  username = get_stored_username(fn)
  if username == None:
    get_new_username(fn)
  else:
    while True:
      match = input("are you %s? (y or n or q) " % username)
      match = match.lower()
      print("'%s'" % match)
      if match == 'q':
        break
      elif match != 'y' and match != 'n':
        print("invalid input")
      elif match == 'y':
        print("welcome back %s" % username)
        break;
      else:
        get_new_username(fn)
        break

greet_user(fn)

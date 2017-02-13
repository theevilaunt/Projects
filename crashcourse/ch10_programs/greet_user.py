import json

fn = 'ch10_data/username.json'
with open(fn) as fo:
  username = json.load(fo)
  print("welcome back %s" % username)

import json

fn = 'ch10_data/numbers.json'

with open(fn) as fo:
  numbers = json.load(fo)

print(numbers)

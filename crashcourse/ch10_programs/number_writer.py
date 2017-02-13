import json

numbers = [2,3,5,7,1,13]

fn = 'ch10_data/numbers.json'
with open(fn, 'w') as fo:

  json.dump(numbers,fo)

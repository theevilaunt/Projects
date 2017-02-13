accusation = {
  'room':'ballroom',
  'weapon': 'lead pipe',
  'person': 'Col Mustard'
}

for card in accusation:
  print(card)

print("*" * 10)

for card in accusation.keys():
  print(card)

print("*" * 10)

for card in accusation.values():
  print(card)

print("*" * 10)

for item in accusation.items():
  print(item)

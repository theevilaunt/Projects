evens = {2,4,6,8}
odds = {1,3,5,7,9}

print(evens)
print(odds)

drinks = {
  'martini': {'vodka', 'vermouth'},
  'black russian': {'vodka', 'kahlua'},
  'white russian': {'cream', 'kahlua', 'vodka'},
  'manhattan': {'rye', 'vermouth', 'bitters'},
  'screwdriver': {'orange juice', 'vodka'}
}

bruss = drinks['black russian']
wruss = drinks['white russian']

print(bruss & wruss)
print(bruss - wruss)
print(bruss.difference(wruss))
print(wruss - bruss)

a = {1,2}
b = {2,3}

print("exclusive or:")
print(a^b)

print(a & b)

print(a.intersection(b))

print (a|b)
print(a.union(b))

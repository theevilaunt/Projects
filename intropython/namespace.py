def change_and_print_global():
  global animal
  animal = 'fruitbat'
  print('inside animal:', animal, id(animal))



animal = 'wombat'
change_and_print_global()
print('main animal:', animal, id(animal))

myList = {}
myList = locals()
print(myList)
for key in myList:
    print("local:", key)
print("globals",globals())

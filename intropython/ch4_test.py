# guess_me = 7

# while True:
#   guess = input("take a guess:")
#   try:
#     guess_me = int(guess)
#     if guess_me < 7:
#       print("too low")
#     elif guess_me > 7:
#       print("too high")
#     else:
#       print("just right")
#       break
#   except:
#       print("bad guess")

for guess_me in range(1,10):
    if guess_me < 7:
      print(guess_me, " is too low")
    elif guess_me > 7:
      print(guess_me, "is too high")
    else:
      print(guess_me, "is just right")
      break

for value in [3,2,1,0]:
  print(value)

print([x for x in range(1,10) if x % 2 == 0])

#4.6
odd = set([x for x in range(1,10) if x % 2 != 0])
print(odd)


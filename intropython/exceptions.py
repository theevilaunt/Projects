short_list = [1,2,3,4]

while True:
  #position = 5
  value = input("position ['q' to quit]:")
  if value == 'q':
    break
  try:
    position = int(value)
    print(short_list[position])
  except IndexError:
    print('Bad index:', position)
  except Exception as other:
    print("Something else failed", other)


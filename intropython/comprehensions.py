number_list = [number for number in range(1,6)]

print(number_list)

number_list = [number-1 for number in range(1,6)]

print(number_list)

odds = [number for number in range(1,10) if number % 2 == 1]

print(odds)

rows = range(1,5)
cols = range(1,3)

cells = [(row, col) for row in rows for col in cols]

print(cells)

for cell in cells:
  print(cell)

for row, col in cells:
  print(row,col)

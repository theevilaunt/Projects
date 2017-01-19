def odds(start = 1):
    if int(start) % 2 == 0: 
    	start = int(start) + 1
    else:
    	start = int(start)

    while True:
    	yield start
    	start += 2

for n in odds():
	if n > 7: break
	else: print(n)
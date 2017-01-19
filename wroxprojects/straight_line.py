def straight_line(gradient, x, constant):
	''' return y coordinate of straight line -> gradient * x + constant'''
	return gradient*x + constant

print(straight_line(2,4,-3))
for x in range(10):
	print(x,straight_line(2,x,-3))
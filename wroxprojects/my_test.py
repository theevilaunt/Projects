def my_test(start = 1):
	try:
		start = int(start)
	except:
		start = 1
	if start % 2 == 0:
		start = start + 1
	while True:
		print("hello %d" % start)
		yield start
		start += 2

value = my_test()
print("value: %s" % int(value))
my_test(3)
my_test('string')
my_test(4)
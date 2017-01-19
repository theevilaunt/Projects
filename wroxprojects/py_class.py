class MyClass(object):
	instance_count = 0
	def __init__(self, value):
		self.__value = value
		MyClass.instance_count += 1
		pinrt("instance# {} created".format(MyClass.instance_count))

	def aMethod(self, aValue):
		self.__value *= aValue
		
	def __str__(self):
		MyClass.instance_count -= 1
def answer():
  print(42)

def run_something(func):
  func() # parens indicates you should call function

def add_args(a,b):
  print("%s" % str(int(a) + int(b)))

def run_something_with_args(func, arg1, arg2):
  func(arg1,arg2)

def sum_args(*args):
  return sum(args)

def run_with_positional_args(func, *args):
  return func(*args)

def outer(a,b):
  def inner(c,d):
    return c + d
  return inner(a,b)

def knights(saying):
  def inner(quote):
    return "we are the knights who say: '%s'" % quote
  return inner(saying)

def knights2(saying):
  def inner2():
    return "we are the knights who say: '%s'" % saying
  return inner2

print(knights('Ni!'))
a = knights2('Ducks')
print(a())

#answer()
#type(answer)
run_something(answer) # lack of parens means just pass function

add_args(4,5)

run_something_with_args(add_args, 4, 5)

print(run_with_positional_args(sum_args, 1,2,3,4,5,6,7))

print(outer(50, 45))

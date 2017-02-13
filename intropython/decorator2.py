def enclose(func):
  def new_function(*args, **kwargs):
    print("start")
    func()
    print("end")
  return new_function

def showdoc(f):
  if f.__doc__:
    print('{}: {}'.format(f.__name__, f.__doc__))
  else:
    print('{}: No doctstring!'.format(f.__name__, f.__doc__))
  return f

@showdoc
def f1():
  '''has docstring'''
  return

@showdoc
def f2():
  pass

f1()

f2()

##@showdoc
@enclose
@showdoc
def does_nothing():
  '''
  useless docstring
  '''
  print("I am a useless function.")
  return 0

does_nothing()

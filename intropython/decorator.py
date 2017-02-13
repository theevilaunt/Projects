def doc_func(func):
  def new_func(*args, **kwargs):
      print("Running function:", func.__name__)
      print('positional args:', args)
      print('keyword args:', kwargs)
      result = func(*args, **kwargs)
      print("Result:", result)
      return result
  return new_func

def square_it(func):
  def new_function(*args, **kwargs):
    result = func(*args, **kwargs)
    return result * result
  return new_function


@square_it
@doc_func
def add_ints(a,b):
  return a + b

print(add_ints(3,5))

#cooler_add_ints = doc_func(add_ints)
#cooler_add_ints(3,5)

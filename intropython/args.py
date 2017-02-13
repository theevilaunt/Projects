def print_args(test1, test2, *args):
  print("positional argument tuple:", test1, test2, args)

print_args(1,2,3,4)
print_args(1,2,3)
print_args(1,2)

def print_kwargs(**kwargs):
  print('Keyword arguments:', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

def weird(*args, **kwargs):
  print(args)
  print(kwargs)

weird(1,2,3,wine='merlot', entree='mutton', dessert='macaroon')


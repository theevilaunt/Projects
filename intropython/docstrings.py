def test_docstring(stuff):
  '''
  this is a stupid docstring w/o
  any interesting info
  '''
  print("hello?", stuff)
  print("printing my own docstring <",test_docstring.__doc__,">")

test_docstring('bogus')
help(test_docstring)

class UpperCaseException(Exception):
  try:
    raise OopsException('panic')
  except OopsException as exc:
    print(exc)


words = ['eenie', 'meenie', 'miny', 'MO']
for word in words:
  if word.isupper():
    try:
      raise OopsException('panic')
    except:
      print(exc)

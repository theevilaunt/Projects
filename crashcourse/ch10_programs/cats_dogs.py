def open_file(fn):
  try:
    fp = open(fn)
    print("****" + fn + "****")
  except FileNotFoundError:
    pass
    #print("file '%s' not found" % fn)
    return None
  return fp

def get_contents(fp):
  if fp != None:
    lines = fp.readlines()
    fp.close()
    for line in lines:
      print(line.strip())

cat_file = 'bogus/ch10_data/cats.txt'
dog_file = 'dogs.txt'

fp = open_file(cat_file)
get_contents(fp)

fp = open_file(dog_file)
get_contents(fp)

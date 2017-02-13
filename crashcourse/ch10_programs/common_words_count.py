def count_words(fp):
  fn = 'PythonCrashCourseSourceFiles/chapter_10/' + fp
  try:
    with open(fn) as fo:
      contents = fo.read()
  except FileNotFoundError:
    pass #print("file %s not found" % fn)
  else:
    words = contents.split()
    num_words = len(words)
    print("%s has ~ %d words" % (fn, num_words))

    check_for_this = 'the'
    print("%s appears %d times" % (check_for_this, contents.lower().count(check_for_this)))

fn = ['bogus.txt', 'alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
# title = "Alice in Wonderland"
# title_list = title.split()

for file in fn:
  count_words(file)



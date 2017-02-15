class employee():
  def __init__(self, first, last, salary = 0):
    self.first = first.title()
    self.last = last.title()
    try:
      self.salary = int(salary)
    except:
      print('salary must be numeric')

  def give_raise(self, amount=5000):
    try:
      amount_int = int(amount)
    except:
      print('amount must be numeric')
    print("amount: %d" % amount_int)
    self.salary += amount_int


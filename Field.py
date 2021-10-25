class Field():
  def __init__(self):
    self.filedCards = []
  
  def add(self,card):
    self.filedCards.append(card)
    return self.judge()

  def remove(self,cards):
    for card in cards:
      self.filedCards.remove(card)

  def judge(self):
    checkCard = sorted(self.filedCards)
    output = []
    for i in range(12):
      duplicate = [s for s in checkCard if str(i+1) in s]
      print(duplicate)
      if(len(duplicate) >= 2):
        output.extend(duplicate)
      duplicate.clear()
    print()
    return output

  def getList(self):
    return self.filedCards

  def test(self):
    self.add("5a")
    self.add("1b")
    self.add("1a")
    self.add("3c")
    self.add("2a")
    print(self.filedCards)
    # self.remove(["1a","2a"])
    # print(self.filedCards)
    print(self.judge())

if __name__ == '__main__':
  field = Field()
  field.test()
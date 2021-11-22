class Field():
  def __init__(self):
    self.filedCards = []
  
  def add(self,card):
    self.filedCards.append(card)
    self.filedCards.sort()
    # return self.judge()
    return card

  def remove(self,cards):
    for card in cards:
      self.filedCards.remove(card)

  def judge(self):
    output = []

    for i in range(12):
      if i == 9:j = "A"
      elif i == 10:j = "B"
      elif i == 11:j = "C"
      else: j = str(i+1)

      duplicate = [s for s in self.filedCards if j in s]
      # print(j,duplicate)
      if(len(duplicate) >= 2):
        output.extend(duplicate)
      duplicate.clear()
    # print()
    return output

  def judgeCard(self,card):
    return [s for s in self.filedCards if card[0] in s]

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
    # print(self.judge())

if __name__ == '__main__':
  field = Field()
  field.test()
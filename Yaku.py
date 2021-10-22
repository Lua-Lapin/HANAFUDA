class Yaku():
  def __init__(self):
    self.yakuList = []# [[カード,カード,役名,得点],[],[]]
    self.yakuCount = len(self.yakuList)

  def check(self,cards,i):
    output = []
    count = 0
    for card in cards:
      if card in self.yakuList[i]:
        count += 1
    if count == len(self.yakuList[i])-2 :
      return [self.yakuList[-2],self.yakuList[-1]]

  def point(self,cards):
    for i in range(self.yakuCount):
      self.check(cards,i)
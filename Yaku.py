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

# 5光 11は雨 1a,3a,8a,11a,12a
# 10a酒 3a桜 8a月
# 7a猪 10a鹿 6a蝶
# 赤短1 2 3 b
# 青短6 9 10b
# 短4 5 7b

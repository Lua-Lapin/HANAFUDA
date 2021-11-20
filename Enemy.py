from Player import Player
from Yaku import Yaku
from Field import Field 
import random

class Enemy(Player):
  priority = [] # 役の優先順位作って
  yaku = Yaku()
  yakuList = []

  def __init__(self):
    super().__init__()
    self.create()

  def create(self):
    self.yakuList.append(["1a","3a","8a","Ba","Ca"])
    self.yakuList.append(["3a","8a","Aa"])
    self.yakuList.append(["1b","2b","3b"])
    self.yakuList.append(["6b","9b","Ab"])
    self.yakuList.append(["4b","5b","7b","Bc"])
    self.yakuList.append(["8a","9a"])
    self.yakuList.append(["3a","9a"])
    self.yakuList.append(["2a","4a","5a","6a","7a","9a","Aa","Bb"])
    self.yakuList.append(["other"])

  def search(self,cards,excl=[]):
    count = self.yaku.countYaku(cards)
    minAct = []

    if "Ba" in cards: count[0]=4-count[0]
    elif "Ba" not in cards: count[0]=3-count[0]
  
    count[1]=3-count[1]
    count[2]=3-count[2]
    count[3]=3-count[3]
    count[4]=5-count[4]
    count[5]=2-count[5]
    count[6]=2-count[6]
    count[7]=5-count[7]
    count[8]=10-count[8]
    count[9]=5-count[9]

    if len(excl)!=0:
      for i in excl:
        count[i]=100
    minAct = [i for i, v in enumerate(count) if v == min(count)]

    return minAct,count[minAct[0]]

  def searchAct(self,cards,ba):
    use=""
    minAct=[]
    wantCard = []
    haveHand = []
    haveField = []
    while True:
      if len(haveHand)!=0 or len(haveHand)!=0:
        if len(minAct)==9:
          use=""
          break
        minAct,dust = self.search(cards,excl=minAct)
      for i in minAct:
        dup=[]
        for j in self.yakuList[minAct[i]]:
          dup = [s for s in cards if j not in cards]
        wantCard.extend(dup)
        dup.clear()
      haveHand = list(set(wantCard) & set(self.getHand()))
      haveField = list(set(wantCard) & set(ba))
      if len(haveHand)!=0:
        dupl=[]
        for i in haveHand:
          dupl = [s for s in ba if i[0] in s]
        if dupl != 0:
          use=[s for s in haveHand if dupl[0] in s]
          use=use[0]
          break
      if len(haveField)!=0:
        dupl=[]
        for i in haveHand:
          dupl = [s for s in self.getHand() if i[0] in s]
        if dupl != 0:
          use=dup[0]
          break
    return use

  def judgeCard(self,card,ba):
    return [s for s in ba if card[0] in s]

  # ランダムに選んでカードを返す
  def random(self):
    # print(len(self.getHand()))
    a = random.randrange(len(self.getHand()))
    b = self.getHand()
    return b[a]

  def test(self):
    print(self.hand)

if __name__ == '__main__':
  # enemy = Enemy()
  # enemy.test()
  count = [1,1,1,3,5,2,2,5,3,1]
  a=[i for i, v in enumerate(count) if v == min(count)]
  print(a)
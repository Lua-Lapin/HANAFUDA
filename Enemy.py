from Player import Player
from Yaku import Yaku
from Field import Field 
import random

class Enemy(Player):
  priority = [] # 役の優先順位作って
  yaku = Yaku()
  def __init__(self):
    super().__init__()

  def search(self,cards):
    point = 0
    # point += self.countPoint(self.yaku.countYaku(self.getTicket()))
    for i in self.getHand():
      dupl = self.getTicket().copy()
      dupl.append(self.judgeCard(i,cards))
      out = self.yaku.check(self.getTicket())
      



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
  enemy = Enemy()
  enemy.test()
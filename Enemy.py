from Player import Player
import random

class Enemy(Player):
  def __init__(self):
    super().__init__()
    priority = [] # 役の優先順位作って

  def search(self):
    pass

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
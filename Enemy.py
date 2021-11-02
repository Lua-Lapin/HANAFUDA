from Player import Player

class Enemy(Player):
  def __init__(self):
    super().__init__()
    priority = [] # 役の優先順位作って

  def search(self):
    
    pass

  def test(self):
    print(self.hand)

if __name__ == '__main__':
  enemy = Enemy()
  enemy.test()
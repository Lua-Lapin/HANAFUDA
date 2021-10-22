import random

class Main():
  def __init__(self):
    # self.ba = field()
    self.currentTurn = 0
    self.deck = []
    self.generateDeck()

  def mainLoop(self):
    pass

  def shuffle(self):
      random.shuffle(self.deck)

  def generateDeck(self):
    for i in range(12):
      self.deck.append(str(i+1)+"a")
      self.deck.append(str(i+1)+"b")
      self.deck.append(str(i+1)+"c")
      self.deck.append(str(i+1)+"d")

  def test(self):
    print(self.deck)
    self.shuffle()
    print(self.deck)

if __name__ == '__main__':
  main = Main()
  main.test()
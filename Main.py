import random
from Field import Field 
from Player import Player
from Enemy import Enemy

class Main():
  def __init__(self):
    self.ba = Field()
    self.currentTurn = 0
    self.deck = []
    self.player = Player()
    self.enemy = Enemy()

    self.generateDeck()
    self.shuffle()

    self.distribute()

  def mainLoop(self):
    print("出すカードを選択してください:",self.player.getHandList())
    card = input()
    self.ba.add(card)
    print(self.ba.add(self.deck.pop(0)))
    pass

  def generateDeck(self):
    for i in range(12):
      self.deck.append(str(i+1)+"a")
      self.deck.append(str(i+1)+"b")
      self.deck.append(str(i+1)+"c")
      self.deck.append(str(i+1)+"d")

  def shuffle(self):
      random.shuffle(self.deck)

  def distribute(self):
    for i in range(4):
      self.player.addHand(self.deck.pop(0))
      self.player.addHand(self.deck.pop(0))
      self.ba.add(self.deck.pop(0))
      self.ba.add(self.deck.pop(0))
      self.enemy.addHand(self.deck.pop(0))
      self.enemy.addHand(self.deck.pop(0))


  def test(self):
    print(self.deck)
    self.shuffle()
    print(self.deck)

if __name__ == '__main__':
  main = Main()
  main.test()
  main.mainLoop()
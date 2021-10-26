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
    # プレーヤー側
    if self.currentTurn == 0:
      print("場のカード:",self.ba.getList())
      print("出すカードを選択してください:",self.player.getHand())
      card = input()
      self.ba.add(card)
      self.ba.add(self.deck.pop(0))
      self.player.playCard(card)

      self.ba.judgeCard(card)
      cards = self.ba.judgeCard(card)
      self.ba.remove(cards)
      self.player.addTicket(cards)

      # 役確認

      self.currentTurn += 1
      print(cards)
      print(self.player.getHand(),"\n",self.player.getTicket(),"\n",self.ba.getList())
    # CPU側
    else:
      pass

  def generateDeck(self):
    for i in range(12):
      if i == 9:j = "A"
      elif i == 10:j = "B"
      elif i == 11:j = "C"
      else: j = str(i+1)
      self.deck.extend([j+"a",j+"b",j+"c",j+"d"])

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
  # main.test()
  main.mainLoop()
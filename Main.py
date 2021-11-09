import random
from typing import Counter
from Field import Field 
from Player import Player
from Enemy import Enemy
from Yaku import Yaku

class Main():
  def __init__(self):
    self.ba = Field()
    self.currentTurn = 0
    self.deck = []
    self.player = Player()
    self.enemy = Enemy()
    self.yaku = Yaku()

    self.generateDeck()
    self.shuffle()

    self.distribute()

  def mainLoop(self):
    # プレーヤー側
    while(True):
      if self.currentTurn == 0:
        # カード出す 
        card = ""
        print("場のカード:",self.ba.getList())
        while card not in self.player.getHand():
          print("出すカードを選択してください:",self.player.getHand())
          card = input()
        self.ba.add(card)
        popcard = self.ba.add(self.deck.pop(0))
        self.player.playCard(card)

        # カード取る
        duplHand = self.ba.judgeCard(card)
        duplDeck = self.ba.judgeCard(popcard)
        if len(duplHand)%2 == 0:
          self.ba.remove(duplHand)
          self.player.addTicket(duplHand)
        elif len(duplHand) == 3:
          self.ba.remove(duplHand[:1])
          self.player.addTicket(duplHand[:1])
        if len(duplDeck)%2 == 0:
          self.ba.remove(duplDeck)
          self.player.addTicket(duplDeck)
        elif len(duplDeck) == 3:
          print("main,49:dupdeck",duplDeck)
          self.ba.remove(duplDeck[:1])
          self.player.addTicket(duplDeck[:1])

        # 役の判定
        judge = self.yaku.check(self.enemy.getTicket())
        if len(judge) != 0:
          self.enemy.addYaku(judge)
          print("役が成立しました：",judge)
          print("ゲームを終了します")
          return None

        print("P",self.player.getHand(),"\n",self.player.getTicket(),"\n",self.ba.getList(),"\n")
        self.currentTurn = 1

      else:
        # カード出す
        card = self.enemy.random()
        self.ba.add(card)
        popcard = self.ba.add(self.deck.pop(0))
        self.enemy.playCard(card)
        
        # カード取る
        duplHand = self.ba.judgeCard(card)
        duplDeck = self.ba.judgeCard(popcard)
        if len(duplHand)%2 == 0:
          self.ba.remove(duplHand)
          self.enemy.addTicket(duplHand)
        elif len(duplHand) == 3:
          self.ba.remove(duplHand[:1])
          self.enemy.addTicket(duplHand[:1])
        if len(duplDeck)%2 == 0:
          self.ba.remove(duplDeck)
          self.enemy.addTicket(duplDeck)
        elif len(duplDeck) == 3:
          self.ba.remove(duplDeck[:1])
          self.enemy.addTicket(duplDeck[:1])
        
        # 役の判定
        judge = self.yaku.check(self.enemy.getTicket())
        if len(judge) != 0:
          self.enemy.addYaku(judge)
          print("役が成立しました：",judge)
          print("ゲームを終了します")
          return None

        print("E",self.enemy.getHand(),"\n",self.enemy.getTicket(),"\n",self.ba.getList(),"\n")
        self.currentTurn = 0
      
      # 手がなくなった時点で終わり
      if len(self.enemy.getHand()) == 0:
        return None

      


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
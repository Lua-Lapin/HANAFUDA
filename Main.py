import random
from typing import Counter
from Field import Field 
from Player import Player
from Enemy import Enemy
from Yaku import Yaku

class Main():
  def __init__(self,player,enemy):
    self.ba = Field()
    self.deck = []
    self.yaku = Yaku()

    self.generateDeck()
    self.shuffle()

    self.distribute(player,enemy)
    # print("P",player.getHand(),"\n",player.getTicket(),"\n",self.ba.getList(),"\n")
    # print("E",enemy.getHand(),"\n",enemy.getTicket(),"\n",self.ba.getList(),"\n")

  def generateDeck(self):
    for i in range(12):
      if i == 9:j = "A"
      elif i == 10:j = "B"
      elif i == 11:j = "C"
      else: j = str(i+1)
      self.deck.extend([j+"a",j+"b",j+"c",j+"d"])

  def shuffle(self):
      random.shuffle(self.deck)

  def distribute(self,player,enemy):
    for i in range(4):
      player.addHand(self.deck.pop(0))
      player.addHand(self.deck.pop(0))
      self.ba.add(self.deck.pop(0))
      self.ba.add(self.deck.pop(0))
      enemy.addHand(self.deck.pop(0))
      enemy.addHand(self.deck.pop(0))

  def play(self,player,card):
    # カード出す
      # card = self.enemy.random()
      self.ba.add(card)
      popcard = self.ba.add(self.deck.pop(0))
      player.playCard(card)
      return [card,popcard]
  
  def catch(self,player,card,popcard):
  # カード取る
    duplHand = self.ba.judgeCard(card)
    duplDeck = self.ba.judgeCard(popcard)
    if len(duplHand)%2 == 0:
      self.ba.remove(duplHand)
      player.addTicket(duplHand)
    elif len(duplHand) == 3:
      self.ba.remove(duplHand[:2])
      player.addTicket(duplHand[:2])
    if len(duplDeck)%2 == 0:
      self.ba.remove(duplDeck)
      player.addTicket(duplDeck)
    elif len(duplDeck) == 3 and duplHand != duplDeck:
      self.ba.remove(duplDeck[:2])
      player.addTicket(duplDeck[:2])

  def isEnd(self,player):
  # 役の判定
    judge = self.yaku.check(player.getTicket())
    if len(judge) != 0:
      player.addYaku(judge)
      print("役が成立しました：",judge)
      print("ゲームを終了します")
      return judge

  def playTest(self,player):
    # カード出す 
    card = ""
    print("場のカード:",self.ba.getList())
    while card not in player.getHand():
      print("出すカードを選択してください:",player.getHand())
      card = input()
    self.ba.add(card)
    popcard = self.ba.add(self.deck.pop(0))
    player.playCard(card)
    return [card,popcard]

  def test(self):
    self.deck.append("1b")
    self.ba.add("1a")
    self.player.addHand("1c")
    print("P",self.player.getHand(),"\n",self.player.getTicket(),"\n",self.ba.getList(),"\n")
    self.player.playCard("1c")
    self.ba.add("1c")
    self.ba.add("1b")
    print("P",self.player.getHand(),"\n",self.player.getTicket(),"\n",self.ba.getList(),"\n")
    duplHand = self.ba.judgeCard("1c")
    duplDeck = self.ba.judgeCard("1b")
    print(duplDeck,duplHand)
    if len(duplHand)%2 == 0:
      self.ba.remove(duplHand)
      self.player.addTicket(duplHand)
    elif len(duplHand) == 3:
      self.ba.remove(duplHand[:2])
      self.player.addTicket(duplHand[:2])
    if len(duplDeck)%2 == 0:
      self.ba.remove(duplDeck)
      self.player.addTicket(duplDeck)
    elif len(duplDeck) == 3 and duplHand != duplDeck:
      print("main,49:dupdeck",duplDeck)
      self.ba.remove(duplDeck[:1])
      self.player.addTicket(duplDeck[:1])
    print("P",self.player.getHand(),"\n",self.player.getTicket(),"\n",self.ba.getList(),"\n")

  # ここに書く
def mainloop():
  player = Player()
  enemy = Enemy()
  main = Main(player,enemy)
  judge=[]
  currentTurn = 0
  while True:
    pop=""
    if currentTurn == 0:
      pop = main.playTest(player)
      main.catch(player,pop[0],pop[1])
      judge = main.isEnd(player)
      print(judge)
      if judge is not None:
        print("役が成立しました：",judge)
        print("ゲームを終了します")
        return judge
      print("P",player.getHand(),"\n",player.getTicket(),"\n")
      currentTurn = 1
      
    else:
      pop = main.play(enemy,enemy.random())
      main.catch(enemy,pop[0],pop[1])
      judge = main.isEnd(enemy)
      if judge is not None:
        print("役が成立しました：",judge)
        print("ゲームを終了します")
        return judge
      if len(enemy.getHand()) == 0:
        print("ゲームを終了します")
        return ["end"]
      print("P",enemy.getHand(),"\n",enemy.getTicket(),"\n")
      currentTurn = 0

if __name__ == '__main__':
  yaku = Yaku()
  judge = mainloop()
  if "end" not in judge:
    yaku.countPoint(judge)



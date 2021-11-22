import random
import time
from typing import Counter
from Agent import Agent
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
    if len(duplDeck)%2 == 0 and duplHand != duplDeck:
      # print(duplHand)
      # print(duplDeck)
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
      # print("役が成立しました：",judge)
      # print("ゲームを終了します",player)
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

def mainloop(agent):
  player = agent
  enemy = Enemy()
  main = Main(player,enemy)
  judge=[]
  currentTurn = 0
  while True:
    pop=""
    if currentTurn == 0:
      dust,pl=player.search(player.getTicket(),delAct(enemy))
      dust,en=enemy.search(enemy.getTicket(),delAct(player))
      # print(dust)
      ran = random.random()
      player.action(pl,en,0 if ran <= 0.5 else 1)
      a=player.searchAct(player.getTicket() if ran <= 0.5 else enemy.getTicket(),main.ba.getList())
      # print("a:",a)
      pop = main.play(player,player.random() if a!="" else a)
      main.catch(player,pop[0],pop[1])
      judge = main.isEnd(player)
      if judge is not None:
        # print("役が成立しました：",judge)
        # print(currentTurn,"ゲームを終了します")
        return [judge,currentTurn]
      # print("P",player.getHand(),"\n",player.getTicket(),"\n")
      currentTurn = 1
      
    else:
      pop = main.play(enemy,enemy.random())
      main.catch(enemy,pop[0],pop[1])
      judge = main.isEnd(enemy)
      if judge is not None:
        # print("役が成立しました：",judge)
        # print(currentTurn,"ゲームを終了します")
        return [judge,currentTurn]
      if len(enemy.getHand()) == 0:
        # print(currentTurn,"ゲームを終了します")
        return ["end"]
      # print("E",enemy.getHand(),"\n",enemy.getTicket(),"\n")
      currentTurn = 0

def delAct(enemy):
  ex=[0 for j in range(9)]
  out=[]
  # print(enemy.yakul)
  for i in enemy.getTicket():
    c=0
    for j in enemy.yakul:
      if i in j:
        ex[c]+=1
      c+=1
      # print(c,i,j)
  if ex[0]>=3:out.append(0)
  if ex[1]>=1:out.append(1)
  if ex[2]>=1:out.append(2)
  if ex[3]>=1:out.append(3)
  if ex[4]>=5:out.append(4)
  if ex[5]>=1:out.append(5)
  if ex[6]>=1:out.append(6)
  if ex[7]>=3:out.append(7)
  # print(out)
  return out

if __name__ == '__main__':
  start_time = time.time()
  yaku = Yaku()
  alpha=1
  gamma=1
  episode=2000
  agent = Agent(alpha,gamma)
  win=[0,0]
  for i in range(episode):
    judge = mainloop(agent)
    if "end" not in judge:
      a = yaku.countPoint(judge[0])
      # print(judge,a)
      if judge[1]==1:
        a*=-1
        win[1]+=1
      else:
        win[0]+=1
      agent.end(a)
    else:
      # print("end")
      agent.end(0)
    judge.clear()
    agent.reset()
    if i % (episode//10) == 0:
      print(i)
  dotime = time.time() - start_time
  print(agent.stateList,"\n")
  print(win,win[0]/episode,"%","\n")
  print(dotime,"sec","\n")
  # agent.test()
  # print(agent.stateList)
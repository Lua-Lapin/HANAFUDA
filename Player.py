class Player():
  def __init__(self):
    self.hand = []
    self.ticket = []
    self.yakuList = []

  def addHand(self,card):
    self.hand.append(card)
    self.hand.sort()

  def addTicket(self,cards):
    self.ticket.extend(cards)

  def playCard(self,card):
    self.hand.remove(card)

  def getHand(self):
    return self.hand

  def getTicket(self):
    return self.ticket

  def checkPoint(self):
    # 役の判定
    pass
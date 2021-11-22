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

  def addYaku(self,yaku):
    self.yakuList.append(yaku)

  def reset(self):
    self.hand.clear()
    self.ticket.clear()
    self.yakuList.clear()
class Player():
  def __init__(self):
    self.hands = []
    self.ticket = []
    self.yakuList = []

  def addHand(self,card):
    self.hands.append(card)

  def getTicket(self,card):
    self.ticket.append(card)

  def playCard(self,card):
    self.hands.remove(card)

  def getHandList(self):
    return self.hands

  def getTicketList(self):
    return self.ticket

  def checkPoint(self):
    # 役の判定
    pass
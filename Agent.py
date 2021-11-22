from Enemy import Enemy

class Agent(Enemy):
  def __init__(self,alpha,gamma):
    super().__init__()
    self.stateList = [[[0 for j in range(2)] for j in range(10)] for i in range(10)]
    # for i in range(10):
    #   self.stateList.append([])
    # for i in self.stateList:
    #   for j in range(10):
    #     self.stateList.append([])
    self.alpha=alpha
    self.gamma=gamma
    self.epi=[]

  def action(self,pl,en,act):
    self.epi.append([pl,en,act])

  def end(self,point):
    # print(point)
    # print(self.epi)
    c=0
    for i in self.epi[::-1]:
      a = self.stateList[i[0]][i[1]][i[2]]
      self.stateList[i[0]][i[1]][i[2]] += ((1 - self.alpha) * a + self.alpha * point) * (self.gamma ** c)
      c+=1

  def test(self):
    self.stateList[0][0][0]=100000000

if __name__ == '__main__':
  agent = Agent(0.5,0.9)
  # agent.state()
  print(agent.stateList,'\n')
  agent.test()
  print(agent.stateList)
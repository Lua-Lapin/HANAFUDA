from Enemy import Enemy

class Agent(Enemy):
  def __init__(self):
    super().__init__()
    self.stateList = [[[0]*2]*10]*10
  
  def action(self):
    pass

if __name__ == '__main__':
  agent = Agent()
  agent.state()
  print(agent.stateList)
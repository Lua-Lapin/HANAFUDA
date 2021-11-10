class Yaku():
  def __init__(self):
    pass

  def countYaku(self,cards):
    output = []
    output.append(len([s for s in cards if ("1a" in s)or("3a" in s)or("8a" in s)or("Ba" in s)or("Ca" in s)]))
    output.append(len([s for s in cards if ("3a" in s)or("8a" in s)or("Aa" in s)]))
    output.append(len([s for s in cards if ("1b" in s)or("2b" in s)or("3b" in s)]))
    output.append(len([s for s in cards if ("6b" in s)or("9b" in s)or("Ab" in s)]))
    output.append(len([s for s in cards if ("4b" in s)or("5b" in s)or("7b" in s)or("Bc" in s)]))
    output.append(len([s for s in cards if ("8a" in s)or("9a" in s)]))
    output.append(len([s for s in cards if ("3a" in s)or("9a" in s)]))
    output.append(len([s for s in cards if ("2a" in s)or("4a" in s)or("5a" in s)or("6a" in s)or("7a" in s)or("9a" in s)or("Aa" in s)or("Bb" in s)]))
    output.append(len([s for s in cards if ("d" in s)or("c" in s)and("B" not in s)or("12b" in s)]))

    return output

  def check(self,cards):
    output = []
    count = self.countYaku(cards)
    # print(count)

    if count[0] == 5: output.append("五光")
    elif count[0] == 4 and "Ba" in cards: output.append("雨四光")
    elif count[0] == 4: output.append("四光")
    elif count[0] == 3 and "Ba" not in cards: output.append("三光")
  
    if count[1] == 3: output.append("猪鹿蝶")
    if count[2] == 3: output.append("赤短")
    if count[3] == 3: output.append("青短")
    if count[4] + count[3] + count[2] >= 5: output.append("短")
    if count[5] == 3: output.append("花見で一杯")
    if count[6] == 3: output.append("月見で一杯")
    if count[7] >= 5: output.append("たね")
    if count[8] >= 10: output.append("かす")
    # print(output)
    return output
  
  def countPoint(self,yakulist):
    point = 0
    if "五光" in yakulist: point+=10
    if "雨四光" in yakulist: point+=8
    if "四光" in yakulist: point+=7
    if "三光" in yakulist: point+=5
    if "猪鹿蝶" in yakulist: point+=5
    if "赤短" in yakulist: point+=5
    if "青短" in yakulist: point+=5
    if "短" in yakulist: point+=1
    if "花見で一杯" in yakulist: point+=5
    if "月見で一杯" in yakulist: point+=5
    if "たね" in yakulist: point+=1
    if "かす" in yakulist: point+=1
    return point

    # def checkAlive(self,ticket):
    #   count = self.countYaku(ticket)

    #   if count[0] == 3 or count[0] == 2 and "Ba" not in cards: output.append("三光")
    #   elif count[0] == 2: output.append("四光")
    #   elif count[0] == 2 or count[0] >= 1 and "Ba" in cards: output.append("雨四光")
    #   elif count[0] == 1: output.append("五光")
    
    #   if count[1] >= 1: output.append("猪鹿蝶")
    #   if count[2] >= 1: output.append("赤短")
    #   if count[3] >= 1: output.append("青短")
    #   print(output)
      # return output

  def test(self):
    cards = ["1a","2a","3a","Aa","8a","Ca","Ba"]
    self.check(cards)
    self.countYaku(cards)

if __name__ == '__main__':
  yaku = Yaku()
  yaku.test()
# 5光 11は雨 1a,3a,8a,11a,12a
# 10a酒 3a桜 8a月
# 7a猪 10a鹿 6a蝶
# 赤短1 2 3 b
# 青短6 9 10b
# 短4 5 7b

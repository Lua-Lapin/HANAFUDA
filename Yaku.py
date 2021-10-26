class Yaku():
  def __init__(self):
    pass

  def check(self,cards):
    output = []
    countLig=len([s for s in cards if ("1a" in s)or("3a" in s)or("8a" in s)or("Ba" in s)or("Ca" in s)])
    countBat=len([s for s in cards if ("3a" in s)or("8a" in s)or("Aa" in s)])
    countRed=len([s for s in cards if ("1b" in s)or("2b" in s)or("3b" in s)])
    countBlu=len([s for s in cards if ("6b" in s)or("9b" in s)or("Ab" in s)])
    countTan=len([s for s in cards if ("4b" in s)or("5b" in s)or("7b" in s)])
    print(countLig,countBat,countBlu,countRed,countTan)

    if countLig == 5: output.append("五光")
    elif countLig == 4 and "Ba" in cards: output.append("雨四光")
    elif countLig == 4: output.append("四光")
    elif countLig == 3 and "Ba" not in cards: output.append("三光")
  
    if countBat == 3: output.append("猪鹿蝶")
    if countRed == 3: output.append("赤短")
    if countBlu == 3: output.append("青短")
    print(output)
    return output
  
  def countPoint(self,yakulist):
    point = 0
    if "五光" in yakulist: point+=0
    if "雨四光" in yakulist: point+=0
    if "四光" in yakulist: point+=0
    if "三光" in yakulist: point+=0
    if "猪鹿蝶" in yakulist: point+=0
    if "赤短" in yakulist: point+=0
    if "青短" in yakulist: point+=0
    return point

  def test(self):
    self.check(["1a","2a","3a","Aa","8a","Ca","Ba"])

if __name__ == '__main__':
  yaku = Yaku()
  yaku.test()
# 5光 11は雨 1a,3a,8a,11a,12a
# 10a酒 3a桜 8a月
# 7a猪 10a鹿 6a蝶
# 赤短1 2 3 b
# 青短6 9 10b
# 短4 5 7b

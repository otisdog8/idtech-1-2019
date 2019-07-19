class bot:
    def __init__(self,name,atk=10,de=10,spd=10,hp=100):
        self.atk = atk
        self.de = de
        self.spd = spd
        self.name = name
        self.hp = hp

    def livename(self):
        if self.is_alive():
            return self.name
        else:
            return ""

    def action(self,opponent):
        num = __import__("random").randint(1,5)
        if num == 1:
            self.boostatk()
        elif num == 2:
            self.boostdef()
        elif num == 3:
            self.boostspd()
        elif num > 3:
            self.attack(opponent)
        self.getstats()
        if self.is_alive() == False:
            return False
        return not opponent.action(self)

    def is_alive(self):
        return self.hp >= 0

    def attack(self,opponent):
        opponent.takedmg(self.atk)

    def takedmg(self,dmg):
        num = __import__("random").randint(1,100)
        if num in list(range(1,self.spd + 1)):
            pass
        else:
            self.hp -= dmg - self.de / 100 * dmg


    def boostatk(self):
        self.atk += 2
        self.de -= 1
        self.spd -= 1

    def boostdef(self):
        self.atk -= 1
        self.de += 2
        self.spd -= 1

    def boostspd(self):
        self.atk -= 1
        self.de -= 1
        self.spd += 2

    def getstats(self):
        hp = str(self.hp)
        print(hp)
        print("Name: {}\nHp: {}\nAtk: {}\nDef: {}\nSpd: {}\n".format(self.name,hp[0:3],self.atk,self.de,self.spd))

def fight(bot1,bot2):
    while bot1.is_alive() and bot2.is_alive():
        bot1.action()
        if bot2.is_alive() == False:
            break
        bot2.action()
    print(bot1.livename() + bot2.livename() + " wins!")

fight(bot("Bob"),bot("Joe"))

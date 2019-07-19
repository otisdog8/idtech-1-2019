import sys,random,time
sys.setrecursionlimit(22500)

class bot:
    def __init__(self,name,atk=10,de=10,spd=10,hp=100):
        self.atk = atk
        self.de = de
        self.spd = spd
        self.name = name
        self.hp = hp

    def print(self,text):
        print(text)

    def action(self,opponent):
        time.sleep(1)
        num = random.randint(1,10)
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
        return  self.hp > 0

    def attack(self,opponent):
        self.print("{} Attacks".format(self.name))
        opponent.takedmg(self.atk)

    def takedmg(self,dmg):
        num = random.randint(1,100)
        if num in list(range(1,self.spd + 1)):
            pass
        else:
            self.hp -= dmg - self.de / 100 * dmg
        self.hp = round(self.hp,1)

    def boostatk(self):
        self.print("{} Boosts Attack".format(self.name))
        self.atk += 2
        self.de -= 1
        self.spd -= 1

    def boostdef(self):
        self.print("{} Boosts Defense".format(self.name))
        self.atk -= 1
        self.de += 2
        self.spd -= 1

    def boostspd(self):
        self.print("{} Boosts Speed".format(self.name))
        self.atk -= 1
        self.de -= 1
        self.spd += 2

    def getstats(self):
        print("Name: {}\nHp: {}\nAtk: {}\nDef: {}\nSpd: {}\n".format(self.name,self.hp,self.atk,self.de,self.spd))

class unbeatabot(bot):
    def action(self,opponent):
        time.sleep(1)
        self.attack(opponent)
        self.getstats()
        if self.is_alive() == False:
            return False
        return not opponent.action(self)
class playerbot(bot):
    def intinput(self,query):
        while True:
            try:
                return int(input(query))
                break
            except:
                print("Enter an integer")
    def action(self,opponent):
        num = self.intinput("Bot {}, choose an action. 1 to boost atk, 2 to boost def, 3 to boost spd, and 4 to attack:  ".format(self.name))
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

class autobot(bot):
    def __init__(self,name,atk=10,de=10,spd=10,hp=100):
        self.atk = atk
        self.de = de
        self.spd = spd
        self.name = name
        self.hp = hp
        self.oatk = atk
        self.ode = de
        self.ospd = spd
        self.ohp = hp

    def reset(self):
        self.atk = self.oatk
        self.de = self.ode
        self.spd = self.ospd
        self.hp = self.ohp

    def action(self,opponent):
        num = random.randint(1,10)
        if num == 1:
            self.boostatk()
        elif num == 2:
            self.boostdef()
        elif num == 3:
            self.boostspd()
        elif num > 3:
            self.attack(opponent)
        if self.is_alive() == False:
            return False
        return not opponent.action(self)

    def print(self,text):
        pass

def fightauto(bot1,bot2):
    print([bot1,bot2][int(bot2.action(bot1))].name + " wins!")

def fightplayer(playerbot,autobot):
    print([bot1,bot2][int(bot2.action(bot1))].name + " wins!")

def playervplayer(player1,player2):
    print([bot1,bot2][int(bot2.action(bot1))].name + " wins!")


def fightloop(turns,bot1=autobot("Bob",de=8,spd=6,atk=11),bot2=autobot("Joe")):
    results = [0,0]
    for i in range(turns):
        try:
            results[int(bot2.action(bot1))] += 1
        except:
            pass
        finally:
            bot1.reset()
            bot2.reset()
    print(results)

def defaultsay(query,num):
    inpu = input(query)
    if inpu == "":
        return num
    else:
        return inpu

def intinput(query,num):
    inpu = defaultsay(query,num)
    try:
        while not inpu.isdigit():
            print("Enter an integer")
            inpu = defaultsay(query,num)
    except:
        pass
    return int(inpu)


while True:
    print("Do you want to:\n1. Watch bots play each other\n2. Play a bot\n3. Play another player\n4. Bot V Bot multiple times\n5. Exit")
    choice = intinput("Enter a number: ",5)
    if choice == 5:
        break
    if choice == 1:
        print("Picking stats for bot 1")
        print("Picking stats for bot 2")
        bot2 = bot(name=input("Enter a name: "),atk=intinput("Enter an attack (default 11): ",11),de=intinput("Enter a defense (default 8): ",8),spd=intinput("Enter a speed (default 6):  ",6),hp=intinput("Enter health (default 100):  ",100))
        bot1 = bot(name=input("Enter a name: "),atk=intinput("Enter an attack (default 10): ",10),de=intinput("Enter a defense (default 10): ",10),spd=intinput("Enter a speed (default 10):  ",10),hp=intinput("Enter health (default 100):  ",100))
        if random.randint(1,2) == 1:
            fightauto(bot1,bot2)
        else:
            fightauto(bot2,bot1)
    if choice == 2:
        print("Picking stats for bot player")
        bot1 = unbeatabot(name=input("Enter a name: "),atk=intinput("Enter an attack (default 10): ",10),de=intinput("Enter a defense (default 10): ",10),spd=intinput("Enter a speed (default 10):  ",10),hp=intinput("Enter health (default 100):  ",100))
        print("Picking stats for human player")
        bot2 = playerbot(name=input("Enter a name: "),atk=intinput("Enter an attack (default 10): ",10),de=intinput("Enter a defense (default 10): ",10),spd=intinput("Enter a speed (default 10):  ",10),hp=intinput("Enter health (default 100):  ",100))
        if random.randint(1,2) == 1:
            fightauto(bot2,bot1)
    if choice == 3:
        print("Picking stats for human player 1")
        bot1 = playerbot(name=input("Enter a name: "),atk=intinput("Enter an attack (default 10): ",10),de=intinput("Enter a defense (default 10): ",10),spd=intinput("Enter a speed (default 10):  ",10),hp=intinput("Enter health (default 100):  ",100))
        print("Picking stats for human player 2")
        bot2 = playerbot(name=input("Enter a name: "),atk=intinput("Enter an attack (default 10): ",10),de=intinput("Enter a defense (default 10): ",10),spd=intinput("Enter a speed (default 10):  ",10),hp=intinput("Enter health (default 100):  ",100))
        if random.randint(1,2) == 1:
            fightauto(bot1,bot2)
        else:
            fightauto(bot2,bot1)
    if choice == 4:
        print("Picking stats for bot 1")
        bot1 = autobot(name=input("Enter a name: "),atk=intinput("Enter an attack (default 11): ",11),de=intinput("Enter a defense (default 8): ",8),spd=intinput("Enter a speed (default 6):  ",6),hp=intinput("Enter health (default 100):  ",100))
        print("Picking stats for bot 2")
        bot2 = autobot(name=input("Enter a name: "),atk=intinput("Enter an attack (default 10): ",10),de=intinput("Enter a defense (default 10): ",10),spd=intinput("Enter a speed (default 10):  ",10),hp=intinput("Enter health (default 100):  ",100))
        fightloop(intinput("Enter how many rounds you want (default 100):  ",100),bot1=bot1,bot2=bot2)

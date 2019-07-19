import random

def pointget(pig1,pig2):
    scores = [0,0,0,5,5,10,15]
    pigs = [pig1,pig2]
    score = 0
    pigs.sort()
    if pigs in [[1,1],[2,2]]:
        score += 5
    pig1 = scores[pig1]
    pig2 = scores[pig2]
    if pig1 == pig2:
        score += pig1*4
    else:
        score += pig1 + pig2
    return score

def getpigscore():
    num = random.randint(1,10000)
    sum = 0
    weights = [3490,3029,2240,880,300,61]
    for i in weights:
        sum += i
        if sum >= num:
            return weights.index(i) + 1


data,pointsgotten = [],[0]
print("How to play Pig game:\nFirst, choose how many players will play the game. 1 player is solo.\nOnce play begins, you have 2 options\ns to stop rolling, and anything else to continue\nFirst to 100 wins!")
for i in range(int(input("How many players do you want?  "))): data.append(0)
while True:
    for i in range(len(data)):
        pointsgotten[0] = 0
        print(int(data[i] != -1)*"Player {}'s turn".format(str(i + 1)))
        while True:
            if data[i] == -1:
                break
            if input("Choose your action ") == "s":
                break
            else:
                data.append(pointget(getpigscore(),getpigscore()))
                if data[len(data)-1] == 0:
                    pointsgotten[0] = 0
                    data.pop(len(data)-1)
                    break
                else:
                    pointsgotten[0] += data[len(data)-1]
                print("You got {} points, and your total points for this round is {}".format(str(data[::-1][0]),str(pointsgotten[0])))
                data.pop(len(data)-1)
        data[i] += pointsgotten[0]
        print(int(data[i] != -1)*"Your total points are {}".format(str(data[i])))
        if data[i] >= 100:
            print("Player {} has won!".format(i+1))
            data[i] = -1
    if all(i==-1 for i in data):
        break
print("Game ended")

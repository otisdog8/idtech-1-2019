def getpigscore():
    num,sum,weights = __import__("random").randint(1,10000),[0],[3490,3029,2240,880,300,61]
    for i in weights:
        if sum[0] + i + (lambda x: 0)(sum.__setitem__(0,sum.__getitem__(0)+i)) >= num: return weights.index(i) + 1
data,pointsgotten,asdf = [],[0],print("How to play Pig game:\nFirst, choose how many players will play the game. 1 player is solo.\nOnce play begins, you have 2 options\nPress 's' to stop rolling, and anything else to continue\nFirst to 100 wins!")
for i in range(int(input("How many players do you want?  "))): data.append(0)
while True:
    for i in range(len(data)):
        pointsgotten[0] = (lambda x: 0)(print(int(data[i] != -1)*"Player {}'s turn".format(str(i + 1))))
        while True:
            if data[i] == -1 or input("Choose your action ") == "s": break
            data.append((lambda pig1,pig2: 5 if [pig1,pig2] in [[1,1],[2,2]] else ([0,0,0,5,5,10,15][pig1]+[0,0,0,5,5,10,15][pig2])*(1 + int(pig1 == pig2)))(getpigscore(),getpigscore()))
            if data[len(data)-1] == 0:
                pointsgotten[0] = (lambda x,y: 0)(data.pop(len(data)-1),print("You got 0 points and so your turn ended"))
                break
            else: pointsgotten[0] += data[len(data)-1]
            print("You got {} points, and your total points for this round is {}".format(str(data[::-1][0]),str(pointsgotten[0])))
            data.pop(len(data)-1)
        data[i] += pointsgotten[0] + (lambda x: 0)(print(int(data[i] != -1)*"Your total points are {}".format(str(data[i] + pointsgotten[0]))))
        if data[i] >= 100: data[i] = (lambda x: -1)(print("Player {} has won!".format(i+1)))
    if all(i==-1 for i in data): break

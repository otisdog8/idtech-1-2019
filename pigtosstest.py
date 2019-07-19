import random
def getpigscore():
    num,sum,weights = __import__("random").randint(1,10000),[0],[3490,3029,2240,880,300,61]
    for i in weights:
        if sum[0] + i + (lambda x: 0)(sum.__setitem__(0,sum.__getitem__(0)+i)) >= num: return weights.index(i)
result = [0,0,0,0,0,0]
for i in range(100000):
    val = getpigscore()
    result[val] += 1

print(result)

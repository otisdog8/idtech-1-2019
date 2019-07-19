import numpy as np
from numpy import random
import matplotlib.pyplot as plt

class Neuron:
    def __init__(self):
        random.seed(1)
        self.weights = initial_weights = 2 * random.random((1,1)) + 1

    def tanhd(self,x):
        return 1 -  np.tanh(x) ** 2

    def step(self,x):
        dotproduct = np.dot(x, self.weights)
        return np.tanh(dotproduct)

    def train(self,iterations,train_inputs,train_outputs):
        for i in range(iterations):
            output = self.step(train_inputs)
            error = train_outputs - output
            ajustment = np.dot(train_inputs.T,self.tanhd(output)*error)
            self.weights += ajustment

def double(x):
    return x * 100

x = [i/100 for i in range(300)]
y = [double(i/100) for i in range(300)]
data = []
for i in range(300):
    data.append(double(i/100) + random.randint(1,100)/50)

x = np.asarray([x])/100
y = np.asarray([y])/100

neuron = Neuron()
print(x)
print(y)
x = x.reshape(300,1)
y = y.T
neuron.train(1000000, x, y)
constant = neuron.weights[0][0]
print(constant)
test_data = [ ]
for i in x:
    test_data.append(i *100* constant)
plt.plot(data, "bo")
plt.plot(test_data, "r-")
plt.show()

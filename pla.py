import math
import random
import numpy as np


def generate_target_func(number_of_runs):
    slope = []
    b = []
    for i in range(number_of_runs):
        for j in range(4):
            x1 = random.uniform(-1,1)
            x2 = random.uniform(-1,1)
            y1 = random.uniform(-1, 1)
            y2 = random.uniform(-1, 1)
        slope.append((y2-y1)/(x2-x1))
        b.append(y1 - (y2-y1)/(x2-x1)*x1)
    return slope, b

def classify_a_point(slope, b):
        random_1 = random.uniform(-1,1)
        random_2 = random.uniform(-1,1)
        if (slope * random_1 + b > random_2):
            return random_1, random_2, -1
        elif (slope * random_1 + b < random_2):
            return random_1, random_2,1
        else:
            return random_1, random_2,0


sample_size = 10;
number_of_runs = 3
t1, t2 = generate_target_func(number_of_runs)
#print(t1)
training = [0] * sample_size
temp = [0]

while(training.count(0) >= 1 or training.count(-1) == sample_size or training.count(1) == sample_size):
    for i in range(sample_size):
        training[i] = [0] * 3

        temp = classify_a_point(t1[0], t2[0])
        #print(temp)
        training[i] = temp

training = np.asmatrix(training)
#print(training[:,2])
#print(training[2][:])

Wn = np.asmatrix([[0] * sample_size] * 2)
print(Wn)
Xn = training[:, 0:2].transpose()
Yn_out = []
missclassified_pt = []
print(Wn[:,0].transpose().shape)
print(Xn[:,0].shape)
print(training[0,2])

for i in range(sample_size):
    Yn_out.append(np.dot(Wn[:,i].transpose(), Xn[:,i]))
    if Yn_out[i] != training[i,2]:
        print(Xn[:,i])
        missclassified_pt.append(training[i, 0:2])
    #print(np.dot(Wn[:,i].transpose(), Xn[:,i]))


random_index = random.randint(0,len(missclassified_pt)-1)
random_wrong_pt = missclassified_pt[random_index]
print(random_wrong_pt)
print("new weights")

Wn[:,random_index] = Wn[:,random_index].transpose() + training[random_index,2] * training[random_index, 0:2]
print(Wn[:,random_index])
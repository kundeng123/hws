import math
import random
import numpy as np
import cvxopt
from pla import  generate_target_func, classify_a_point

sample_size = 10
t1, t2 = generate_target_func(1)
training = [0] * sample_size

while(training.count(0) >= 1 or training.count(-1) == sample_size or training.count(1) == sample_size):
    for i in range(sample_size):
        training[i] = [0] * 3

        temp = classify_a_point(t1[0], t2[0])
        #print(temp)
        training[i] = temp

training = np.asmatrix(training)

print(training)




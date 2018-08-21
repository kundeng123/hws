import numpy as np
import panda as pd
import math
#import cvxopt
import scipy
#from svmutil import *

#from svmutil import *


def read_data(fileloc):

    data = pd.read_table(fileloc,header = None,delim_whitespace=True)
    return data


def get_weights(z_vector_input, y_vector_input):
    pseudo_inverse = np.dot(np.linalg.inv(np.dot(np.transpose(z_vector_input),z_vector_input)),np.transpose(z_vector_input))
    return np.dot(pseudo_inverse, y_vector_input)


training = read_data('HW6-in.dta').values
testing = read_data('HW6-out.dta').values

x1_vector = training[:24,0]
x2_vector = training[:24,1]
y_vector = training[:24,2]
z_vector = np.column_stack((np.ones(len(x1_vector)),x1_vector,x2_vector,x1_vector*x1_vector,x2_vector*x2_vector,
                           x1_vector*x2_vector,abs(x1_vector-x2_vector),abs(x1_vector+x2_vector)))
z_vector_3 = np.column_stack((np.ones(len(x1_vector)),x1_vector,x2_vector,x1_vector*x1_vector,x2_vector*x2_vector
                              , x1_vector*x2_vector,abs(x1_vector-x2_vector),abs(x1_vector+x2_vector)))

weights_3 = get_weights(z_vector_3, y_vector)

print(weights_3)


val_x1_vector = training[25:,0]
val_x2_vector = training[25:,1]
val_y_vector = training[25:,2]

# ,
#                                   val_x2_vector*val_x2_vector, val_x1_vector*val_x2_vector,
#                                   abs(val_x1_vector-val_x2_vector), abs(val_x1_vector+val_x2_vector)

val_z_vector_3 = np.column_stack((np.ones(len(val_x1_vector)),val_x1_vector,val_x2_vector,val_x1_vector*val_x1_vector
                                  ,val_x2_vector*val_x2_vector, val_x1_vector*val_x2_vector
                                  ,abs(val_x1_vector-val_x2_vector), abs(val_x1_vector+val_x2_vector)))

val_3_output = np.dot(weights_3.transpose(),val_z_vector_3.transpose())

print(val_3_output)
print(val_y_vector)

count = 0;
for i in range(len(val_y_vector)):
    if np.sign(val_y_vector[i]) != np.sign(val_3_output[i]):
        count = count + 1
print(count/len(val_y_vector))

# ,testing[:,1]*testing[:,1],
#  testing[:, 0]*testing[:,1],abs(testing[:,0]-testing[:,1]),abs(testing[:,0]+testing[:,1])

z_vector_testing = np.column_stack((np.ones(len(testing[:,0])),testing[:,0],testing[:,1],testing[:,0]*testing[:,0]
                                    , testing[:, 1] * testing[:, 1], testing[:, 0]*testing[:,1]
                                    , abs(testing[:, 0] - testing[:, 1]),abs(testing[:,0]+testing[:,1])))

testing_y_vector = testing[:,2]
testing_output = np.dot(weights_3.transpose(),z_vector_testing.transpose())

out_of_sample_count = 0
for i in range(len(testing_y_vector)):
    if np.sign(testing_y_vector[i]) != np.sign(testing_output[i]):
        count = count + 1
print(count/len(testing_y_vector))


print(math.sqrt(np.dot(abs((testing_y_vector - testing_output)).transpose(),abs((testing_y_vector - testing_output)))))

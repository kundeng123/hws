
import numpy as np
import pandas as pd

def read_data(fileloc):

    data = pd.read_table(fileloc,header = None,delim_whitespace=True)
    return data

training = read_data('HW6-in.dta').values
testing = read_data('HW6-out.dta').values

x1_vector = training[:,0]
x2_vector = training[:,1]
y_vector = training[:,2]

z_vector = np.column_stack((np.ones(len(x1_vector)),x1_vector,x2_vector,x1_vector*x1_vector,x2_vector*x2_vector,
                           x1_vector*x2_vector,abs(x1_vector-x2_vector),abs(x1_vector+x2_vector)))

z_vector_testing = np.column_stack((np.ones(len(testing[:,0])),testing[:,0],testing[:,1],testing[:,0]*testing[:,0],testing[:,1]*testing[:,1],
                                    testing[:, 0]*testing[:,1],abs(testing[:,0]-testing[:,1]),abs(testing[:,0]+testing[:,1])))
#print(z_vector)

z_pseudo_inverse = np.dot(np.linalg.inv(np.dot(np.transpose(z_vector),z_vector)),np.transpose(z_vector))
#print(z_pseudo_inverse.shape)
weights = np.dot(z_pseudo_inverse,y_vector)
#print(weights)




training_output = np.dot(weights.transpose(),z_vector.transpose())
#print(y_vector)
#print(training_output)


count = 0;
for i in range(len(y_vector)):
    if np.sign(y_vector[i]) != np.sign(training_output[i]):
        count = count + 1
print(count/len(y_vector))
# print(np.dot(weights.transpose(),z_vector.transpose()))

count = 0;
testing_y_vector = testing[:,2]


testing_output = np.dot(weights.transpose(),z_vector_testing.transpose())
print(testing_output.shape)
for i in range(len(testing_y_vector)):
    if np.sign(testing_y_vector[i]) != np.sign(testing_output[i]):
        count = count + 1
print(count/len(testing_y_vector))

lambda_val = 0.01
lambda_val = 0.1

weights_aug_training = np.dot(np.linalg.inv(np.dot(np.transpose(z_vector),z_vector) +lambda_val*np.identity(8)),
                              np.dot(z_vector.transpose(),y_vector))

print(weights_aug_training)

training_output_aug = np.dot(weights_aug_training.transpose(),z_vector.transpose())
print(y_vector)
print(training_output_aug)


count = 0;
for i in range(len(y_vector)):
    if np.sign(y_vector[i]) != np.sign(training_output_aug[i]):
        count = count + 1
print("weight decay in sample error")
print(count/len(y_vector))


testing_output_aug = np.dot(weights_aug_training.transpose(),z_vector_testing.transpose())
count = 0;
for i in range(len(testing_y_vector)):
    if np.sign(testing_y_vector[i]) != np.sign(testing_output_aug[i]):
        count = count + 1
print("weight decay out of sample error")
print(count/len(testing_y_vector))
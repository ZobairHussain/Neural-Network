import random as ran
import numpy as np
import math
 
n = int(input("Enter the number of input lines: ")) #input layer
h = int(input("Enter the number of nodes in hidden layer: ")) #hidden layer
o = int(input("Enter the number of output lines: ")) #output layer
 
wh = np.random.rand(n, h) #input to hidden edge
uh = np.random.rand(h) #hidden threshold
wo = np.random.rand(h, o) #hidden to output edge
uo = np.random.rand(o) #output threshold
Oaj = np.zeros(h) 
Oak = np.zeros(o)
Err = np.zeros(o)
 
data=[] #total data initialization
train=[] #train test split
test=[]
 
data_len = pow(2,n) #input data are taken for 2^inpur data
for i in range(data_len):
    temp = int(i);
 
    x = []
    for j in range(n): #define class
        x.append(temp%2) 
        temp = int(temp/2) #zeros for class zero, one for 
 
    x.reverse() 
    y = [] #generate x
    
    for j in range(o):
        y.append(x[j]) #insert x to y
 
    pr = (x,y)
    data.append(pr) #insert pair of (x,y) to the data
 
 
train = ran.sample(population = data, k = int((data_len)*.8)) #train test split
 
for i in range(len(data)): #if the data in=s not in train then push it to test
    flag = 0
    for j in range(len(train)):
        if (data[i] == train[j]):
            flag = 1
    if (flag == 0):
        test.append(data[i])

k1 = 1 #initialize some values
k2 = 1
ita1 = 1
ita2 = 1
 
errora = 0  #at first error is 0
 
for li in range(len(train)):
    x = train[li][0]  #take train value to the temporary variable
    t = train[li][1] #take train value to the temporary variable
 
    for j in range(h):
        net = 0
        for i in range(n):
            net = net + wh[i][j]*x[i]  #calculayting net weight
        Oaj[j] = 1.00/(1.00 + math.exp(-k1*activ))  #calculating output
 
    for k in range(o):
        net = 0
        for j in range(h):
            net = net + wo[j][k]*Oaj[j]
        activ = net + uo[k]
        Oak[k] = 1.00/(1.00 + np.exp(-k2*activ))
 
        Err[k] = t[k] - Oak[k]  #calculating error
 
        errora = 0.5*(Err[k]*Err[k]) 
 
    for j in range(h):
        for k in range(o):
            wo[j][k] = wo[j][k] + ita2*k2*Err[k]*Oaj[j]*Oak[k]*(1-Oak[k])  #back propagate
 
    for k in range(o):
        uo[k] = uo[k] + ita2*k2*Err[k]*Oaj[j]*Oak[k]*(1-Oak[k])  ##again calculate output
 
    for j in range(h):    
        for i in range(n):
            e = 0
            for k in range(o):
                e += Err[k]*wo[j][k]  #update threshold th=with the help of back propagate
            wh[i][j] = wh[i][j] + ita1*k1*e*x[i]*Oaj[j]*(1-Oaj[j])
 
            uh[j] += ita1*k1*e*x[i]*Oaj[j]*(1-Oaj[j]) #update threshold
 
 
print("Training Data Error = ", errora) #resulting error
 
errora = 0
 
for li in range(len(test)): #testing
    x = test[li][0] #take data into temporary variables
    t = test[li][1]
 
    for j in range(h):
        net = 0
        for i in range(n):
            net = net + wh[i][j]*x[i] #calculate the net weight
        activ = net + uh[j] #
        Oaj[j] = 1.00/(1.00 + math.exp(-k1*activ)) #mathamtical calculations
 
    for k in range(o):
        net = 0
        for j in range(h):
            net = net + wo[j][k]*Oaj[j]
        activ = net + uo[k]
        Oak[k] = 1.00/(1.00 + np.exp(-k2*activ)) #mathamatical calculation for second layer
 
        Err[k] = t[k] - Oak[k] #calculate i=error
 
        errora = 0.5*(Err[k]*Err[k])
 
    print("Input:        ", x) #print the inputs
    print("Output class: ", t) 3PRINT THE PREDICTED OUTPUTS
 
 
 
print("Testing Data Error = ", errora)
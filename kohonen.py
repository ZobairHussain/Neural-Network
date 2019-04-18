import random as ran
import numpy as np
n=5
o=25
#n = int(input("input lines: "))
#o = int(input("Enter the number of internal nodes: "))
    
data=[] #initialize variable matrixes
train=[]
test=[]

data_len = pow(2,n) #data length is 2^input pattern
 
for i in range(data_len):
    temp = int(i);  #generate data
    
    x = []
    for j in range(n):
        md = temp%2
        if (md == 1):  #data is generated as +1 or 0 for input pattern
            x.append(1)
        else:
            x.append(0) 
        temp = int(temp/2)
    #x.reverse()
    data.append(x)  #data is ready for train test

 
train = ran.sample(population = data, k = int((data_len)*.8)) #train test split

for i in range(len(data)):  #as the data is split in train test manually, so the patterns that are not in train, push them to the test
    flag = 0
    for j in range(len(train)):
        if (data[i] == train[j]):  #generating test data
            flag = 1
    if (flag == 0):
        test.append(data[i]) #test data is generates

w = np.random.rand(n, o)   #weight matrix
Nj = np.random.rand(o) #nearest neighbour matrix

ita = 0.5  #radius of the neighbour
        
for s in range(len(train)):  #training the model
    x = train[s]
    
    disj = []
    for j in range(o):  #distance measure for every node
        dis = 0
        for i in range(n):
            dis = dis + (x[i]-w[i][j])*(x[i]-w[i][j]) #distance is calculated as ucledian distance
        pr = (dis,j)
        disj.append(pr)
        
    def getKey(item):
        return item[0]  #train data is sorted according to the distance of their neighbour
    
    disj = sorted(disj, key=getKey)
    
    mn = disj[0][1]  #distance for every node is saved
    
    sum = 0

    for k in range(len(disj)): #calculate the neighbour of every node according to their distance
        j = disj[k][1]
        dis = disj[k][0]
        
        if i != 0:
            sum = sum+dis  
        
        if sum > Nj[mn]:  #neighbour is generated
            break
        
        for i in range(n):
            w[i][j] = w[i][j] + ita*(x[i]-w[i][j])  #weight matrix calculation for every node
            
        Nj[j] = 0.5*Nj[j]  #update neighbour in every iteration




for s in range(len(test)):  #testing period
    x = test[s]
    
    disj = []
    for j in range(o): #mathamatical calculations for testing
        dis = 0
        for i in range(n):
            dis = dis + (x[i]-w[i][j])*(x[i]-w[i][j]) #sum of weight matrix for testing input pattern
        pr = (dis,j)
        disj.append(pr) #distance is measureed
        
    def getKey(item):
        return item[0] #data is sorted according to their distance
    
    disj = sorted(disj, key=getKey)
    
    mn = disj[0][1] #calculate the neighbour
    
    #print('Unknown pattern = ', x)
    print('Unknown pattern = ', x,' of output node = ', mn)  #print the output pattern
    print()
    #print('Train pattern most similar to that output node = ', trainRep[mn])

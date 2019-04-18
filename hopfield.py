import random as ran
import numpy as np

#n = int(input("Enter the number of input lines: "))
n=8  
data=[]
train=[]
test=[]

data_len = pow(2,n) #data length is 26input k=length
 
for i in range(data_len):
    temp = int(i); #create a dataset where each input is eighter +1 or -1
    
    x = []
    for j in range(n): 
        md = temp%2
        if (md == 1): #for +1 input
            x.append(1)
        else:
            x.append(-1) #for -1 input
        temp = int(temp/2)
    x.reverse()
    data.append(x) #data is created

 
train = ran.sample(population = data, k = int((data_len)*.8))  #train test split

for i in range(len(data)):
    flag = 0
    for j in range(len(train)): #if data in not in tha=e train then push it to the test
        if (data[i] == train[j]):
            flag = 1
    if (flag == 0):
        test.append(data[i]) #test data is generated

m = len(train) #measure train length


w = np.random.rand(n, n) #weight matrix
        
for i in range(n):
    for j in range(n):
        w[i][j] = 0
        if (i != j):
            for s in range(m):
                w[i][j] = w[i][j] + train[s][i]*train[s][j]  #calculated weights


prev = []
        
for s in range(len(test)):  #testing period
    mu = test[s]
    print("Unknown pattern =     ", mu) #for unknow pattern test 

    cnt = 0   
    while 1:
        for i in range(n):
            sum = 0
            for j in range(n):
                sum = sum + w[i][j]*mu[j] #calculate sum of weight matrix
            if sum > 0:
                mu[j] = 1  #calculate the pattern +1 or -1
            else:
                mu[j] = -1
                
        cnt = cnt+1
#        if cnt > 10:
#            break
        prev.append(mu)
        
        if (len(prev) > 5): #if same pattern is coming for 5 times, then it is belived that pattern is stable. so the pattern can be taken as a result
            prev.pop(0)
        
        matched = 1
        for i in range(len(prev)): #if the pattern is unstable, contineu for matching
            if mu != prev[i]:
                matched = 0
            
        if matched == 1:
            break

    print("Transformed pattern = ", mu)  #print the output pattern
    
        
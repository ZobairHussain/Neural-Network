

import random
import numpy as np

while(1):
    n= int(input("Enter the number of input line: "))
    weight=[]
    
    for i in range(n+1):
        w=random.random()
        weight.append(w)
        
    data=[]
    train=[]
    test=[]
    
    data_length = pow(2,n)
    #n= str(n)
    stra= '0'+str(n)+'b'
    for i in range (data_length):
        x=format(i,stra)
    
         
        if (x[0]=='0'):
            y=0
        else:
            y=1
        pair= (x,y)
        data.append(pair)
    
     
    tr = float (data_length)*.8
    train_size = int(tr)
    train = random.sample(population = data, k = train_size)
    
    for i in range(len(data)):
        flag = 0
        for j in range(len(train)):
            if (data[i] == train[j]):
                flag = 1
        if (flag == 0):
            test.append(data[i])
    
    ita = 0.5
    
    #print(train)
    train = data
    i=0;
    cnt=0;
    while(i<len(train)):
        print('iteration:',i,'        trained data is',train[i])
        x=train[i][0]
        weighted_sum=0.0    
        for j in range(n):
            z=float(x[j])
            weighted_sum+=z*weight[j+1]
    
        weighted_sum+=weight[0]
        y = 0
        
        if(weighted_sum>0):
            y=1
        else:
            y=0
        
        if(y==train[i][1]):
            i=i+1       
        else:
            if(y==0 and train[i][1]==1):
                for j in range(len(x)):
                    z=float(x[j])
                    weight[j+1]=weight[j+1]+z*ita
                weight[0] = weight[0]+1.00*ita
            else:
                for j in range(len(x)):
                    z=float(x[j])
                    weight[j+1]=weight[j+1]-ita*z
                weight[0] = weight[0]-1.00*ita 
            i=0
    print("\n\n")
    correct=0
    wrong=0
    weighted_sum = 0.0
    for i in range(data_length-train_size):
        x=test[2][0]
        for j in range(len(x)):
            z=float(x[j])
            weighted_sum+=z*weight[j+1]
        weighted_sum+=weight[0]
            
        if(weighted_sum>0):
            y=1
        else:
            y=0
            
        if(y==test[i][1]):
            correct=correct+1
        print('the tested data is',test[1][0], 'and the class is',test[1][1])
        
        accuracy=correct/len(test)
        
    print("Accuracy is: ",int(accuracy*100),"%")
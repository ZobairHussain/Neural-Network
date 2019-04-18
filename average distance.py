from numpy import array
import math
import matplotlib.pyplot as plt

print("Enter coordinate of class A") #taking coordinates of class A
x1= int(input())
y1= int(input())
a=[[x1,y1]] #insert those values to class A
print("Enter coordinate of class B") #taking coordinates of class B
x2= int(input())
y2= int(input())
b=[[x2,y2]] #insert those coordinates to tha class B

z1=[] 
w1=[]
print("ok")
while True:
    i=0
    print("Enter coordinate for testing") #take a coordinate and classify it
    x3= int(input())
    y3= int(input())
    if x3==0 and y3==0: #if coordinates are 0 then stop the code
        break
    
    for i in range(0,len(a)):    #calculate distance by average distance for class A
        print(z1)
        z1.append(math.sqrt(((a[i][0]-x3)**2 + (a[i][1]-y3)**2)))  
        i=i+1
        print(z1) #print the distances
        
        
    #w= math.sqrt((x2-x3)**2 + (y2-y3)**2)
    for j in range(0,len(b)): #calculate distances for class B
        w1.append(math.sqrt(((b[j][0]-x3)**2 + (b[j][1]-y3)**2)))
        j=j+1
        
    
    z= sum(z1)/len(z1)
    z1.clear()
    
    w= sum(w1)/len(w1)  #calculate sum
    
    w1.clear()
    if z>w:   #if sum is greater then a threshod value, then put the new coordinate to the class B
        b.append([x3,y3])
        print('class B')
    else:
        a.append([x3,y3])
        print('class A')  #otherwise in class A
        
    f = plt.figure() #draw the figure for both classes
    an  = array(a)   
    plt.plot(an[:,0], an[:, 1], '*') #for class a print *(star)
    
    bn  = array(b)   #for class B print .(dot)
    plt.plot(bn[:,0], bn[:, 1], '.')
    plt.show() #repeat the loop
    
    
    
    
    
    
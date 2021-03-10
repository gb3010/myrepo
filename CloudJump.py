#Jump 2 steps if there is 0 if not jump 1 step
def Cloudjump(Arr,jump=0):
    for i in range(len(Arr)-2):
             if Arr[i+2] == 0 and Arr[i] != 1:
                     print("Sensing 0 two steps ahead standing at {p}".format(p=i))
                     i+=2
                     jump+=1
                     print("Now at {x} and jump no. {y}".format(x=i,y=jump))
             else:
                 #print('no',i)
                 if Arr[i] == 0:
                     i+=1
                     jump+=1
    
    if i != len(Arr)-1 and Arr[-1] == 0:
        jump+=1 
    
    return jump
    



k=[0, 1, 0, 0, 1, 0, 0]
z=[0, 1, 0, 0, 0, 1 ,0]
q=[0, 0, 0, 1, 0, 1, 0]
k2=Cloudjump(q)
print(k2)

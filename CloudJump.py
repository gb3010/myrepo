#Jump 2 steps if there is 0 if not jump 1 step
def jumpingOnClouds(c):
    
    i=jump=0
    while i<len(c)-2:
        if c[i+2] == 0:
            jump+=1
            i+=2
        elif c[i+1] == 0:
            jump+=1
            i+=1

    
    if i == len(c)-2 and c[i] == 0 :
        jump+=1

    return jump
    



#k=[0, 1, 0, 0, 1, 0, 0]
#z=[0, 1, 0, 0, 0, 1 ,0]
q=[0, 0, 0, 1, 0, 1, 0]
k2=Cloudjump(q)
print(k2)

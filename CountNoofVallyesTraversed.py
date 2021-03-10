#D being travesal below sea level and U being travesal above sea level, count no. of valleys traversed ( crossing from below sea level )

def countingValleys(steps, path):
    
    UpsAndDowns=[]
    CrossSeaLevel=0
    count=0
    
    for i in path:
        if i == 'D':
            count -=1
        else:
            count +=1
        UpsAndDowns.append(count)

    for i in range(steps-1):
        if UpsAndDowns[i]  == -1 and UpsAndDowns[i+1] == 0:
            CrossSeaLevel+=1

    return CrossSeaLevel

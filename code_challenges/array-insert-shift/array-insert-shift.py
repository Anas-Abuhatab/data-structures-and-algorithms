

def insertShiftArray (list,val):
    
    newArr =[val]
    finall =[]
    finall= list+newArr
    if len(list)%2 == 0:
        position =int(len(list)/2)+1
    else:
        position =int((len(list)+1)/2)
    for i in range(position):
        if i != 0:
            finall[len(finall)-i] ,finall[len(finall)-i-1] =finall[len(finall)-i-1],finall[len(finall)-i]
    return finall

print(insertShiftArray([1,2,3,4,1,2,3,4],1000))
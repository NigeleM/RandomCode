

def main(lists):
    lists=sorted(lists)
    count = 0
    for index,num in enumerate(lists):
        if index == 0:
            count +=1  
        elif num == lists[index-1]+1:
            count +=1    
        else:
            continue
        

    if count == 1:
        return 0
    return count


print(main([100,4,200,1,3,2]))
print(main([0,0,1,2]))
print(main([0,0,0,0]))

    

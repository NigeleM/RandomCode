
# Given an array and a number k that's
# smaller than the length of the array
# rotate the array to the right elements in-place

def rotate(lists,k):
    k_after = k
    hold = 1
    newlist = []
    for i in range(len(lists)):
        if i < k:
            k_after += 1
            if k_after> len(lists)-1:
                k_after -= 1  
                
            hold=lists[k_after]
            lists[k_after] = lists[i]
            lists[i] = hold
            newlist.append(lists[k_after])
            newlist.append(lists[i])
        if i == k:
            if len(newlist) ==  len(lists) - 1:
                kvalue = lists[k]
                lists.pop(lists.index(kvalue))
                lists.append(kvalue)
            else:
                if len(lists) == 2:
                    return lists
                else:
                    kvalue = lists[k]
                    lists.pop(lists.index(kvalue))
                    lists.insert(0,kvalue)

    return lists
# Actual answer
"""n = len(nums)
        k %= n
        
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                
                if start == current:
                    break
            start += 1 """

print(rotate([1,2,3,4,5],2))
print(rotate([1,2,3,4,5,6,7],3))
print(rotate([-1,-100,3,99],2))
print(rotate([1,2,3],1))
print(rotate([1],0))
print(rotate([1,2],0))
print(rotate([1,2],1))


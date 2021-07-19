
import itertools
def permute(nums):
        dataSet = []
        perNum = len(nums)
        permList=list(itertools.permutations([1,2,3,4], perNum))
        for items in permList:
            item = list(items)
            dataSet.append(item)

        return dataSet
            


print(permute([1,2,3,4]))

print(permute(["G","R","L"]))

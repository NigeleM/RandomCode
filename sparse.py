
"""Use a more space-efficient data structure, SparseArray, that implements
the same interface:

init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.
"""

class SparseArray:

    def __init__(self,size):
        self.count = 0
        self.size = size
        self.array = [0] * size

    def set(self,index,value):
        if index > self.size-1:
            print('index is out of range')
        else:
            self.array[index] = value

    def get(self,index,value):
        if index > self.size-1:
            print('index is out of range')
        else:
            return self.array[index] 

    
            
array = SparseArray(10)
print(array.array)
array.set(0,10)
array.set(9,1)
array.set(3,5)
print(array.array)



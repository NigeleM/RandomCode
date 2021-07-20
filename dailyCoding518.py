


"""Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.
Given an array of numbers and a number k, determine if there are three entries
in the array which add up to the specified number k. For example,
given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49."""

# my solution is to use a permutations
import itertools
def main(n,k):
    List=list(itertools.permutations(n, 3))
    for solution in List:
        if k == sum(solution):
            return True

    return False
            
        
        
        
print(main([20, 303, 3, 4, 25],49))
print(main([20, 303, 3, 4, 25],310))
print(main([100, 100, 3, 4, 25],203))
print(main([100, 100, 3, 4, 25],53))
print(main([20, 303, 3, 4, 25],99))


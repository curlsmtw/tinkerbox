from typing import List
#------------------------------------------------
class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for num in nums: # Loops through nums
            if num in hash_table:
                return True # If integer is already in hash_table, then the current integer is a duplicate
            hash_table[num] = True  # If the number is not in the table, it is added. True is a placeholder for numbers that have been seen
        return False

#------------------------------------------------

array1 = [1, 2, 3, 1] # Supposed to return True
array2 = [1, 2, 3, 4] # Supposed to return False
array3 =  [1,1,1,3,3,4,3,2,4,2] # Supposed to return True
array4 = ['a', 'a'] # Edge Case
array5 = [] # Edge Case
sol = Solution()
print(sol.containsDuplicate(array1))
print(sol.containsDuplicate(array2))
print(sol.containsDuplicate(array3))
print(sol.containsDuplicate(array4))
print(sol.containsDuplicate(array5))
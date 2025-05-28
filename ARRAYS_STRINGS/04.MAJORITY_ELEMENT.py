#BRUTE FORCE
def Majority_Element(arr):
    for i in arr:
        if arr.count(i)>len(arr)//2:
            return i


#OPTIMAL 
class Solution(object):
    def majorityElement(self, nums):
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > len(nums) // 2:
                return num        
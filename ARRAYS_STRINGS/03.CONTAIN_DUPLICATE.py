#BRUTE FORCE

class Solution(object):
    def removeDuplicates(self, nums):
        unique = []
        for num in nums:
            if num not in unique:
                unique.append(num)

        # Overwrite nums with the unique elements
        for i in range(len(unique)):
            nums[i] = unique[i]

        return len(unique)

#OPTIMAL 
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 
        i=0 
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1 
                nums[i]=nums[j]
        return i+1      
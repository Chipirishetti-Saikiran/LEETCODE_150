class Solution(object):
    def rotate(self, nums, k):

        n = len(nums)
        k = k % n  # Ensure k is within bounds
        temp = nums[-k:] + nums[:-k]
        for i in range(n):
            nums[i] = temp[i]
      
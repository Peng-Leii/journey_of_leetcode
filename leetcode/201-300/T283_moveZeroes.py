class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        t = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[t] = nums[i]
                t += 1
        nums[t:] = [0]*len(nums[t:])

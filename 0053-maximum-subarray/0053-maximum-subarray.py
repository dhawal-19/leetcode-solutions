class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if not nums: return 0
        currSum,maxSum = 0,nums[0]
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(currSum,maxSum)
        return maxSum
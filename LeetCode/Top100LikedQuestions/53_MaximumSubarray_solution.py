class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        
        max_sum = nums[0]
        _sum = 0
        for i in nums:
            _sum += i
            max_sum = max(max_sum, _sum)
            if _sum < 0: _sum = 0
        return max_sum

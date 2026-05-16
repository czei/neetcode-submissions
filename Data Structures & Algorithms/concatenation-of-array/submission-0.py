class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        arr_len = len(nums)        
        ans = [0] * arr_len * 2

        for i, val in enumerate(nums):
            ans[i] = nums[i]
            ans[i+arr_len] = nums[i]

        return ans
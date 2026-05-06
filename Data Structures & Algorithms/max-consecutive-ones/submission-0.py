class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count = 0
        max_count = 0
        for val in nums:
            if val == 0:
                if count > max_count:
                    max_count = count
                count = 0
            else:
                count += 1
        return max(count, max_count)
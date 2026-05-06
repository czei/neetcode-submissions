class Solution:
    def removeElement(self, nums: List[int], target: int) -> int:

        j = 0
        i = 0
        max_len = len(nums)
        while i < max_len:
            nums[j] = nums[i]
            if nums[i] != target:
                j += 1
            i += 1

        return j
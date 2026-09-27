class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        min_num = nums[0]
        maximum = -1

        for i in range(1, len(nums)):
            if nums[i] > min_num:
                maximum = max(maximum, nums[i] - min_num)
            else:
                min_num = nums[i]

        return maximum
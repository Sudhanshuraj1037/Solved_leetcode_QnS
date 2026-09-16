class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0

        while i < n:
            j = i

            bits = nums[i].bit_count()

            while j < n and nums[j].bit_count() == bits:
                j += 1

            nums[i:j] = sorted(nums[i:j])

            i = j

        return nums == sorted(nums)
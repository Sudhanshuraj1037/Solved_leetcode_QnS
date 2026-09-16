class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        m = min(nums)

        for x in nums:
            if x % m != 0:
                return 1

        count = nums.count(m)

        return (count + 1) // 2
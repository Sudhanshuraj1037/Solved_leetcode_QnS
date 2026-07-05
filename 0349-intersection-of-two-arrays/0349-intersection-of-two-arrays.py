class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashset1 = set(nums1)
        # hashset2 = set(nums2)
        result = set()

        for num in nums2:
            if num in hashset1:
                result.add(num)
            
        return list(result)
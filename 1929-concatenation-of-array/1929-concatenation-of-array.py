class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * (2 * n)

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans
        
        # n=2*len(nums)
        # ans = [0]*n
        # for i in range(len(nums)):
        #     ans[i]=nums[i]
        #     ans[i+len(nums)]=nums[i]
        # # print(nums[i])
            
        #     return ans

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
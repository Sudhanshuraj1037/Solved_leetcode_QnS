class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        collection = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in collection:
                return(collection[complement], i)
                
            collection[nums[i]] = i

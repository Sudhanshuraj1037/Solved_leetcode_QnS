class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [0]*len(nums)
        
        runningSum[0] = nums[0] #Yaha pe 1st element alag se hamdel kar rahe h kyu ki
                                                       # 0 index pe -1 ho jayega [i-1]
        for i in range( 1, len(nums)):
            runningSum[i] = runningSum[i-1] + nums[i]
        
        return runningSum
        

        
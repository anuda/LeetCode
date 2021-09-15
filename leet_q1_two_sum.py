class Solution:
    def __init__(self):
        pass
        
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Runtime: 1656 ms, faster than 40.17% of Python online submissions for Two Sum.
        Memory Usage: 14.4 MB, less than 24.37% of Python online submissions for Two Sum.
        """
        for i,j in enumerate(nums):
            diff = target-j
            if diff in nums[:i]+nums[i+1:]:
                if i!=nums.index(diff):
                    return([i,nums.index(diff)])
                else:
                    nums.remove(j)
                    return([i,nums.index(diff)+1])
            

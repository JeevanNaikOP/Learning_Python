class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind={}
        for i,v in enumerate(nums):
            if(target-v in ind):
                return [ind[target-v],i]
            ind[v]=i    

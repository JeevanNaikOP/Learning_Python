class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        y={}
        count=0
        longest=0
        for i,v in enumerate(s) :
            if v in y and y[v]>=count:
                count=y[v]+1
            else:
                longest=max(longest,i-count+1)
            y[v]=i
        return longest    

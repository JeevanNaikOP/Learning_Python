class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        i=0
        if not strs:
            return ""
        while i<len(strs[0]) and i<len(strs[-1])and strs[0][i]==strs[-1][i]:
            i+=1
        return strs[0][:i]

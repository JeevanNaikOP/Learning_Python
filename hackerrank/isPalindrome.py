class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=0
        z=x
        while z>0:
            y=y*10+z%10
            z=z//10
        if x==y and x>=0 :
            return True
        else:
            return False

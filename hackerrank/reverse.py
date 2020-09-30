class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev=0
        negative=x<0
        x=abs(x)
        while x>0:
            rev=x%10+rev*10
            x=x//10
        if rev>2**31-1:return 0    
        return(rev if(not negative) else -rev)     

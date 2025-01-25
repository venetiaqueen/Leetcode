class Solution(object):
    def isPalindrome(self, x):

        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x_as_str = str(x)
        length = len(x_as_str)
        l=0
        r= length-1

        while l <= r:
            if x_as_str[l] != x_as_str[r]:
                return False
            else:
                l+=1
                r-=1
        return True
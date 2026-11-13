class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = x
        rev = 0

        if a < 0:
            return False

        while a > 0:
             d = a % 10
             rev = rev * 10 + d
             a = a//10
             
        if x == rev:
            return True
            
        else:
            return False
    

        
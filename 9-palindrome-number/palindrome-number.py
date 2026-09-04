class Solution(object):
    def isPalindrome(self, x):
        if x < -2**31 or x>2**31-1:
            return False
        if x < 0:
            return False
        num = str(x)
        num = num[::-1]
        if str(x) == num:
            return True
        
        return False
        
        
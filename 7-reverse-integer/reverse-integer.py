class Solution(object):
    def reverse(self, x):
        sign = 1
        
        if x<0:
            sign = -1
            x = x*-1
        num = str(abs(x))
        num = num[::-1]
        num = int(num)
        num = num*sign

        if num < (-2**31) or num > ((2**31)-1):
            return 0

        return num
        
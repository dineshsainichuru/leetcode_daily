class Solution(object):
    def isPalindrome(self, s):
        new = ""
        for char in s :
            if char.isalnum():
                new = new+char.lower()
        newnew = new[::-1]
        if new == newnew:
            return True
        else:
            return False
        
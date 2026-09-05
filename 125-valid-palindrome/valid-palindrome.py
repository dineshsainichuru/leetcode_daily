class Solution(object):
    def isPalindrome(self, s):
        new = ''.join(char.lower() for char in s if char.isalnum())
        return new[::-1] == new
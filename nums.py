#9. Palindrome Number
#Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x<0):
            return False
        if x!=0 and x%10==0:
            return False
        half=0
        while (x>half):
            half = half*10 + (x%10)
            x//=10
        return x==half or x==(half//10)


#13. Roman to integer
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. Convert roman to int

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        trans = {
            "I":1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        num =0
        s = s.replace("IV","IIII")
        s = s.replace("IX","VIIII")
        s = s.replace("XL","XXXX")
        s = s.replace("XC","LXXXX")
        s = s.replace("CD","CCCC")
        s = s.replace("CM","DCCCC")
        
        for c in s:
            num += trans[c]
        return num


        

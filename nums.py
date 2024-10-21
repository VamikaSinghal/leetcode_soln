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


#Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=0
        c=0
        for n in nums:
            if n==1:
                c+=1
                if c>max:
                    max = c
            else:
                if c>max:
                    max = c
                c=0
        return maxx


#35. Search Insert Position
#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for i in range(len(nums)):
            if target<=nums[i]:
                return i
        
        return len(nums)

#66. Plus one
#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#Increment the large integer by one and return the resulting array of digits.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #last to first
        for i in range(len(digits)-1, -1, -1):
            #if 9, set to 0
            if digits[i]==9:
                digits[i]=0
            else:
                #if not 9
                digits[i] = digits[i]+1
                return digits
        
        #all digits are 9
        return [1]+digits

#69. Sqrt(x)
#Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
#You must not use any built-in exponent function or operator.
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while left<=right :
            mid = (right+left)//2

            if (mid*mid)<x:
                left = mid+1
            elif (mid*mid)>x:
                right= mid-1
            else:
                return mid
            
        return right

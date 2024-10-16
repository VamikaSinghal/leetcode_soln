#217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

#242. Valid Anagram
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        return sorted(s)==sorted(t)

#1. two sums
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        prevMap = {} #value:index
        
        for i,n in enumerate(nums):
            diff = target-n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i
        return

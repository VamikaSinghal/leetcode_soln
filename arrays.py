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
        

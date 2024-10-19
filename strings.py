#14. Longest Common Prefix
#Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0]

        for str in strs[1:]:
            while str.find(prefix)!=0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

#58. length of last string
#Given a string s consisting of words and spaces, return the length of the last word in the string.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        return len(words[-1])
        
#28. Find the Index of the First Occurrence in a String
#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (haystack==needle):
            return 0
        n,m = len(needle),len(haystack)
        hay=haystack[0:n]

        for i in range(n,m+1):
            if hay==needle:
                return i-n
            if i<m: 
                hay = hay[1:]+haystack[i]
        return -1

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

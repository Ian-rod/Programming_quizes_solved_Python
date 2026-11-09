"""
Longest Palindromic Substring
Medium
Topics
Company Tags
Hints
Given a string s, return the longest substring of s that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.

Example 1:

Input: s = "ababd"

Output: "bab"
Explanation: Both "aba" and "bab" are valid answers.

Example 2:

Input: s = "abbc"

Output: "bb"
Constraints:

1 <= s.length <= 1000
s contains only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        retPalindrome=""
        substrings = [
            s[i:j] 
            for i in range(len(s)) 
            for j in range(i + 1, len(s) + 1)  
            if s[i:j] == s[i:j][::-1]
            ]
        for s in substrings:
            if(len(s)>len(retPalindrome)):
                retPalindrome=s
        return retPalindrome

myObj=Solution()
print(myObj.longestPalindrome("abbcccbbbcaaccbababcbcabca"))
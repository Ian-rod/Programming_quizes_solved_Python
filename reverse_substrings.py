"""
Reverse Substrings Between Each Pair of Parentheses
Medium
Topics
Company Tags
The string s contains lowercase English letters and balanced parentheses. Reverse the characters inside each matching pair of parentheses, processing inner pairs before outer pairs. Remove every parenthesis and return the resulting string. Letters outside all parentheses keep their relative positions.

Example 1:

Input: s = "a(bc)d"

Output: "acbd"
Explanation: Reverse bc to cb. The outer letters a and d stay in place, producing acbd.

Example 2:

Input: s = "(a(bc)d)"

Output: "dbca"
Explanation: First reverse bc to cb, leaving (acbd). Reversing the outer group gives dbca.

Example 3:

Input: s = "()"

Output: ""
Explanation: There are no letters inside the pair, so removing the parentheses leaves an empty string.

Constraints:

1 <= s.length <= 2000
s contains only lowercase English letters and parentheses.

"""

import re
class Solution:
    def reverseParentheses(self, s: str) -> str:
        pattern = r"\(\w*\)"
        while re.search(pattern,s):
            res=re.search(pattern,s)
            repstr=res.group().replace("(", "").replace(")", "") 
            s=s.replace(res.group(),repstr[::-1])
        return s

mySolution=Solution()
print(mySolution.reverseParentheses("()"))
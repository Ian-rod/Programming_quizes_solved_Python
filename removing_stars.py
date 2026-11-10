"""
Removing Stars From a String
Medium
Topics
Company Tags
Each * in s removes itself and the closest remaining letter to its left. Continue until no stars remain and return the resulting string. The input guarantees that every removal is possible, and the result does not depend on the order in which you perform the removals.

Example 1:

Input: s = "a"

Output: "a"
Explanation: There are no stars, so the string stays "a".

Example 2:

Input: s = "abc"

Output: "abc"
Explanation: There are no stars, so all three letters remain.

Example 3:

Input: s = "a*"

Output: ""
Explanation: The star removes the "a" immediately to its left, and the star itself is also removed. Nothing remains.

Constraints:

1 <= s.length <= 100000
Only lowercase English letters and * occur. Every star has an available letter to remove.

"""

class Solution:
    def removeStars(self, s: str) -> str:
        while "*" in s:
            index=s.index("*")
            substr=s[index-1:index+1]
            s=s.replace(substr,"")
        return s

myObJ= Solution()
print(myObJ.removeStars("abc"))
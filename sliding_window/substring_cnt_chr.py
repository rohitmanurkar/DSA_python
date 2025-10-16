"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
"""

#better approach
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = {i: -1 for i in range(3)}
        cnt = 0
        n = len(s)
        for r in range(n):
            d[ord(s[r]) - ord('a')] = r
            if (d[0]!= -1 and d[0]!= -1 and d[0]!= -1):
                cnt =cnt +(1 + min(d[0],d[1],d[2]))
        
        return cnt
        

#brute force
class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        n = len(s)
        count =0
        

        for i in range (n):
          d = {'a': 0, 'b': 0, 'c': 0}
          for j in range (i,n):
                d[s[j]] += 1
                if all(d[c] > 0 for c in 'abc'):
                    count = count +(n-j)
                    break
        return count

        
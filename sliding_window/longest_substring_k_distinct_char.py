"""
Given a string s and an integer k.Find the length of the longest substring with at most k distinct characters.


Examples:
Input : s = "aababbcaacc" , k = 2

Output : 6

Explanation : The longest substring with at most two distinct characters is "aababb".

The length of the string 6.

Input : s = "abcddefg" , k = 3

Output : 4

Explanation : The longest substring with at most three distinct characters is "bcdd".

The length of the string 4.
"""

class Solution:
    def kDistinctChar(self, s, k):
        #your code goes here
        maxLen = 0
        l = 0
        r = 0
        n = len(s)
        d = {}

        while r < n:
            if s[r] in d:
             d[s[r]] += 1
            else:
                d[s[r]] = 1

            if(len(d) > k):
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1
            
            if(len(d)<=k):
                maxLen = max(maxLen, ((r-l)+1))
            r += 1
        return maxLen
            
s = Solution()
print(s.kDistinctChar("aababbcaacc", 2))

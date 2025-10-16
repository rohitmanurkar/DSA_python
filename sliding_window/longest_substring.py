"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left =0
        longest = 0
        sett = set()
        n = len(s)
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[left])
                left += 1

            window = (r - left)+1
            longest = max(longest, window)
            sett.add(s[r])
      
        return longest

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        max_len = 0
        zero = 0
        n = len(nums)
        while r < n:
            if nums[r] == 0:
                zero += 1
            if zero > k:
                if nums[l] == 0:
                    zero -= 1
                l += 1
            if zero <= k:
                leng = (r-l) + 1
                max_len = max(max_len, leng)
            r += 1
            
        return max_len
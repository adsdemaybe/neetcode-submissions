class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_str = ""
        max_len = 0
        l = 0
        r = 0
        while l <= r and r < len(s):
            print(curr_str)
            curr_str = s[l:r]
            if (s[r] in curr_str):
                l += 1
            else:
                r += 1
                max_len = max(len(s[l:r]), max_len)
        
        return max_len
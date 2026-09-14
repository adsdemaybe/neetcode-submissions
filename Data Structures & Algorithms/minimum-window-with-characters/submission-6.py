from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        window = {}

        pres = 0
        req = len(count_t)

        best = 10000000
        best_substr = ""

        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in count_t and window[char] == count_t[char]:
                pres += 1

            while pres == req:
                if (r - l + 1) < best:
                    best = r - l + 1
                    best_substr = s[l : r + 1]

                left_char = s[l]
                window[left_char] -= 1
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    pres -= 1
                l += 1

        return best_substr
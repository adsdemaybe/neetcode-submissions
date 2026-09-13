class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        target_counts = {}
        window_counts = {}

        for ch in t:
            target_counts[ch] = target_counts.get(ch, 0) + 1

        have = 0
        need = len(target_counts)

        best_range = (-1, -1)
        best_len = float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1

            while have == need:
                cur_len = right - left + 1
                if cur_len < best_len:
                    best_len = cur_len
                    best_range = (left, right)

                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    have -= 1
                left += 1

        l, r = best_range
        return s[l : r + 1] if best_len != float("inf") else ""
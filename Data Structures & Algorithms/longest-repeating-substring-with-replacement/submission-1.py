class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = {}
        best = 0 # count that is most frequented
        best_len = 0

        for r in range(len(s)):
            # s[r] is the letter currently
            counts[s[r]] = counts.get(s[r], 0) + 1
            best = max(best, counts[s[r]])

            while((r - l + 1) > best + k):
                counts[s[l]] -= 1
                l += 1
            
            best_len = max(best_len, r-l+1)

        return best_len
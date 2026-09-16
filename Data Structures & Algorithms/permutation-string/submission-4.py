from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        need_counts = dict(Counter(s1))
        have_counts = dict(Counter(s2[0:size]))

        if have_counts == need_counts:
            return True

        for i in range(size, len(s2)):
            # add ith count
            # remove ith-size count

            # counts[s[r]] = counts.get(s[r], 0) + 1
            have_counts[s2[i]] = have_counts.get(s2[i], 0) + 1
            have_counts[s2[i-size]] -= 1
            if have_counts[s2[i-size]] == 0:
                del have_counts[s2[i-size]]

            if have_counts == need_counts:
                return True
        
        return False



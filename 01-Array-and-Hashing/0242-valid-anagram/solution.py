class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False
        # Use a fixed-size list for lowercase letters
        freq = [0] * 26
        base = ord('a')
        for ch in s:
            freq[ord(ch) - base] += 1
        for ch in t:
            idx = ord(ch) - base
            freq[idx] -= 1
            if freq[idx] < 0:
                return False  # early exit
        # All counts should be zero
        return all(v == 0 for v in freq)

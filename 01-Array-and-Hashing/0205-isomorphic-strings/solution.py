class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Quick length check (optional, constraints guarantee equal length)
        if len(s) != len(t):
            return False
        map_s_to_t = {}
        map_t_to_s = {}
        for c1, c2 in zip(s, t):
            # Check forward mapping
            if c1 in map_s_to_t:
                if map_s_to_t[c1] != c2:
                    return False
            else:
                map_s_to_t[c1] = c2
            # Check reverse mapping
            if c2 in map_t_to_s:
                if map_t_to_s[c2] != c1:
                    return False
            else:
                map_t_to_s[c2] = c1
        return True

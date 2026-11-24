class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary mapping the canonical key to list of anagrams
        groups = {}
        for s in strs:
            # Canonical key: sorted characters of the string
            key = ''.join(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        # Return the grouped anagrams as a list of lists
        return list(groups.values())

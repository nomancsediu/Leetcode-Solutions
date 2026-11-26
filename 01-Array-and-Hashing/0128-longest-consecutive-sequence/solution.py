class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge case: empty list
        if not nums:
            return 0
        num_set = set(nums)  # O(n) space for hash set
        max_len = 0
        for num in num_set:
            # Only start counting if 'num' is the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                cur_len = 1
                # Expand forward while consecutive numbers exist
                while current + 1 in num_set:
                    current += 1
                    cur_len += 1
                max_len = max(max_len, cur_len)
        return max_len

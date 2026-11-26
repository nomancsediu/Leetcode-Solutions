class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hashmap stores prefix sum -> frequency
        prefix_counts = {0: 1}
        prefix = 0
        result = 0
        for num in nums:
            prefix += num
            # needed prefix sum that would make current subarray sum to k
            need = prefix - k
            result += prefix_counts.get(need, 0)
            # record current prefix sum
            prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1
        return result

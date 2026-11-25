class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        # 2. Create buckets: index = frequency
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        # 3. Gather top k elements from high freq to low
        res = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

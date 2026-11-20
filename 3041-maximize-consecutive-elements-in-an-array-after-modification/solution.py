class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        # each element v can be used as v or v+1 -> interval [v, v+1]
        intervals = sorted(nums)  # left endpoints
        n = len(intervals)
        i = 0  # index in intervals
        if n == 0:
            return 0
        import heapq
        heap = []  # stores right endpoints (v+1)
        cur = intervals[0]  # start from the smallest possible value
        cur_len = 0
        max_len = 0
        while i < n or heap:
            # add all intervals whose left <= cur
            while i < n and intervals[i] <= cur:
                heapq.heappush(heap, intervals[i] + 1)
                i += 1
            # discard intervals that cannot cover cur
            while heap and heap[0] < cur:
                heapq.heappop(heap)
            if heap:
                # assign cur to the interval with smallest right endpoint
                heapq.heappop(heap)
                cur_len += 1
                max_len = max(max_len, cur_len)
                cur += 1
            else:
                # cannot extend current block, start a new one
                if i >= n:
                    break
                cur_len = 0
                cur = intervals[i]
                heap.clear()
        return max_len

# The method name follows the problem statement; if LeetCode expects a different name,
# rename accordingly (e.g., def maximumElements(self, nums: List[int]) -> int).

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR accumulator; cancels out numbers appearing twice
        result = 0
        for num in nums:
            result ^= num
        return result

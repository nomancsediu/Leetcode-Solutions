class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n is the length of the array; the full range is 0..n inclusive
        n = len(nums)
        # Expected sum of 0..n using Gauss formula
        expected_sum = n * (n + 1) // 2
        # Actual sum of the given numbers
        actual_sum = sum(nums)
        # The difference is the missing number
        return expected_sum - actual_sum

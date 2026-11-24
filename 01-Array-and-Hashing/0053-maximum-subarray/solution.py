class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize current and global maximum with the first element
        current_sum = max_sum = nums[0]
        # Iterate over the rest of the array
        for num in nums[1:]:
            # Either extend the previous subarray or start a new one at current index
            current_sum = max(num, current_sum + num)
            # Update global maximum if needed
            max_sum = max(max_sum, current_sum)
        return max_sum

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # First pass: mark presence by negating the value at the corresponding index
        for num in nums:
            idx = abs(num) - 1  # target index for the value num
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        # Second pass: collect indices that remain positive
        result = []
        for i, val in enumerate(nums):
            if val > 0:
                result.append(i + 1)
        return result

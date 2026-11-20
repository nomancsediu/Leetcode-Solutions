class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # dictionary to store number -> its index
        seen: dict[int, int] = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        # According to problem constraints this line is never reached
        raise ValueError("No two sum solution found")

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Do not return anything, modify nums in-place."""
        write = 0
        # First pass: bring all non‑zero elements forward
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
        # Second pass: fill the rest with zeros
        for i in range(write, len(nums)):
            nums[i] = 0

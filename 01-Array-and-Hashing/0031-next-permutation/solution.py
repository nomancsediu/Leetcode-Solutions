class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """Modify nums in‑place to the next lexicographic permutation."""
        n = len(nums)
        # 1. find pivot i
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            # 2. find rightmost successor j
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # 3. swap pivot and successor
            nums[i], nums[j] = nums[j], nums[i]
        # 4. reverse suffix i+1 .. end
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

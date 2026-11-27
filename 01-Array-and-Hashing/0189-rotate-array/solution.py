class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """Rotate nums to the right by k steps in‑place.
        Modifies nums directly and returns None.
        """
        n = len(nums)
        if n == 0:
            return
        k %= n  # effective rotations
        if k == 0:
            return
        # helper to reverse a sub‑array [l, r]
        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        # step 1: reverse whole array
        reverse(0, n - 1)
        # step 2: reverse first k elements
        reverse(0, k - 1)
        # step 3: reverse remaining n‑k elements
        reverse(k, n - 1)

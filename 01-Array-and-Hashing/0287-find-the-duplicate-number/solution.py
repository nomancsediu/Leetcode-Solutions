class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Phase 1: Find intersection point of two runners.
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # Phase 2: Find entrance to the cycle.
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

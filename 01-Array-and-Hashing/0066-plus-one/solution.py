class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # start with a carry of 1 because we need to add one
        carry = 1
        n = len(digits)
        # process digits from least significant to most significant
        for i in range(n - 1, -1, -1):
            if carry == 0:
                break
            total = digits[i] + carry
            digits[i] = total % 10
            carry = total // 10
        # if we still have a carry, insert it at the front
        if carry:
            digits.insert(0, carry)
        return digits

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        # XOR of all numbers = unique1 ^ unique2
        for num in nums:
            xor ^= num

        # Get a bit where the two unique numbers differ
        diff = xor & -xor

        a = 0
        b = 0

        # Divide numbers into two groups
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num

        return [a, b]
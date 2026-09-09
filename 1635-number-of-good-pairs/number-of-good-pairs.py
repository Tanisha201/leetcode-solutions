class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPair = 0
        freq = {}

        for num in nums:
            if num in freq:
                goodPair += freq[num]

            freq[num] = freq.get(num, 0) + 1

        return goodPair
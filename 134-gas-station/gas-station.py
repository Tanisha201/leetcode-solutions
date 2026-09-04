class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        current_gas = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]

            total_gas += diff
            current_gas += diff

            # Cannot reach next station from current start
            if current_gas < 0:
                start = i + 1
                current_gas = 0

        # Total gas is not enough for the complete circuit
        if total_gas < 0:
            return -1

        return start
class Solution {
public:
    int majorityElement(vector<int>& nums) {

        unordered_map<int, int> seen;

        for (int num : nums) {

            seen[num]++;

            if (seen[num] > nums.size() / 2) {
                return num;
            }
        }

        return 0;
    }
};
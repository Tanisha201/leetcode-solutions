class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        unordered_map<int,int> seen;
        int pairs =0;

        for (int num : nums){
            pairs+=seen[num];
            seen[num]++;
        }
        return pairs;
    }
};
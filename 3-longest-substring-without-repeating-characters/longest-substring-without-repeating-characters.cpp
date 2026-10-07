class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        unordered_map<char, int> seen;

        int left = 0;
        int ans = 0;

        for (int right = 0; right < s.length(); right++) {

            if (seen.find(s[right]) != seen.end()) {
                left = max(left, seen[s[right]] + 1);
            }

            seen[s[right]] = right;

            ans = max(ans, right - left + 1);
        }

        return ans;
    }
};
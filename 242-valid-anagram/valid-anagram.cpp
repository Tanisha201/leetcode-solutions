class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }
        unordered_map<char,int> seen;

        for (char c : s) {
            seen[c]++;
        }
        for (char c : t) {
            seen[c]--;
        }
        for (auto x : seen){
            if (x.second != 0){
                return false;
            }
        }
        return true;
    }
};
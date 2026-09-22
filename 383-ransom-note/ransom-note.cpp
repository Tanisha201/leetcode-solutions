class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map <char,int> seen;
        for (char c : magazine){
            seen[c]++;
        }
        for (char c : ransomNote){
            seen[c]--;
        }
        for (auto x : seen){
            if (x.second < 0){
                return false;
            }
        }
        return true;
    }
};
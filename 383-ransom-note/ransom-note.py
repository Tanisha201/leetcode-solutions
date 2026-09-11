class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen = {}

        for i in range(len(magazine)):
            seen[magazine[i]] = seen.get(magazine[i], 0) + 1

        for i in range(len(ransomNote)):
            if ransomNote[i] not in seen or seen[ransomNote[i]] == 0:
                return False

            seen[ransomNote[i]] -= 1

        return True


            
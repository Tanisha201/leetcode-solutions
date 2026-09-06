class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:

        def match(word1, word2):
            count = 0

            for i in range(6):
                if word1[i] == word2[i]:
                    count += 1

            return count

        while words:

            best_word = None
            min_max_group = float('inf')

            for word1 in words:
                groups = [0] * 7

                for word2 in words:
                    if word1 != word2:
                        groups[match(word1, word2)] += 1

                max_group = max(groups)

                if max_group < min_max_group:
                    min_max_group = max_group
                    best_word = word1

            matches = master.guess(best_word)

            if matches == 6:
                return

            words = [
                word for word in words
                if match(best_word, word) == matches
            ]
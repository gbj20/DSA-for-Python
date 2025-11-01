from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0  # endWord must be in the wordList

        queue = deque([(beginWord, 1)])  # (current_word, level)

        while queue:
            word, steps = queue.popleft()

            # If we reach the endWord, return the number of steps
            if word == endWord:
                return steps

            # Try changing each character in the word
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordSet:
                        wordSet.remove(new_word)  # mark as visited
                        queue.append((new_word, steps + 1))

        return 0  # no possible transformation


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(Solution().ladderLength(beginWord, endWord, wordList))

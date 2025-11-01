from typing import List
from collections import defaultdict, deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # Step 1: BFS to find the shortest distance from beginWord to every reachable word
        layer = {}
        layer[beginWord] = [[beginWord]]  # paths reaching each word

        while layer:
            new_layer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]  # all paths reaching endWord
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet:
                            for path in layer[word]:
                                new_layer[new_word].append(path + [new_word])
            wordSet -= set(new_layer.keys())  # remove visited words
            layer = new_layer

        return []


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(Solution().findLadders(beginWord, endWord, wordList))

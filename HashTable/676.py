# 676. Implement Magic Dictionary
from collections import defaultdict
from typing import List


class MagicDictionary:

    def __init__(self):
        self.a = defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.a[len(word)].add(word)

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        if n not in self.a:
            return False
        for word in self.a[n]:
            k = 0
            for i in range(n):
                if word[i] != searchWord[i]:
                    k += 1
            if k == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

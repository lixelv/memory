from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self, words=None):
        self.children = defaultdict(TrieNode)
        self.words = words or []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]

    def insert_word_and_index(self, word: tuple | list | set):
        node = self.root
        node.words.append(word)

        for char in word[0]:
            if node.children.get(char) is not None:
                node = node.children[char]
                node.words.append(word)
            else:
                break

    def search(self, word):
        node = self.root

        for char in word:
            sub_node = node.children.get(char)
            if sub_node is not None:
                node = sub_node
                if node.words:
                    last_node = node
            else:
                break

        words = last_node.words
        minimal = min(words, key=lambda x: (len(x[0]), x[1]))

        return minimal

    def __str__(self):
        def _display_trie(node, prefix, is_tail):
            lines = []
            children = list(node.children.items())
            for i, (char, child) in enumerate(children):
                connector = "└── " if i == len(children) - 1 else "├── "
                lines.append(f"{prefix}{connector}{char}")
                if child.children:
                    extension = "    " if i == len(children) - 1 else "│   "
                    lines.extend(
                        _display_trie(child, prefix + extension, i == len(children) - 1)
                    )
            return lines

        return "\n".join(_display_trie(self.root, "", True))


class Solution:
    def stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str]
    ) -> List[int]:
        trie = Trie()

        for i in wordsQuery:
            trie.insert(i[::-1])

        for i, j in enumerate(wordsContainer):
            trie.insert_word_and_index((j[::-1], i))

        return [trie.search(i[::-1])[1] for i in wordsQuery], trie


# Пример использования
wordsContainer = ["abcdefgh", "poiuygh", "ghghgh"]
wordsQuery = ["gh", "acbfgh", "acbfegh"]

# trie = Trie()

# for i in wordsQuery:
#     trie.insert(i[::-1])

# for i, j in enumerate(wordsContainer):
#     trie.insert_word_and_index((j[::-1], i))

# print(trie.root.words)
print(*Solution().stringIndices(wordsContainer, wordsQuery), sep="\n")

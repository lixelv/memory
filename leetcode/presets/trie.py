from collections import defaultdict


class TrieNode:
    def __init__(self, words=None):
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]

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

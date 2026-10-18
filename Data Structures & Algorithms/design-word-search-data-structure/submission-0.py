class TrieNode:
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]

        cur.is_end = True
    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.is_end
            
            # pre order dfs
            if word[index] == ".":
                # search all children
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
            if word[index] not in node.children:
                return False

            return dfs(index + 1, node.children[word[index]])
            

        return dfs(0, self.root)

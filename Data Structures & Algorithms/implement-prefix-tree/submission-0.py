class NodeTree:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = NodeTree()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children[c]:
                cur.children[c] = NodeTree()
            cur = cur.children[c]


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children[c]:
                return False
            cur = cur.children[c]
        return cur.end
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children[c]:
                return False
            cur = cur.children[c]
        return True
        
        
        
class TrieNode:

    def __init__(self):
        self.child = [None] * 26
        self.terminator = False

class Trie:

    def __init__(self):
        self.root = self.getNode()

    def charToIndex(self, c):
        return ord(c) - ord("a")

    def getNode(self):
        return TrieNode()
    
    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for i in range(length):
            index = self.charToIndex(key[i])

            if not pCrawl.child[index]:
                pCrawl.child[index] = self.getNode()
            pCrawl = pCrawl.child[index]
        pCrawl.terminator = True


def test():
    keys = ["this", "is", "a", "test"]

    t = Trie()

    for k in keys:
        t.insert(k)
    
    print(t)

test()
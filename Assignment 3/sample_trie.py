class TrieNode:
    def __init__(self):
        self.num = 26
        self.next_node = [None for _ in range(self.num)]
        self.isend = False
        self.base = ord('a')
    def put(self, node, s):
        self.next_node[ord(s)-self.base] = node
    def get(self, s):
        return self.next_node[ord(s)-self.base]
    def contain_key(self, s):
        return self.next_node[ord(s)-self.base] is not None
    def set_end(self):
        self.isend = True
    def if_end(self):
        return self.isend

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        head = self.root
        for i in word:
            if head.contain_key(i):
                head = head.get(i)
            else:
                head.put(TrieNode(), i)
                head = head.get(i)
        head.set_end()


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        head = self.root
        for i in word:
            if not head.contain_key(i):
                return False
            head = head.get(i)
        return head.isend


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        count = 0
        head = self.root
        for i in prefix:
            if not head.contain_key(i):
                return count
            head = head.get(i)
            count += 1
        return count

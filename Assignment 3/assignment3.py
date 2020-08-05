class TrieNode:
    """
    This class implements the node of a Trie
    """
    def __init__(self):
        self.child = [None] * 26
        self.terminator = False


class Trie:
    """
    This class implements the Trie structure
    """
    def __init__(self, text):
        self.root = self.getNode()
        for string in text:
            node = self.root
            for i in range(len(string)):
                index = self.toIndex(string[i])
                if not node.child[index]:
                    node.child[index] = self.getNode()
                node = node.child[index]
            node.terminator = True

    def getNode(self):
        """
        this method returns an TrieNode object
        @param: none
        @return: a TrieNode object
        @time-complexity: O(1)
        @space-complexity: O(1)
        """
        return TrieNode()

    def toIndex(self, c):
        """
        this method converts a character into index number
        @param c: a character
        @return: the index number representing this character
        @time-complexity: O(1)
        @space-complexity: O(1)
        """
        return ord(c) - ord("a")

    def insert(self, string):
        """
        this method inserts a string into the Trie
        @param string: a string for insertion
        @return: none
        @time-complexity: O(n) where n is the length of the string
        @space_complexity: O(n) where n is the length of the string
        """
        node = self.root
        for i in range(len(string)):
            index = self.toIndex(string[i])
            if not node.child[index]:
                node.child[index] = self.getNode()
            node = node.child[index]
        node.terminator = True

    def string_freq(self, query_str):
        """
        this method checks the occurence of a string in the Trie
        @param query_str: the target string
        @return: the occurence of the string
        @time-complexity: O(n) where n is the length of the string
        @space-complexity: O(n) where n is the length of the string
        """
        count = 0
        node = self.root
        for i in range(len(query_str)): 
            index = self.toIndex(query_str[i]) 
            if not node.child[index]: 
                return count 
            node = node.child[index]
            if node.terminator == True:
                count += 1
        return count

    def prefix_freq(self, query_str):
        """
        this method checks the occurence of a string with a specific prefix in the Trie
        @param query_str: the target prefix
        @return: the occurence of the string with the prefix
        @time-complexity: O(n) where n is the length of the string
        @space-complexity: O(n) where n is the length of the string
        """
        count = 0
        node = self.root
        for i in range(len(query_str)): 
            index = self.toIndex(query_str[i]) 
            if not node.child[index]: 
                return count 
            node = node.child[index]
            if node.terminator == True:
                count += 1
        return count
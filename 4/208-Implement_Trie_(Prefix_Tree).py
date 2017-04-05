# coding=utf-8
'''
前缀树
每个节点类型，children存着该节点的孩子，一个节点可以有很多孩子。word表示从跟到该节点组成的字符是不是一个单词。
插入：每个节点插入一个字母。例如插入"word"
'''


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.word = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in word:
            if not node.children.get(i, None):
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in word:
            if not node.children.get(i, None):
                return False
            node = node.children[i]
        return node.word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in prefix:
            if not node.children.get(i, None):
                return False
            node = node.children[i]
        return True



        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)
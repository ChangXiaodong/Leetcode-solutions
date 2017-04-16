class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList:
            return 0
        stack = []
        res = 0
        stack.append(beginWord)
        if beginWord in wordList:
            wordList.remove(beginWord)
        while stack:
            size = stack.__len__()
            for _ in range(size):
                w = stack.pop(0)
                if w == endWord:
                    return res + 1
                for i in range(len(w)):
                    new_word = list(w)
                    for ch in range(ord("a"), ord("z")):
                        ch = chr(ch)
                        new_word[i] = ch
                        check = "".join(new_word)
                        if check != w and check in wordList:
                            wordList.remove(check)
                            stack.append(check)
            res += 1
        return 0

    def ladderLength1(self, beginWord, endWord, wordList):
        import collections
        wordList.add(endWord)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0
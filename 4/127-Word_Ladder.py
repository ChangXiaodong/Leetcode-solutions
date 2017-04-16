# coding=utf-8
'''
广度优先搜索。
从beginWord开始，找到本单词word变更一个字母(new_word)，并且在wordList中的单词，为下一次的遍历单词。
如果遍历到word == endword，返回累加结果res。

节约时间的方法：
1.检查变更一个字母并且在wordlist中的方法，不要检查wordlist中的单次和本单词是不是差一个字母。
改用，对本单词的每个位置，从a变到z，并且看是否在wordlist中。

2. 对访问过的单次，直接从wordlist中删掉，不需要额外的used来保存是否访问过

3.不要建立从本单词到下个单次映射的哈希表，直接把下个单次存在队列中，这件可以减少建哈希表的时间和空间。
'''
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
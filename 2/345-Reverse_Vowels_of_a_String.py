# coding=utf-8
'''
注意字符串和数组相互转化的方法
str->list:  a = list(string)
list->str:  string = "".join(a)
'''
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        char = list(s)
        vowels = ["a", "e", "i", 'o', 'u', "A", "E", "I", "O", "U"]
        i = 0
        j = len(s) - 1
        while i < j:
            if not char[i] in vowels:
                i += 1
            if not char[j] in vowels:
                j -= 1
            if char[i] in vowels and char[j] in vowels:
                char[i], char[j] = char[j], char[i]
                i += 1
                j -= 1
        return "".join(char)


'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows<1:
        return 0
    if numRows==1:
        return s
    j = 0
    buf = ""
    for i in range(numRows):
        j = i
        while j<len(s):
            buf += s[j]
            if i==0 or i==numRows-1:
                j = j + ((numRows-2)*2+2)
            else:
                j = j + (numRows-i-1)*2
                if j<len(s):
                    buf += s[j]
                    j = j + i*2
    return buf

def convert1(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            print L
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)
print convert("PAYPALISHIRING",3)
print convert1("PAYPALISHIRING",3)



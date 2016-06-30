'''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''
def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x%10 == 0 and x > 0):
            return False
        length = len("%d" % x)
        for i in range(int(length/2)):
            if x % 10 == 0:
                x = int(x/10)
                continue
            first = int(x/pow(10,length-i*2-1))
            last = x%10
            if first != last:
                return False
            x = x - first*pow(10,length-i*2-1)
            x = int(x/10)
        return True

def isPalindrome1(x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        normal = x
        reverse = 0
        while x > 0:
            reverse = reverse * 10 + x%10
            x =int(x / 10)
        return reverse == normal

print(isPalindrome1(122321))
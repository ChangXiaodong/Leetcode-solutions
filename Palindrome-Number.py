def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x%10 == 0 and x > 0):
            return False
        length = len("%d" % x)
        for i in range(length/2):
            if x % 10 == 0:
                x /= 10
                continue
            first = x/pow(10,length-i*2-1)
            last = x%10
            if first != last:
                return False
            x = x - first*pow(10,length-i*2-1)
            x /= 10
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
            x /= 10
        return reverse == normal

print isPalindrome1(123)
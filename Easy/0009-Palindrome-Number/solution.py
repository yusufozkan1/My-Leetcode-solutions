class Solution:
    def isPalindrome(self, x: int) -> bool:
        def reverse(x):
            reversenum = 0
            sign = -1 if x < 0 else 1
            while x > 0 :
                digit = x % 10 
                reversenum = (reversenum * 10 ) + digit
                x //= 10 
                reversenum = reversenum * sign
            return reversenum
       
        if x == reverse(x): return True 
        else:
             return False        
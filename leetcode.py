class LeetCode:
    '''This function takes an integer x, return true if x is a palindrome, and false otherwise.'''
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10
    
    ''' Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. 
If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. 
Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.'''
    
    def myAtoi(self, s: str) -> int:
        s = s.strip()
    
        if not s:
            return 0

        sign = -1 if s[0] == '-' else 1
        i = 1 if s[0] in '+-' else 0

        digits = []
        while i < len(s) and s[i].isdigit():
            digits.append(s[i])
            i += 1

        if not digits:
            return 0

        num = int(''.join(digits)) * sign

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num

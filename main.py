from leetcode import LeetCode

if __name__ == "__main__":
    leet_obj = LeetCode()

    # Test cases for isPalindrome function
    print(leet_obj.isPalindrome(121))    # True
    print(leet_obj.isPalindrome(-121))   # False
    print(leet_obj.isPalindrome(12321))  # True
    print(leet_obj.isPalindrome(10))     # False
    print(leet_obj.isPalindrome(0))      # True

    # Test cases for myAtoi function
    print(leet_obj.myAtoi('0-1'))    # 0
    print(leet_obj.myAtoi('42'))     # 42
    print(leet_obj.myAtoi("   -042"))  # -42
    print(leet_obj.myAtoi( "1337c0d3"))  # 1337
    print(leet_obj.myAtoi("words and 987")) # 0
    print(leet_obj.myAtoi("-91283472332"))    # -2147483648
    print(leet_obj.myAtoi("0"))    # 0
    print(leet_obj.myAtoi("-yu987klj"))    # 0
    print(leet_obj.myAtoi("98lkm654"))   # 98
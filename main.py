from itertools import takewhile
from leetcode import leetcode,ListNode
obj_leetcode = leetcode()

#Test def ispalidrome
print(obj_leetcode.ispalidrome(121))
print(obj_leetcode.ispalidrome(-121))
print(obj_leetcode.ispalidrome(0))
print(obj_leetcode.ispalidrome(121))
print(obj_leetcode.ispalidrome(121))
print(obj_leetcode.ispalidrome(121))

#Test int_reverse function
print(obj_leetcode.int_reverse(12))
print(obj_leetcode.int_reverse(-25))
print(obj_leetcode.int_reverse(987))
print(obj_leetcode.int_reverse(120))

#Test myAtoi function
print(obj_leetcode.myAtoi("   -036"))
print(obj_leetcode.myAtoi("36"))
print(obj_leetcode.myAtoi("288c0d4"))
print(obj_leetcode.myAtoi("0-45"))
print(obj_leetcode.myAtoi("I am 765"))
print(obj_leetcode.myAtoi("0"))


# Manually creating linked lists for testing
l1 = ListNode(3, ListNode(4, ListNode(5)))  # 543
l2 = ListNode(8, ListNode(7, ListNode(9)))  # 978

# Calling addTwoNumbers function
result = leetcode().addTwoNumbers(l1, l2)
#priniting the results
while result:
    print(result.val, end=" -> ")
    result = result.next
from itertools import takewhile
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class leetcode():
    def ispalidrome(self,x):
        ''' ispalidrome function takes number x and checks if it is positive or it is a multiple of 10, if so it return 0 and if is positive number or 0, it procees to find the quotient and reminder'''
        if x < 0 or (x%10 ==0 and x !=0):
            return False
        rev = 0
        while x > 0:
            rev = rev * 10 + x%10
            x //= 10
        return x==rev or x == x//10

    def int_reverse(self, x): 
        sign = -1 if x < 0 else 1
        reversed_x = int(str(abs(x))[::-1]) * sign
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        return reversed_x
    
    def myAtoi(self, s: str) -> int:
        '''This function takes a string s, removes the whitespaces on left and right,returns 0 if the result is empty, assigns -1, or 1 when the first index of S during slicing is either '-', or '+', if sign is not indicated, it assigns s=s[:],uses package takewhile from itertools to consider consistent digit part of the string,joins the digits and sures that the result is 32 bits'''
        s = s.strip()
        if not s:
            return 0

        sign = 1
        if s[0] in ('-', '+'):
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

        digits = ''.join(takewhile(str.isdigit, s))

        if not digits:
            return 0

        num = sign * int(digits)
        return max(min(num, 2**31 - 1), -2**31)

    # Definition for singly-linked list.
    ''' This functions takes two singly linked lists, reverses the values of the two nodes separately and adds the two results to get a single value that is also stored in a reversed version in a single linked rist'''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

    
    
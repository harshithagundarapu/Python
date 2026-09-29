class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0

        dummy = ListNode(0)
        current = dummy

        while l1 or l2 or carry:

            if l1:
                a = l1.val
            else:
                a = 0

            if l2:
                b = l2.val
            else:
                b = 0

            total = a + b + carry

            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next

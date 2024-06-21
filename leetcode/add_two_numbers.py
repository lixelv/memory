# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, lst: list):
        if not lst:
            return None

        dummy = cls()
        current = dummy
        for i in lst:
            current.next = cls(i)
            current = current.next

        return dummy.next

    def __iter__(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result.__iter__()


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, shift=None) -> ListNode:
        result = ListNode()

        current = l1.val + l2.val + (shift or 0)
        if current > 9:
            shift = 1
        else:
            shift = 0

        result.val = current % 10
        if l1.next and l2.next:
            result.next = self.addTwoNumbers(l1.next, l2.next, shift=shift)
        elif l1.next or l2.next:
            result.next = self.addTwoNumbers(
                l1.next if l1.next else l2.next, ListNode(0), shift=shift
            )
        elif shift:
            result.next = ListNode(1)

        return result


current = ListNode.from_list([0])
current2 = ListNode.from_list([0])
print(list(Solution.addTwoNumbers(current, current2)))

from presets.list_node import ListNode
from typing import List, Optional


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current is not None and current.next is not None:
            if current.next.val == 0:
                current.next = current.next.next
                current = current.next
            else:
                current.val += current.next.val
                current.next = current.next.next

        return head


a = ListNode.from_iter([0, 3, 1, 0, 4, 5, 2, 0])
print(Solution().mergeNodes(a))

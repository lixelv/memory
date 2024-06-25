from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binarySearch(self, root: Optional[TreeNode], target) -> bool:
        if root is None:
            return False

        if root.val == target:
            return True
        elif root.val > target:
            return self.binarySearch(root.left, target)
        else:
            return self.binarySearch(root.right, target)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def nodeCheck(node: Optional[TreeNode]) -> bool:
            if node.val == 3:
                print(node.val)

            if node.left is not None:
                if not node.left.val < node.val:
                    return False
                if not nodeCheck(node.left):
                    return False

            if node.right is not None:
                if not node.right.val > node.val:
                    return False
                if not nodeCheck(node.right):
                    return False

            if not self.binarySearch(root, node.val):
                return False

            return True

        return nodeCheck(root)


# [5,4,6,null,null,3,7]
tree = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
print(Solution().isValidBST(tree))

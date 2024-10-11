# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def count(node):
            if node is None:
                return 0
            return count(node.left) + count(node.right) + 1

        if root is None:
            raise ValueError("Tree is empty or k is invalid")

        x = count(root.left)

        if k <= x:
            return self.kthSmallest(root.left, k)
        elif k == x + 1:
            return root.val
        else:
            return self.kthSmallest(root.right, k - x - 1)

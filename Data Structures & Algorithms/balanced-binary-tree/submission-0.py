# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        def getHeight(root):
            if not root:
                return 0

            left_height = getHeight(root.left)
            right_height = getHeight(root.right)

            if abs(left_height - right_height) > 1:
                self.isBalanced = False
            
            return 1 + max(left_height, right_height)

        getHeight(root)
        if not self.isBalanced:
            return False
        else:
            return True


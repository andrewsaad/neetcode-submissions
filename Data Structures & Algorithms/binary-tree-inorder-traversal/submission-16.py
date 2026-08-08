# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_list = []
        if not root:
            return []
        
        if root.left:
           inorder_list.extend(self.inorderTraversal(root.left))
        inorder_list.append(root.val)
        if root.right:
            inorder_list.extend(self.inorderTraversal(root.right))
        return inorder_list
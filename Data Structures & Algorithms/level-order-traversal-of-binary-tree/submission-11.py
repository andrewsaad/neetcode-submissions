# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        main_list = []

        if root:
           queue.append(root)
          # main_list.append([root.val])

        level = 0

        while len(queue) > 0 :
            loop_list = []
            # print("level",level)
            for i in range (len(queue)):
                current = queue.popleft()
                loop_list.append(current.val)
                if current.left:
                    queue.append(current.left)
                    #loop_list.append(current.left.val)
                if current.right:
                    queue.append(current.right)
                    #loop_list.append(root.right.val)
               #loop_list.append(current.val)
            main_list.append(loop_list)
            level +=1
        return main_list
                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque([root])
        zigzag = []
        to_right = False
        if not root:
            return []
        while que:
            temp = []
            for i in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                temp.append(node.val)
            if not to_right:
                zigzag.append(temp)
                to_right = True
            else:
                zigzag.append(temp[::-1])
                to_right = False
        return zigzag
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
      
        self.res = 0

        def iterate(node):
            if not node:
                return 0,0

            l,n_l = iterate(node.left)
            r,n_r = iterate(node.right)

            total_sum = node.val + l + r
            total_num = 1 + n_l + n_r

            av = total_sum//total_num
            if node.val == av:
                self.res += 1

            return total_sum,total_num

        iterate(root)
        return self.res

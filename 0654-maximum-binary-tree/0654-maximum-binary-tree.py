# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        tree = self.dfs(nums, 0, len(nums) - 1)
        
        return tree
    
    def dfs(self, nums, left, right):
        if right < left:
            return None
        
        if right == left:
            return TreeNode(nums[right])
        
        node = TreeNode()
        idx = -1
        val = -1
        
        for i in range(left, right + 1):
            if nums[i] > val:
                idx = i
                val = nums[i]
                
        node.val = val
        node.left = self.dfs(nums, left, idx - 1)
        node.right = self.dfs(nums, idx + 1, right)
        
        return node
        
        
        
        
        
        
        
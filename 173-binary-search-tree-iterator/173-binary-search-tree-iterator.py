# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stk = []
        
        while root:
            self.stk.append(root)
            root = root.left
    def next(self) -> int:
        temp = self.stk.pop()
        cur = temp.right
        while cur:
            self.stk.append(cur)
            cur = cur.left
        
        return temp.val

    def hasNext(self) -> bool:
        return self.stk


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
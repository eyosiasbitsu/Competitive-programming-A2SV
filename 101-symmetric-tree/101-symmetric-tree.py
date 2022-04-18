# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.que = deque()
        self.que.append(root)
        def is_pali(arr):
            i = 0
            l = len(arr) - 1
            while i <= l:
                if (arr[i] and not arr[l]) or (not arr[i] and arr[l]):
                    return False
                elif not arr[i] and not arr[l]:
                    i += 1
                    l -= 1
                elif arr[i].val != arr[l].val:
                    return False
                else:
                    i += 1
                    l -= 1
            return True
        while self.que:
            for i in range(len(self.que)):
                temp = self.que.popleft()
                if temp:
                    self.que.append(temp.left)
                    self.que.append(temp.right)
            if not is_pali(self.que):
                return False
        return True
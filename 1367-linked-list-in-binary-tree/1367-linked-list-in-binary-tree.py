class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        
        if not root:
            return False
        
        if head.val == root.val:
            temp = self.search(head,root)
            if temp:
                return True
        
        return self.isSubPath(head,root.right) or self.isSubPath(head,root.left)
    
    def search(self,head,root):
        if not head:
            return True
        
        if not root or root.val != head.val:
            return False
        
        return self.search(head.next,root.left) or self.search(head.next,root.right)
            
            
            
            
            
            
            
            
            
            
            
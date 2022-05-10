# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #  the first thing we shoud make sure is that if the given root is empty or not
        #  if it is empty we create a new treeNode with value val and return it
        
        if not root:
            return TreeNode(val)
        
        temp = root
        par = None  # is used to find the node wich is direct parent of the position 
        #  in which we are going to insert the value val
        
        # then we iterate over the bst to find the specific position in which 
        # the value can be inserted
        
        while temp:
            par = temp
        # now check weter we should go to the right or to the left to find the position
        # in which val is supposed to be inserted based on 
        # the rules of bst (binary search tree) which are:
        # 1, all the nodes to the left of the given node have less values than the node
        # 2, all the nodes to the right of the given node have more values than the node
        
        # based on the ubove info we proceed to iterate trough the bst
            if val >= temp.val:
                temp = temp.right
            elif val < temp.val:
                temp = temp.left
        
        # now we ave found the parent of the position of the vaue
        # now all that is left is wether the value is inserted to the right or to the left
        # of the parent, we also check this using th ubove two laws of bst
        
        if val >= par.val:
            par.right = TreeNode(val)
            
        else:
            par.left = TreeNode(val)
        
        # the return the modified root
        return root
                
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Disjoint:
    def __init__(self,size):
        self.parent = [ i for i in range(size)]
        self.rank = [ 1 for _ in range(size)]
    
    def find(self, num):
        
        if self.parent[num] == num:
            return num
        
        self.parent[num] = self.find(self.parent[num])
        return self.parent[num]
    
    def union(self, num1, num2):
        par1 = self.find(num1)
        par2 = self.find(num2)
        
        if par1 == par2:
            return
        
        if self.rank[par1] > self.rank[par2]:
            self.parent[par2] = par1
        
        elif self.rank[par1] < self.rank[par2]:
            self.parent[par1] = par2
        
        else:
            self.parent[par2] = par1
            self.rank[par1] += 1
        
    def count(self, _set, size):
        result = set()
        
        for i in range(size):
            par = self.find(i)
            if par in _set:
                result.add(par)
        
        return len(result)
    
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        neighbours = defaultdict(set)
        prev = head.val
        size = 0
        
        while head:
            neighbours[head.val].add(prev)
            prev = head.val
            
            if head.next:
                neighbours[head.val].add(head.next.val)
        
            head = head.next
            size += 1
        
        union_find = Disjoint(size)
        nums = set(nums)
        
        for n in nums:
            for neigh in neighbours[n]:
                if neigh in nums:
                    union_find.union(n, neigh)
        
        result = union_find.count(nums, size)
        
        return result
                
                
                
                
                
                
                
                
                
                
                
                
                
        
        
        
        
        
        
        
        
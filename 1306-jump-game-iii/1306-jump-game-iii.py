class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        self.checker = set()
        self.val = -1
        def do_bfs(i):
            if i not in self.checker:
                self.checker.add(i)
                if arr[i] == 0:
                    self.val = 0
                if 0 <= i-arr[i]:
                    do_bfs(i-arr[i])
                if i + arr[i] < len(arr):
                    do_bfs(i+arr[i])
        do_bfs(start)
        if self.val == 0:
            return True
        return False
        
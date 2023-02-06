# using bfs
class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([])
        visited = set()
        
        queue.append((0, 1, 0))
        visited.add((0, 1))

        while queue:
            size = len(queue)
            
            while size > 0:
                cur_pos, cur_speed, moves = queue.popleft()
                
                if cur_pos == target:
                    return moves
                
                new_pos = cur_pos + cur_speed
                new_speed = 2 * cur_speed
                
                if ((new_pos, new_speed) not in visited and 
                        abs(new_pos - target) < target):
                    visited.add((new_pos, new_speed))
                    queue.append((new_pos, new_speed, moves + 1))
                
                new_pos = cur_pos
                new_speed = 1 if cur_speed < 0 else -1
                
                if (new_pos, new_speed) not in visited and abs(new_pos - target) < target:
                    visited.add((new_pos, new_speed))
                    queue.append((new_pos, new_speed, moves + 1))
        
        return -1

# using dp
class Solution:
    def racecar(self, t, dp = {0 : 0, 0 : 0}):
        if t in dp:
            return dp[t]

        n = t.bit_length()
        
        if 2**n - 1 == t:
            dp[t] = n
        else:
            dp[t] = self.racecar(2**n - 1 - t, dp) + n + 1
            
            for m in range(n - 1):
                dp[t] = min(dp[t], self.racecar(t - 2**(n - 1) + 2**m, dp) + n + m + 1)
        
        return dp[t]

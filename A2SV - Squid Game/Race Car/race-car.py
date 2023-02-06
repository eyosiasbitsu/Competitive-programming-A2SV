
class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([])
        visited = set()
        queue.append((0, 1, 0))
        visited.add((0, 1))
        while queue:
            size = len(queue)
            while size > 0:
                current_position, current_speed, moves = queue.popleft()
                if current_position == target:
                    return moves
                new_position = current_position + current_speed
                new_speed = 2 * current_speed
                if (new_position, new_speed) not in visited and abs(new_position - target) < target:
                    visited.add((new_position, new_speed))
                    queue.append((new_position, new_speed, moves + 1))
                # Explore option : "R"
                new_position = current_position
                new_speed = 1 if current_speed < 0 else -1
                if (new_position, new_speed) not in visited and abs(new_position - target) < target:
                    visited.add((new_position, new_speed))
                    queue.append((new_position, new_speed, moves + 1))
        return -1

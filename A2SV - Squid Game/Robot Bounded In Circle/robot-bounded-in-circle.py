# Solution1
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        directions = [1, 1, -1, -1]
        cur_direction = 0
        cur_position = [0, 0]

        for instruction in instructions:
            if instruction == "G":
                cur_position[(cur_direction % 2 + 1)%2] += directions[cur_direction]
            
            elif instruction == "L":
                cur_direction -= 1

                if cur_direction < 0:
                    cur_direction = 3
            
            elif instruction == "R":
                cur_direction = (cur_direction + 1) % 4
        
        cur_position = tuple(cur_position)

        return cur_position == (0, 0) or cur_direction != 0

# Solution2
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        horizontal_dir = 0
        vertical_dir = 1

        cur_position = [0, 0]

        for instruction in instructions:
            if instruction == "G":
                cur_position[0] += horizontal_dir
                cur_position[1] += vertical_dir
            
            elif instruction == "L":
                horizontal_dir, vertical_dir = -1*vertical_dir, horizontal_dir
            
            else:
                horizontal_dir, vertical_dir = vertical_dir, -1*horizontal_dir
        
        cur_position = tuple(cur_position)

        return cur_position == (0, 0) or (horizontal_dir, vertical_dir) != (0, 1)



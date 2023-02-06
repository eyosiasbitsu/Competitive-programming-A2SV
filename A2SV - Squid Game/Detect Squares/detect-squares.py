class DetectSquares:

    def __init__(self):
        self.points_count = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points_count[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        point_x, point_y = point
    
        for x, y in self.points:
            if ((x != point_x and y != point_y) and 
                    (abs(x - point_x) == abs(y - point_y))):
                
                res += self.points_count[(x, point_y)]*self.points_count[(point_x, y)]
        
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

class RecentCounter:

    def __init__(self):
        # Initializes the counter with zero recent requests.
        self.recentcounter = [] 
    def ping(self, t: int) -> int:
        if len(self.recentcounter) == 0:
            self.recentcounter.append(t)
        else:
            self.recentcounter.append(t)
            while self.recentcounter[0] < t - 3000:
                self.recentcounter.pop(0)
        return len(self.recentcounter)
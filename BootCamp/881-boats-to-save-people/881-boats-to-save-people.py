class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        count = 0
        
        if people[0] >= limit:
            return len(people)
        
        i = 0
        j = len(people) - 1
        while i <= j:
            if people[i] + people[j] > limit:
                count += 1
            if people[i] + people[j] <= limit:
                count += 1
                i += 1
            j -= 1
        return count
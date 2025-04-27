class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        start, end = 0, len(people) - 1
        boats = 0

        while end >= start:
            capacity = limit - people[end]
            
            end -= 1
            boats += 1

            if end >= start and capacity >= people[start]:
                start += 1
        
        return boats


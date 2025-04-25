class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        boats = 0
        start, end = 0, len(people) - 1

        while end >= start:
            capacity = limit - people[end]
            end -= 1
            boats += 1

            if end >= start and capacity >= people[start]:
                start += 1


        return boats
            

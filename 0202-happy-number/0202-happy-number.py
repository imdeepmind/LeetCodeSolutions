class Solution:
    def getIndividualNumbers(self, num):
        if num < 10:
            return [num]
        
        rem = num % 10
        div = num // 10


        return self.getIndividualNumbers(div) + [rem]
    
    def productSum(self, nums):
        return sum([num**2 for num in nums])

    def isHappy(self, n: int) -> bool:
        slow = self.productSum(self.getIndividualNumbers(n))
        fast = self.productSum(self.getIndividualNumbers(slow))

        while slow != fast:
            if slow == 1 or fast == 1:
                return True
            slow = self.productSum(self.getIndividualNumbers(slow))
            fast = self.productSum(self.getIndividualNumbers(self.productSum(self.getIndividualNumbers(fast))))

        return slow == 1
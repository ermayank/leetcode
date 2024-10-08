class Solution:
    
    def squareSum(self, num):
        sum = 0
        num = str(num)
        for i in range(len(num)):
            sum += int(num[i]) * int(num[i])
            
        return sum
    

    def isHappy(self, n: int) -> bool:
        seenSet = set()

        while (n != 1 and n not in seenSet):
            seenSet.add(n)
            n = self.squareSum(n)
        
        return n == 1
        

        
        
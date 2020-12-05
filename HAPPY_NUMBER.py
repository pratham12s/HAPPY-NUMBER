class Solution:
    def sumofsquare(self,n):
        sum1=0
        while n>0:
            sum1+=(n%10)*(n%10)
            n=n//10
        return sum1
    def isHappy(self, n: int) -> bool:
        current=n
        current_1=n
        while True:
            current = self.sumofsquare(current)
            current_1 = self.sumofsquare(self.sumofsquare(current_1))
            if current!=current_1:
                continue
            else:
                break
        return current==1
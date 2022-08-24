class solution(object):
    def maxprofit(self, prices):
        if not prices:
            return 0
        leftmin, rightmax = [0 for i in range(len(prices))], [0 for i in range(len(prices))]
        leftmin[0] = prices[0]

        for i in range(1, len(prices)):
            leftmin[i] = min(leftmin[i-1], prices[i])

        #print(leftmin)

        rightmax[-1] = prices[-1]
        for i in range(len(prices) -2, -1, -1):
            rightmax[i] = max(rightmax[i+1], prices[i])

        #print(rightmax)
        ans = 0
        for i in range(len(prices)-1):
            ans = max(ans, rightmax[i+1]-leftmin[i])
        return ans

ob1 = solution()
print(ob1.maxprofit([7,2,5,8,6,3,1,4,5,4,7]))

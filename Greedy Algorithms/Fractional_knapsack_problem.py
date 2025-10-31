class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        n = len(val)
        # Create list of (value, weight, ratio)
        items = [(val[i], wt[i], val[i]/wt[i]) for i in range(n)]
        # Sort by ratio descending
        items.sort(key=lambda x: x[2], reverse=True)

        curw = 0
        finalValue = 0.0

        for value, weight, ratio in items:
            if curw + weight <= capacity:
                curw += weight
                finalValue += value
            else:
                remain = capacity - curw
                finalValue += ratio * remain
                break

        return round(finalValue, 6)


val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50

print(Solution().fractionalKnapsack(val, wt, capacity))

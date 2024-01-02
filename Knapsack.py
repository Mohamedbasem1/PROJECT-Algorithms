
def knapSack(wt, val, W):
    n = len(val)
    # initialize the dp matrix with items row and W columns
    dp =[[0 for _ in range(W + 1)] for _ in range(n)]


    for i in range(n):
        for w in range(W + 1):
            # because 1st row is when i am not talking any item
            # and 1st column because there is no available W
            if i == 0 or w == 0:
                dp[i][w] = 0

                # check if w of the item now is less than or equal available wight
                # take it
            elif wt[i] <= w:
                dp[i][w] = max(val[i] + dp[i - 1][w - wt[i]], dp[i - 1][w])

                #     if the available weight is less than the item's weight
                # leave it
            else:
                dp[i][w] = dp[i - 1][w]


    # return the last cell with largest value.
    return dp[i][w]

# Example usage:
weights = [4, 3, 2, 1]
values =  [5, 4, 3, 2]
capacity = 6
result = knapSack(weights, values, capacity)

print(f"For a knapsack with a capacity of {capacity} and items:")
for i in range(0,len(weights)):
    print(f"Item {i + 1}: Value = {values[i]}, Weight = {weights[i]}")

print(f"\nThe maximum value that can be obtained is: {result}")

print(result)


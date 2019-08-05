# Challenge 4 - Dynamic Programming

## Knapsack Problem

Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.

### Steps in Solving

1. Subproblems: All the combinations of other items that add up to be less than the maximum for each item M if item M can be included in the final solution.
2. Guess First Choice: Here we can arbitrarily choose the first item that has a weight less then the maximum capacity.
3. Recursively define the value of an optimal solution: For each item we must find the subproblems.
4. Compute the value of an optimal solution: Look at the code.
5. Solve original problem: Done.

## Coin Change Problem

Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.

### Steps in Solving

1. Subproblems: All the combinations of coins that can be added up to make a given value in change.
2. Guess First Choice: Just pick the last item if it is less that the max (bottom-up)
3. Recursively define the value of an optimal solution: For each item we must find the subproblems.
4. Compute the value of an optimal solution: Look at the code.
5. Solve original problem: Done.

## Resources

https://skerritt.blog/dynamic-programming/#knapsack-problem
http://rosettacode.org/wiki/Knapsack_problem/0-1#Recursive_dynamic_programming_algorithm
https://www.geeksforgeeks.org/coin-change-dp-7/

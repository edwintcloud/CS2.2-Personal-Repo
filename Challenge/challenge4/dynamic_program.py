from timeit import default_timer as timer


class Coins:
    def __init__(self, coins, target_value):
        self.coins = coins
        self.target_value = target_value

    def solve(self, coins=None, target_value=None):
        """
        Coin change problem solution using dynamic programming.

        Args:
            coins ([int]): The coins.
            target_value (int): The target value.

        Returns:
            result (int): Number of ways to make change with coins
            that adds up to target_value.
        """
        if coins is None or target_value is None:
            coins = self.coins
            target_value = self.target_value

        # return empty tuple if items is empty
        if not coins:
            return -1

        # the meat and potatoes
        table = [target_value + 1] * (target_value + 1)
        table[0] = 0
        for i in range(1, target_value + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    table[i] = min(table[i], table[i - coins[j]] + 1)

        # return answer or -1 if not found
        return (
            -1 if table[target_value] > target_value else table[target_value]
        )

    def print_result(self):
        start = timer()
        result = self.solve(self.coins, self.target_value)
        end = timer()
        print('\nFor this input:')
        print(
            "\tList of coins: [{}]".format(
                ', '.join(''.join(str(i)) for i in self.coins)
            )
        )
        print(f"\tTarget value: {self.target_value}")
        print("\nThe solution is:")
        print("\t{}\n".format(result))

        # print runtime info
        print(f'Runtime: {((end - start) * 1000):.2f}ms')


if __name__ == "__main__":

    # compute and print the result
    coins = [1, 5, 10, 25]
    target_value = 100
    c = Coins(coins, target_value)
    c.print_result()

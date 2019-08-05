import unittest
from knapsack import Knapsack
from dynamic_program import Coins


class Chal4Test(unittest.TestCase):
    def test_knapsack_values(self):
        bag = (
            (10, 60),
            (20, 100),
            (30, 195),
            (40, 120),
            (50, 120),
            (5, 120),
            (60, 120),
            (10, 50),
            (10, 200),
            (20, 120),
        )
        size = 50
        ks = Knapsack(bag, size)
        result = ks.solve()

        self.assertEqual(((30, 195), (5, 120), (10, 200)), result)

    def test_knapsack_empty(self):
        bag = ()
        size = 50
        ks = Knapsack(bag, size)
        result = ks.solve()

        self.assertEqual((), result)

    def test_coins_values(self):
        coins = [1, 5, 10, 25]
        target_value = 100
        c = Coins(coins, target_value)
        result = c.solve()

        self.assertEqual(4, result)

    def test_coins_empty(self):
        coins = []
        target_value = 100
        c = Coins(coins, target_value)
        result = c.solve()

        self.assertEqual(-1, result)

    def test_coins_no_answer(self):
        coins = [5, 10, 25]
        target_value = 103
        c = Coins(coins, target_value)
        result = c.solve()

        self.assertEqual(-1, result)


if __name__ == "__main__":
    unittest.main()

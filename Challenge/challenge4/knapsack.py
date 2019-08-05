from functools import lru_cache
from timeit import default_timer as timer


class Knapsack:
    def __init__(self, items, max_cap):
        self.items = items
        self.max_cap = max_cap

    @lru_cache(maxsize=None)
    def solve(self, items=None, max_cap=None):
        """
        Knapsack problem solution using dynamic programming. We must
        use a tuple of tuples here so that lru_cache can hash solutions.

        Args:
            items ([(int, int)]): The items in the knapsack representated as a
            tuple of (size, value).
            max_cap (int): The maximum capacity of the knapsack. The total of
            item sizes must not exceed this number.

        Returns:
            result (((int, int))): List of items with optimal value to fit in
             the knapsack.
        """
        if items is None or max_cap is None:
            items = self.items
            max_cap = self.max_cap

        # return empty tuple if items is empty
        if not items:
            return ()

        # the meat and potatoes
        head = items[0]
        tail = items[1:]
        include = (head,) + self.solve(tail, max_cap - head[0])
        exclude = self.solve(tail, max_cap)
        include_sum = (
            sum(i[1] for i in include)
            if sum(i[0] for i in include) < max_cap
            else 0
        )
        exclude_sum = (
            sum(i[1] for i in exclude)
            if sum(i[0] for i in exclude) < max_cap
            else 0
        )

        # cacheable result
        return include if include_sum > exclude_sum else exclude

    def print_result(self):
        start = timer()
        result = self.solve(self.items, self.max_cap)
        end = timer()
        print('\nFor this input:')
        print(
            "\tList of items with size and value: ({})".format(
                ', '.join(''.join(str(i)) for i in self.items)
            )
        )
        print(f"\tSize of knapsack: {self.max_cap}")
        print("\nThe solution is:")
        print("\t{}\n".format(', '.join(''.join(str(i)) for i in result)))

        # print runtime info
        print(f'Runtime: {((end - start) * 1000):.2f}ms')
        print(self.solve.cache_info())


if __name__ == "__main__":

    # compute and print the result
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
    ks.print_result()

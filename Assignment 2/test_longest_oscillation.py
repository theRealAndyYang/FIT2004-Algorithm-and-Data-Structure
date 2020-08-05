import unittest
import task1
from itertools import combinations
import random


class TestLongestOscillation(unittest.TestCase):

    def is_oscillation(self, lst):
        # Checks if the oscillation array is correct

        # Empty lists are True
        if lst == []:
            return True

        # Lists of only one element are correct oscillations
        if len(lst) == 1:
            return True

        # Sanity check that nothing is the same next to each other for answer
        for i in range(1, len(lst)):
            if lst[i-1] == lst[i]:
                return False

        # Check oscillations
        last_up = False
        last_down = False

        if lst[0] > lst[1]:
            last_down = True
        else:
            last_up = True

        i = 2
        while i < len(lst):
            if last_up:
                if lst[i-1] < lst[i]:
                    return False

                last_up = False
                last_down = True

            elif last_down:
                if lst[i-1] > lst[i]:
                    return False

                last_up = True
                last_down = False

            i += 1

        return True

    def output_check(self, output):
        # Sanity check to ensure the length of the output list is the same as
        # the number given

        # output = (len, ouput_lst)
        return output[0] == len(output[1])

    def brute_force_solutions(self, input_lst):
        # List of elements in the format (len, actual list of the numbers in
        # oscillating order)

        filtered_sols = []
        for i in range(len(input_lst)+1):
            temp_i_len_sols = []
            for potential_sol in combinations(input_lst, i):
                potential_sol = list(potential_sol)
                if self.is_oscillation(potential_sol):
                    temp_i_len_sols.append(
                        (len(potential_sol), potential_sol))

            if temp_i_len_sols != []:
                filtered_sols = temp_i_len_sols

        print("-------- Actual Number Solutions (NOT INDEX'S) --------")
        for i in filtered_sols:
            print(i)

        return filtered_sols

    def is_optimal_solution(self, input_lst, proposed_solution):
        self.assertTrue(
            self.output_check(proposed_solution))

        output_lst = []
        for index in proposed_solution[1]:
            output_lst.append(input_lst[index])

        self.assertTrue(
            self.is_oscillation(output_lst))

        output_result = (len(output_lst), output_lst)
        print("-------- Input Number Solutions (NOT INDEX'S) ---------")
        print(output_result)

        if output_result in self.brute_force_solutions(input_lst):
            return True

        return False

    # USE THIS TO TEST
    def check_longest_oscillation(self, input_lst):
        print("\n\n + REAL TEST +")
        proposed_solution = task1.longest_oscillation(input_lst)
        print("Input List=>", input_lst)
        print("Proposed Solution =>", proposed_solution, "\n")
        self.assertTrue(
            self.is_optimal_solution(input_lst, proposed_solution))

    def test_empty_is_oscillation(self):
        self.assertTrue(self.is_oscillation([]))

    def test_single_item_is_oscillation(self):
        self.assertTrue(self.is_oscillation([5]))
        self.assertTrue(self.is_oscillation([2]))
        self.assertTrue(self.is_oscillation([6]))
        self.assertTrue(self.is_oscillation([1]))
        self.assertTrue(self.is_oscillation([-1561646]))
        self.assertTrue(self.is_oscillation([548968676876874]))
        self.assertTrue(self.is_oscillation([---54896867634243234876874]))

    def test_same_items_is_oscillation(self):
        self.assertFalse(self.is_oscillation(
            [5, 5, 4342, 3421, 2223, 4123, 22, 22]))

        self.assertFalse(self.is_oscillation(
            [1, 2, 3, 4, 5, 6, 7, 89, -1, 1, 5, 4, 78, 0, 0, 5, 4]))

        self.assertFalse(self.is_oscillation(
            [1, 1, 1, 1, 1, 1, 1, 1]))

        self.assertFalse(self.is_oscillation(
            [1, 2, 3, 4, 5, 6, 7, 8, 1, 1]))

        self.assertFalse(self.is_oscillation(
            [0, 0]))

    def test_good_oscillations_check(self):
        self.assertTrue(self.is_oscillation([1, 2]))
        self.assertTrue(self.is_oscillation([2, 1]))

        self.assertTrue(self.is_oscillation([2, 1, 2]))
        self.assertTrue(self.is_oscillation([1, 2, 1]))

        self.assertTrue(self.is_oscillation([2, 1, 2, 1]))
        self.assertTrue(self.is_oscillation([1, 2, 1, 2]))

        self.assertTrue(self.is_oscillation([2, 1, 2, 1, 2]))
        self.assertTrue(self.is_oscillation([1, 2, 1, 2, 1]))

        self.assertTrue(self.is_oscillation(
            [-1, 20, -1000, 2, 1, 103123, 0, 1, 0]))

        self.assertTrue(self.is_oscillation(
            [-1, 20, -1000, 2, 1, 103123, 0, 1, 0, 1.21]))

    def test_output_check(self):
        self.assertTrue(self.output_check((7, [1, 2, 3, 4, 5, 6, 7])))
        self.assertFalse(self.output_check((7, [1, 2, 3, 4, 5, 6])))
        self.assertTrue(self.output_check(
            (11, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100])))
        self.assertTrue(self.output_check(
            (0, [])))
        self.assertTrue(self.output_check(
            (1, [5454])))
        self.assertFalse(self.output_check(
            (1, [21, 21])))

    def test_is_optimal_solution(self):
        input_lst = [1, 1, 1, 1, 1]
        proposed_solution = (1, [0])
        self.is_optimal_solution(input_lst, proposed_solution)

        input_lst = [1, 5, 7, 4, 6, 8, 6, 7, 1]
        proposed_solution = (7, [0, 2, 3, 5, 4, 7, 8])
        self.is_optimal_solution(input_lst, proposed_solution)

        input_lst = [1, 2, 3]
        proposed_solution = (2, [0, 1])
        self.is_optimal_solution(input_lst, proposed_solution)

    # REAL TESTS FOR FUNCTION task1.longest_oscillation()
    def test_null_list(self):
        self.check_longest_oscillation([])

    def test_single_list(self):
        self.check_longest_oscillation([0])
        self.check_longest_oscillation([-1])
        self.check_longest_oscillation([-122])
        self.check_longest_oscillation([5000])
        self.check_longest_oscillation([42742])
        self.check_longest_oscillation([1513545])
        self.check_longest_oscillation([-42742])

    def test_samples_on_sheet(self):
        self.check_longest_oscillation([1, 1, 1, 1, 1])
        self.check_longest_oscillation([1, 5, 7, 4, 6, 8, 6, 7, 1])
        self.check_longest_oscillation([1, 2, 3])

    def test_edge_values_at_end(self):
        self.check_longest_oscillation([1, 5, 7, 4, 6, 8, 6, 7, 1, 1, 1, 1, 1])

    def test_edge_values_at_start(self):
        self.check_longest_oscillation(
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3])

    def test_samething(self):
        self.check_longest_oscillation(
            [1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1000])

    def test_doubles(self):
        self.check_longest_oscillation([1, -20021])
        self.check_longest_oscillation([1, -123545.1658578])
        self.check_longest_oscillation([0, 0])
        self.check_longest_oscillation([50, 12015.54565])

    def test_long_numbers(self):
        self.check_longest_oscillation(
            random.sample(range(-100, 100), 22))

    def test_random_lists(self):
        for _ in range(100):
            rand_list = random.sample(range(-100, 100), 10)
            self.check_longest_oscillation(rand_list)

        for _ in range(10):
            rand_list = random.sample(range(-100, 100), 20)
            self.check_longest_oscillation(rand_list)

    def test_long_start_and_end(self):
        self.check_longest_oscillation(
            [5, 5, 5, 5, 5, 5, 11, 11, 11, 11, 11, 22, 22, 22, 0, 0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()

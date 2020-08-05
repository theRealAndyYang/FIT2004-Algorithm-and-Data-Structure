import random
import csv
import timeit
from task1 import *

def time_radix_sort():
    """
    this function performs radix sort for different bases and time them seprately then write them into a csv file
    @return: the runtime of each sort
    @time complexity: O(nm) where n is the size of test_data and m is the number of digit
    @space complexity: O(nm) where n is the size of test_data and m is the number of digit
    """
    f = open('task2analysis.csv', 'w', newline = '', encoding = 'utf-8')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["Base", "Runtime"])
    bases = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    results = []
    for base in bases:
        test_data = [random.randint(1,(2**64)-1) for _ in range(100000)]
        start = timeit.default_timer()
        radix_sort(test_data, base)
        time = timeit.default_timer() - start
        results.append(time)
        csv_writer.writerow([base, time])
    f.close()
    return results

print(time_radix_sort())
import math

def get_digit(num, digit):
    """
    this function simplyt get the right most digit for the input number
    @param num: a integer
    @param digit: the which digit should it get
    @return the specific digit of the integer
    @time complexity: O(1)
    @space complexity: O(1)
    """
    return num[-digit]


def convert_base_b(num, b, digit):
    """
    this function converts decimal integer into base b
    @param num: the decimal integer
    @param b: the target base
    @param digit: the target digit
    @return: the input integer in base b
    @time complexity: O(n) where n is the digit
    @space complexity: O(n) where n is the digit
    """
    result = []
    for _ in range(digit):
        reminder = num % b
        quotient = num // b
        num = quotient
        result.append(reminder)
    return result[::-1]


def convert_base_10(num, b):
    """
    this function converts integer in base b to decimal
    @param num: number in base b
    @param b: the target base
    @return: the input number in decimal
    @time complexity: O(n) where n is the digit
    @space complexity: O(n) where n is the digit
    """
    result = 0
    for n in num:
        result *= b
        result += n
    return result

def radix_aux(array, b, digit):
    """
    this function performs counting sort for each single row of specific digit in the array
    @param array: the array which need to sorted
    @param b: the target base
    @param digit: the target digit
    @return: the sorted array in the order of specific digit
    @time complexity: O(n) where n is size of the array
    @space complexity: O(n) where n is size of the array
    """
    size = len(array)
    count = [0] * (b)
    for i in range(0, size):
        count[get_digit(array[i], digit)] += 1
    position = [0] + ([0] * b)
    for i in range(1, b+1):
        position[i] = position[i-1] + count[i-1]
    temp = [0] * size
    for i in range(0, size):
        temp_digit = get_digit(array[i], digit)
        temp[position[temp_digit]] = array[i]
        position[temp_digit] += 1
    for i in range(size):
        array[i] = temp[i]
    return array

def radix_sort(array, b):
    """
    this function performs radix sort by sorting each digit of element from right most to left most
    @param array: the array which need to sorted
    @param b: the target base
    @return: the sorted array
    @time complexity: O(nm) where n is the size of array and m is the number of digit
    @space complexity: O(nm) where n is the size of array and m is the number of digit
    """
    digits = 0
    base = min(b, 10)
    for i in range(len(array)):
        digits = max(digits, math.ceil(math.log(array[i] + 1, base)))   # use upperbound of log to find the maximum digits in the array
    base_b = [convert_base_b(num, b, digits) for num in array]
    for digit in range(1, digits+1):
        array = radix_aux(base_b, b, digit)
    array = [convert_base_10(nums, b) for nums in array]
    return array
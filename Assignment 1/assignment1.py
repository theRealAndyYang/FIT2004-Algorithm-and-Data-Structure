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

def rotate(string, p):
    """
    this function get the string after p rotations, 
    @param string: str, original string before converting
    @param p: number of rotation
    @time_complexity: O(m), where m is the length of string
    @space_complexity: O(m), where m is the length of string
    """
    p = p% len(string)
    result = string[p:] + string[:p]
    return result

def unrotate(s, p):
    """
    this function restore the string before p rotations, 
    @param string: str, original string before converting
    @param p: number of rotation
    @time_complexity: O(m), where m is the length of string
    @space_complexity: O(m), where m is the length of string
    """
    p = p% len(s)
    result = s[-p:] + s[:-p]
    return result

def to_numberic(s):
    """
    this function convert string to integer using ord() function
    @time_complexity: O(m), where m is the length of input string
    @space_complexity: O(m), where m is the length of input string
    """
    total = 0
    for c in s:
        total *= 27
        total += ord(c) - ord("a") + 1
    return total

def to_string(n):
    """
    this function convert integer into string
    @param n: a integer
    @time_complexity: O(log(n)) where n is the input integer
    @space_complexity: O(log(n)) where n is the input integer
    """    
    result = []
    while n > 0:
        result.append(chr((n % 27) - 1 + ord("a")))
        n = n // 27
    return "".join(result[::-1])

def find_rotations(string_list, p):
    """
    this function finds the identical string after p rotation
    @param string_list: a list containing strings
    @param p: the number of rotation
    @time_complexity: O(nm), where n is the length of the string, m is the length of the word in the array which has maximum character
    @space_complexity: O(nm), where n is the length of the string, m is the length of the word in the array which has maximum character
    """    

    # apply rotate function to entire list, O(NM)
    rotated = [rotate(s, p) for s in string_list]
    # combine rotated list and original, O(N)
    combined = rotated + string_list
    # convert all string to numeric values, O(NM)
    combined_num = [to_numberic(s) for s in combined]

    # apply radix sort on all numeric values, O(NM)
    combined_num = radix_sort(combined_num, 27)

    # check equality with next element in list, if match, convert back to original form O(NM)
    result = []
    for i in range(len(combined_num)-1):
        if combined_num[i] == combined_num[i+1]:

            s = unrotate(to_string(combined_num[i]), p)
            result.append(s)

    return result
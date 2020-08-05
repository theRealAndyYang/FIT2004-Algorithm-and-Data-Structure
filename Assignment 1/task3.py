from task1 import *
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
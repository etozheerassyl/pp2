#TASK 1
from functools import reduce

def multiply_list(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

numbers = [1, 2, 3, 4, 5]
result = multiply_list(numbers)
print("Result:", result)
#TASK 2
def count_upper_lower(string):
    u_count = sum(1 for char in string if char.isupper())
    l_count = sum(1 for char in string if char.islower())
    return u_count, l_count

string = "SahlO FolIna"
upper, lower = count_upper_lower(string)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
#TASK 3
def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

string1 = "Kazak"
if is_palindrome(string1):
    print("True")
else:
    print("False")
#TASK 4
import time
import math

def delayed_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result

number = 25100
milliseconds = 2123

result = delayed_square_root(number, milliseconds)

print(f"Square root of {number} after {milliseconds} milliseconds is {result}.")
#TASK 5
def all_true(tuple_data):
    return all(tuple_data)

tuple_data = (True, True, True, True)
result = all_true(tuple_data)
print(result)  

tuple_data = (True, False, True, True)
result = all_true(tuple_data)
print(result)  


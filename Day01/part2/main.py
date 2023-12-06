## Store input as lines as  array elements
## check if in each line, char is a digit, store in another array
## concatenate first and last element in that array as a number "94"
## find sum of all the elements of the sorted array and print it.
## exmaple:
## eightfivesssxxmgthreethreeone1sevenhnz
## hzdlftdtfqfdbxgsix9onetwo13
## [11,93]
## [11+93]
## 104
from preprocessor_func import preprocessing

filename = "input1.txt"
array = []
sorted_array = []

with open(filename, "r") as file:
    for i in file:
        array.append(i.strip())
        line_numbers = []
        line_numbers = preprocessing(i)
        line_numbers_int = [int(char) for char in line_numbers if char.isdigit()]
        if line_numbers_int:
            first_num = line_numbers_int[0]
            last_num = line_numbers_int[-1]
            sorted_num = f"{first_num}{last_num}"
            sorted_array.append(sorted_num)
sum_of_sorted_array = sum(map(int, sorted_array))
print(sum_of_sorted_array)

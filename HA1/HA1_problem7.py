import os
import math as mt
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
input_filepath = filedialog.askopenfilename()
input_file = open(input_filepath)
input_objects = input_file.readlines()
symbols_string = input_objects[0]
ordered_string = ""
for char in symbols_string:
    if char != " " and char != "\n":
        ordered_string = ordered_string + char
length_n = int(input_objects[1])

# Fnx prints all possible strings of length k
def find_all_perms(set, prefix, k):
    n = len(set)
    # Base case: k is 0, print prefix
    if (k == 0):
        perm_list.append(prefix)
        return
    # One by one add all characters from set and recursively call for k equals to k-1
    for i in range(n):
        # Next character of input added
        newPrefix = prefix + set[i]
        # k is decreased, because we have added a new character
        find_all_perms(set, newPrefix, k - 1)


# get permutations symbols_string of length_n
perm_list = []
find_all_perms(ordered_string, "", length_n)
print(perm_list)
output_file = open("CS122_JB_P7_AnsFile.txt", "w+")
for element in perm_list:
    output_file.write(element + "\n")
output_file.close()
outputfile_check = open("CS122_JB_P7_AnsFile.txt", "r")
outputfile_check_lines = outputfile_check.readlines()
print(outputfile_check_lines)
dir_path = os.path.dirname(os.path.realpath("CS122_JB_P7_AnsFile.txt"))
print(dir_path)



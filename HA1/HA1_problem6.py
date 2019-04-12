import os
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
input_filepath = filedialog.askopenfilename()
input_file = open(input_filepath)
input_objects = input_file.readlines()
output_dict = {}
for char in input_objects[0]:
    if char in output_dict:
        output_dict[char] += 1
    elif char == '\n':
        continue
    else:
        output_dict[char] = 1
output_file = open("CS122_JB_P6_AnsFile.txt", "w+")
output_file.write(str(output_dict['A']) + " " + str(output_dict['C']) + " " + str(output_dict['G']) + " " + str(output_dict['T']))
output_file.close()
outputfile_check = open("CS122_JB_P6_AnsFile.txt", "r")
outputfile_check_lines = outputfile_check.readlines()
print(outputfile_check_lines)
dir_path = os.path.dirname(os.path.realpath("CS122_JB_P6_AnsFile.txt"))
print(dir_path)

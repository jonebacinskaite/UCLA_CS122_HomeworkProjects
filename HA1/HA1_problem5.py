import os
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
input_filepath = filedialog.askopenfilename()
input_file = open(input_filepath)
input_objects = input_file.readlines()
for line in input_objects:
	output_list = line.split(" ")
i = 0
output_dict = {}
while i < len(output_list):
    if output_list[i] in output_dict:
        output_dict[output_list[i]] += 1
    elif output_list[i] == 'be\n':
        output_dict['be'] += 1
    else:
        output_dict[output_list[i]] = 1
    i += 1
output_file = open("CS122_JB_P5_AnsFile.txt", "w+")
for key, value in output_dict.items():
    output_file.write(key + " " + str(value) + "\n")
output_file.close()
outputfile_check = open("CS122_JB_P5_AnsFile.txt", "r")
outputfile_check_lines = outputfile_check.readlines()
print(outputfile_check_lines)
dir_path = os.path.dirname(os.path.realpath("CS122_JB_P5_AnsFile.txt"))
print(dir_path)



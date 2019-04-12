import os
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
input_filepath = filedialog.askopenfilename()
input_file = open(input_filepath)
input_objects = input_file.readlines()
output_file = open("CS122_JB_P4_AnsFile.txt", "w+")
i = 0
while i < len(input_objects):
	if(i%2)==1:
		output_file.write(input_objects[i])
	i = i + 1
output_file.close()
outputfile_check = open("CS122_JB_P4_AnsFile.txt", "r")
outputfile_check_lines = outputfile_check.readlines()
print(outputfile_check_lines)
dir_path = os.path.dirname(os.path.realpath("CS122_JB_P2_AnsFile.txt"))
print(dir_path)

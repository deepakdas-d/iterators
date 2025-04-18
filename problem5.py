#Write a function to compute the total number of lines of code in all python files in the specified directory recursively.
# try:

#     def total_line(file):
#         with open(file,'r')as f:
#             n=len(f.readlines())
#             print(n)
# except FileNotFoundError:
#     print("No File Exisit in that name")

# total_line('problem1.py')
import os

def total_lines(dir):
    line_count=0
    for root, dirs, files in os.walk(dir):#go through  directory.
        for file in files:# in the files.
            path=os.path.join(root,file)
            try:
                with open(path, 'r') as f:
                    for line in f:
                        line_count += 1
            except Exception as e:
                print(f"Could not read {path}: {e}")
    print("Total number of lines:", line_count)

total_lines('C:/Users/deepa/New folder')
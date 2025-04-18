#Write a function to compute the number of python files (.py extension) in a specified directory recursively.

import os

def py_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):#go through  directory.
        for file in files:# in the files.
            if file.endswith('.py'):#find files end with ".py".
                count += 1
    return count

# Example usage
directory_path = "D:\python\working with data"
print("Number of Python files:", py_files(directory_path))


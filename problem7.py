# Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.
import sys
import os

def split_file(n, filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    total_lines = len(lines)
    base_name = os.path.splitext(filename)[0]#program
    ext = os.path.splitext(filename)[1]#.py
    
    for i in range(0, total_lines, n):
        split_lines = lines[i:i+n]#slice the lines till n.
        part_filename = f"{base_name}_part{i//n + 1}{ext}"#'problem1_part1.py
        with open(part_filename, 'w') as out_file:
            out_file.writelines(split_lines)
        print(f"Written {len(split_lines)} lines to '{part_filename}'")


try:
    n = int(sys.argv[1])
except ValueError:
    print("Error: n must be an integer.")
    sys.exit(1)

filename = sys.argv[2]
split_file(n, filename)
###output
# Written 3 lines to 'problem1_part1.py'
# Written 3 lines to 'problem1_part2.py'
# Written 3 lines to 'problem1_part3.py'
# Written 3 lines to 'problem1_part4.py'
# Written 3 lines to 'problem1_part5.py'
# Written 3 lines to 'problem1_part6.py'
# Written 3 lines to 'problem1_part7.py'
# Written 3 lines to 'problem1_part8.py'
# Written 3 lines to 'problem1_part9.py'
# Written 3 lines to 'problem1_part10.py'
# Written 1 lines to 'problem1_part11.py'
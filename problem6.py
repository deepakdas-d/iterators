#Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively.
import os

def count_code_lines(directory):
    total_lines = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r') as f:
                        for line in f:
                            stripped = line.strip()
                            if stripped and not stripped.startswith("#"):
                                total_lines += 1
                except Exception as e:
                    print(f"Could not read {filepath}: {e}")

    print(f"Total lines of code (excluding comments and blanks): {total_lines}")

count_code_lines("C:/Users/deepa/New folder")

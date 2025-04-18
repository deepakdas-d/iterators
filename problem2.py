# Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.
# def line(file, n=40):
#     with open(file, 'r') as f:
#         for line in f:
#             if len(line.strip()) > n:
#                 print(line.strip())

# lin=['sample.txt','sample2.txt']
# for i in lin:
#     n=line(i)
#     print(n)


import sys

try:
    def line(filen, n=40):
        with open(filen, 'r') as f:
            for line in f:
                if len(line.strip()) > n:
                    print(f"{filen}: {line.strip()}")
except FileNotFoundError:
    print(f"File  not found.") 

filen= sys.argv[1:]
for f in sys.argv[1:]:
    line(f)
    # output
#sample.txt: "The quick brown fox jumps over the lazy dog near the riverbank."
# sample.txt: "In the heart of the forest, silence speaks louder than words."
# sample.txt: "Programming in Python can be both fun and powerful when you get the hang of it."
# sample2.txt: This line is definitely going to be longer than forty characters because it's quite wordy.
# sample2.txt: Yet another long line that will pass the forty character threshold easily.

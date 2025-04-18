# The built-in function enumerate takes an iteratable and returns an iterator over pairs (index, value) for each value in the source.
lst = ['a', 'b', 'c']

for index, value in enumerate(lst):
    print(f"Index: {index}, Value: {value}")

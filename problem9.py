# The built-in function enumerate takes an iteratable and returns an iterator over pairs (index, value) for each value in the source.
lst = ['a', 'b', 'c']

for index, value in enumerate(lst):
    print(f"Index: {index}, Value: {value}")
####Output
#Index: 0, Value: a
# Index: 1, Value: b
# Index: 2, Value: c
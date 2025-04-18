#Implement a function izip that works like itertools.izip.
def izip_two(iterable1, iterable2):
    # Create iterators for the two input iterables
    iter1 = iter(iterable1)
    iter2 = iter(iterable2)
    
    while True:
        try:
            # Get the next item from both iterators
            yield (next(iter1), next(iter2))
        except StopIteration:
            # If any iterator is exhausted stop
            return

a = [1, 2, 3]
b = ['a', 'b', 'c']

for item in izip_two(a, b):
    print(item)
######OUTPUT
#(1, 'a')
# (2, 'b')
# (3, 'c')
#
#
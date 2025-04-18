# Write a function peep, that takes an iterator as argument and returns the first element and an equivalant iterator.
from itertools import chain

def peep(iterable):
    it = iter(iterable)
    try:
        first = next(it)
    except StopIteration:
        raise ValueError("Iterator is empty")

    # Use chain to put the first item back in front
    new_iter = chain([first], it)
    return first, new_iter

it = iter([10, 20, 30])
first, new_it = peep(it)

print("First item:", first)
print("Remaining items:", list(new_it))




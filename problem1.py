#Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction.

class reverse_iter:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            n = self.n
            self.n -= 1 # we decrement the given n value.
            return n
        else:
            raise StopIteration()
#n=list(reverse_iter(5))
#output
# [5, 4, 3, 2, 1]
ls=[1,2,3,4,5]
i=reverse_iter(len(ls))
print(next(i))#5

print(next(i))#4

print(next(i))#3

print(next(i))#2

print(next(i))#1

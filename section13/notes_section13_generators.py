# yield is used to create a generator. A generator is a special type of iterator that generates values on the fly and can be iterated over. When a function contains a yield statement, it becomes a generator function. When called, it returns a generator object that can be iterated over.

def create_cubes(n):
    for x in range(n):
        yield x**3

for x in create_cubes(11):
    print(x)

print("\n\n")

def gen_fibon(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in gen_fibon(10):
    print(num)
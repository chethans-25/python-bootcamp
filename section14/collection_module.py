
print("Counter Example:")
# Counter
from collections import Counter

my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
a = Counter(my_list)

print(a)
print(type(a))

str_list = "hello hello, how how are you are you doing today?"
b = Counter(str_list.lower().split())
print(b)


print("DefaultDict Example:")
# defaultdict
from collections import defaultdict
my_dict = defaultdict(lambda: "Not Found")
my_dict['a'] = "Found"
print(my_dict['a'])
print(my_dict['b'])
print(type(my_dict))


print("NamedTuple Example:")
# namedtuple
from collections import namedtuple
Dog = namedtuple('Dog', ['age', 'name'])
my_dog = Dog(age=5, name='Buddy')
print(my_dog)
print(type(my_dog)) //Dog

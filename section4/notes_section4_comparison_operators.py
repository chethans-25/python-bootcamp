# comparison operators are used to compare values and return a boolean result (True or False)

# equal to (==)
print(5 == 5)  # True
print(5.0 == 5)  # True (because 5.0 is considered equal to 5)

# not equal to (!=)
print(5 != 3)  # True

# greater than (>)
print(5 > 3)  # True

# less than (<)
print(5 < 10)  # True

# greater than or equal to (>=)
print(5 >= 5)  # True

# less than or equal to (<=)
print(5 <= 10)  # True

# comparison operators can also be used with strings
print("hello" == "hello")  # True
print("hello" != "world")  # True
print("apple" > "banana")  # False (because 'a' comes before 'b' in the alphabet)
print("apple" < "banana")  # True
print("apple" >= "apple")  # True
print("apple" <= "banana")  # True


# comparison operators can also be used with other data types, such as lists
print([1, 2, 3] == [1, 2, 3])  # True
print([1, 2, 3] != [4, 5, 6])  # True
print([1, 2, 3] > [4, 5, 6])  # False (because the first element of the first list is less than the first element of the second list)
print([1, 2, 3] < [4, 5, 6])  # True
print([1, 2, 3] >= [1, 2, 3])  # True
print([1, 2, 3] <= [4, 5, 6])  # True


multiple_comparisons = 5 > 3 > 1  # True (5 is greater than 3 and 3 is greater than 1)
# less common but also valid
# use logical operators to combine multiple comparisons for readability

# Logical operators can be used to combine comparison operators
print(5 > 3 and 5 < 10)  # True (both conditions are true)
print(5 > 3 or 5 < 10)  # True (at least one condition is true)
print(not (5 > 3))  # False (the condition is true, so not makes it false)


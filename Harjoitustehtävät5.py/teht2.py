numbers = [1, 2, 3, 4, 5]
print(numbers[-2])

numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
numbers3 = numbers1 + numbers2
print(numbers1)
print(numbers2)
print(numbers3)

numbers4 = [1, 2, 3]
numbers5 = [10, 20, 30]
numbers5 += numbers4
print(numbers4)
print(numbers5)

numbers7 = [1, 2, 3, 4, 5]
my_list = numbers7[:]
print(my_list)
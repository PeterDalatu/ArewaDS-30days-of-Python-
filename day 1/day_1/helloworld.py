# Question 1
#python --version

# Question 2
a = 3
b = 4

sum = a + b
print(sum)

sub = a - b
print(sub)

mul = a * b
print(mul)

mod = a % b
print(mod)

div = a / b
print(div)

exp = a ** b
print(exp)

fdiv = a // b
print(fdiv)

# Question 3
a = "My name is Peter Dalatu"
print(a)
b = "The name of my family is Dalatu"
print(b)
c = "My country is Nigeria"
print(c)
d = "I am enjoying 30 days of python"
print(d)


# Question 4
data = [
    10,
    9.8,
    3.14,
    4 - 4j,
    ['Asabeneh', 'Python', 'Finland'],
    'Peter Dalatu',
    'Dalatu',
    'Nigeria'
]

for i in data:
    print(f'The data type of {i} is {type(i)}')
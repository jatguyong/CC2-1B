#assigning variables

name = input("What is your name? ")
age_input = input("What is your age? ")

age = int(age_input)

print("Hello " + name)
print("Hello", name)
print(f"Hello {name}")
print(f"My age next year is {(age + 1)}")

modulo = 5%3
pi = 3.1415

print(f"5 modulo 3 is {modulo}")
print(f"The pi value is {pi}")

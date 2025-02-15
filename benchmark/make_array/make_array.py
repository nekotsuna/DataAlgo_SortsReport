import random

max_value = 10 ** 9
equal_value = 100
num1 = 1
num2 = 2

def random_case(length):
    seed = random.randint(0, 99999)
    random.seed(seed)
    array = [random.randint(0, max_value) for _ in range(length)]
    return array, seed

def ascend_case(length):
    seed = random.randint(0, 99999)
    random.seed(seed)
    array = [random.randint(0, max_value) for _ in range(length)]
    return sorted(array), seed

def descend_case(length):
    seed = random.randint(0, 99999)
    random.seed(seed)
    array = [random.randint(0, max_value) for _ in range(length)]
    return sorted(array, reverse=True), seed

def equal_case(length):
    array = [equal_value for _ in range(length)]
    return array, seed

def jagg_case(length):
    array = []
    for i in range(1, (length // 2) + 1):
        array.append(length - i + 1)
        array.append(i)
    if length % 2 == 1:
        array.append((length // 2) + 1)
    return array

def separate_case(length):
    array = []
    half_length = length // 2
    array.extend([num1] * half_length)
    array.extend([num2] * half_length)
    if length % 2 == 1:
        array.append(num2)
    return array

def generate_case():
    print("R: random")
    print("A: ascend")
    print("D: descend")
    print("E: equal")
    print("J: jagg")
    print("S: separate")

    choice = input("Enter case:")
    length = int(input("Enter length:"))

    array = [0] * length
    seed

    if choice == 'R':
        array, seed = random_case(length)
    elif choice == 'E':
        array, seed = equal_case(length)
    elif choice == 'A':
        array, seed = ascend_case(length)
    elif choice == 'D':
        array, seed = descend_case(length)
    elif choice == 'J':
        array = jagg_case(length)
    elif choice == 'S':
        array = separate_case(length)
    else:
        print("Invalid input")

    return array

print(generate_case())
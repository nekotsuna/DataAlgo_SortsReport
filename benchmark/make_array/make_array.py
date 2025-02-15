import random

max_value = 10 ** 7
duplication_max_value = 10
equal_value = 1
num1 = 1
num2 = 2

def random_case(length):
    seed = random.randint(0, 10000)
    random.seed(seed)
    array = [random.randint(0, 10 ** 7) for _ in range(length)]
    return array, seed

def ascend_case(length):
    seed = random.randint(0, 10000)
    random.seed(seed)
    array = [random.randint(0, 10 ** 7) for _ in range(length)]
    return sorted(array), seed

def descend_case(length):
    seed = random.randint(0, 10000)
    random.seed(seed)
    array = [random.randint(0, 10 ** 7) for _ in range(length)]
    return sorted(array, reverse=True), seed

def equal_case(length):
    seed = random.randint(0, 10000)
    random.seed(seed)
    array = [equal_value for _ in range(length)]
    return array, seed

def jagg_case(length):
    seed = random.randint(0, 10000)
    random.seed(seed)
    array = []
    for i in range(1, (length // 2) + 1):
        array.append(length - i + 1)
        array.append(i)
    if length % 2 == 1:
        array.append((length // 2) + 1)
    return array, seed

def separate_case(length):
    seed = random.randint(0, 10000)
    random.seed(seed)
    array = []
    half_length = length // 2
    array.extend([1] * half_length)
    array.extend([2] * half_length)
    if length % 2 == 1:
        array.append(2)
    return array, seed

def duplication_case(length):
    seed = random.randint(0, 10000)
    random.seed(seed)
    array = [random.randint(0, 10) for _ in range(length)]
    return array, seed

def generate_case():
    print("R: random")
    print("A: ascend")
    print("D: descend")
    print("E: equal")
    print("J: jagg")
    print("S: separate")
    print("D: duplication")

    choice = input("Enter case:")
    length = int(input("Enter length:"))

    array = [0] * length
    seed = 0

    if choice == 'R':
        array, seed = random_case(length)
    elif choice == 'E':
        array, seed = equal_case(length)
    elif choice == 'A':
        array, seed = ascend_case(length)
    elif choice == 'D':
        array, seed = descend_case(length)
    elif choice == 'J':
        array, seed = jagg_case(length)
    elif choice == 'S':
        array, seed = separate_case(length)
    elif choice == 'D':
        array, seed = duplication_case(length)
    else:
        print("Invalid input")

    return array, seed

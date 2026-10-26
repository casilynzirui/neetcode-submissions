def add_two_numbers() -> int:
    numbers = input()
    two_numbers = numbers.split(",")

    add_numbers = int(two_numbers[0]) + int(two_numbers[1])

    return add_numbers



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

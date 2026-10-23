def reverse_string(input_string: str) -> str:
    reversed_string = ""

    for char in input_string:
        reversed_string = char + reversed_string

    return reversed_string

# do not modify below this line
print(reverse_string("NeetCode"))
print(reverse_string("Hello!"))
print(reverse_string("Bye Bye"))

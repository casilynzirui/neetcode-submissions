from typing import List

def read_integers() -> List[int]:
    integers = input()
    integer_list = integers.split(",")

    for i in range(len(integer_list)):
        integer_list[i] = int(integer_list[i])

    return integer_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

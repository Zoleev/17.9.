def sort(my_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                swapped = True
    return my_list

def binary_search(nums, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if nums[middle] == element:
        return middle
    elif element < nums[middle]:
        return binary_search(nums, element, left, middle - 1)
    else:
        return binary_search(nums, element, middle + 1, right)

while True:
    try:
        nums = input('Введите целые числа через пробел: ').split()
        my_list = list(map(int, nums))
        b_array = sort(my_list)
        for i in b_array:
            if i < 0:
                raise Exception
        break
    except ValueError:
        print('Введите целые числа через пробел')
        exit()
    except Exception:
        print('Введите целые числа через пробел')
        exit()
add_num = int(input('Введите любое число: '))
sort(my_list).append(add_num)
print(sort(my_list))

add_num_index = binary_search(sort(my_list), add_num, 0, len(sort(my_list)))
pre = add_num_index - 1
next = add_num_index + 1
print(f'Номер позиции числа {add_num}: {add_num_index}.')

if pre in range(len(sort(my_list))):
    print(f'Номер позиции предыдущего числа: {pre}.')
else:
    print(f'Номер позиции предыдущего числа: {pre}')

if next in range(len(sort(my_list))):
    print(f'Номер позиции следующего числа: {next}.')
else:
    print(f'Номер позиции следующего числа: {next}')

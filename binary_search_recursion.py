def binary_search_recursion(array, item, start, finish):
    if finish >= start:
        mid = (finish + start) // 2
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            return binary_search_recursion(array, item, start, mid + 1)
        else:
            return binary_search_recursion(array, item, mid + 1, finish)
    else:
        return -1


my_list = [1, 5, 9, 7, 3]
print(f'\nIndex of searching item - {binary_search_recursion(my_list, 9, 0, len(my_list))}')
print()

# Write a function called `choose_func` which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list and return the result of it.
# Otherwise, return the result of the second one


def choose_func(nums: list, func1, func2):
    item = all([item >= 0 for item in nums])
    if item:
        result = square_nums(nums)
        return result
    else:
        result_2 = remove_negatives(nums)
        return result_2


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def main():
    # Assertions
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]
    print(choose_func(nums1, square_nums, remove_negatives))
    print(choose_func(nums2, square_nums, remove_negatives))


if __name__ == '__main__':
    main()

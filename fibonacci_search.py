def fibonacci(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_search(m_list, x):
    m = 0
    while fibonacci(m) < len(m_list):
        m = m + 1
    offset = -1
    while fibonacci(m) > 1:
        i = min(offset + fibonacci(m - 2), len(m_list) - 1)
        if x > m_list[i]:
            m = m - 1
            offset = i
        elif x < m_list[i]:
            m = m - 2
        else:
            return i
    if fibonacci(m - 1) and m_list[offset + 1] == x:
        return offset + 1
    return -1


new_list = [10, 22, 30, 44, 56, 58, 60, 70, 100, 110, 130]
x = 56
print(f'Index of searching element: {fibonacci_search(new_list, x)}')

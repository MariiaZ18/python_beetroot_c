def check(input_value):
    open_b = ('([{')
    close_b = (')]}')
    check_dict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    my_list = []

    for i in input_value:
        if i in open_b:
            my_list.append(check_dict[i])
        elif i in close_b:
            if not my_list or i != my_list.pop():
                return f'{input_value} - Unbalanced'
    if not my_list:
        return f'{input_value} - balanced'
    else:
        return f'{input_value} - Unbalanced'


print(check("{45}"))
print(check("{45))}"))
print(check("({{45})}"))
print(check("()[]{}"))

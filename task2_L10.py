# Create a function which takes as input two dicts with structure mentioned above, then computes and returns the total price of stock.

def fun_total_price():
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }
    a = list(stock.values())
    b = list(prices.values())
    keys_for_dict = ["banana", "apple", "orange", "pear"]
    dict_c = {}
    list_1 = []
    for i, j in zip(a, b):
        list_1.append(i * j)

    for key in keys_for_dict:
        for value in list_1:
            dict_c[key] = value
            list_1.remove(value)
            break
    print(f'Stock: {stock}')
    print(f'Prices: {prices}')
    print(f'The total price of stock: {dict_c}')


if __name__ == '__main__':
    fun_total_price()

import requests


def get_weather():
    API_key = "492dd8e724d04bff3ef82290a4edaf5a"
    # city_name = get_city()
    city_name = str(input('Enter city:'))
    w = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric')
    result = w.json()
    return result


def print_weather():
    result = get_weather()
    city = result.get('name')
    main = result.get('main')
    # weather = result.get('weather')
    wind = dict(result.get('wind'))

    speed = wind.get('speed')
    temp = main.get('temp')
    feels = main.get('feels_like')
    degree_sign = u'\N{DEGREE SIGN}'
    f_str = f"Temperature in {city} is {temp}{degree_sign}, feels like {feels}{degree_sign}. Wind speed - {speed} km/h"
    print(f_str)


if __name__ == '__main__':
    print_weather()
    # print(get_weather())

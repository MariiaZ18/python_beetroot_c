# Creating a dictionary.
# Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
# Make the function print out the values of the dictionary to make sure that it works as intended

def make_country(country_n, capital_n) -> dict[str, str]:
    country_dictionary = {'name': country_n, 'capital': capital_n}
    print(f'Country - {country_dictionary.get("name")}, capital - {country_dictionary.get("capital")}')

    return country_dictionary


if __name__ == '__main__':
    make_country(country_n="Czech Republic", capital_n="Prague")

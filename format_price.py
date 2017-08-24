import sys


def format_price(price):

    price = str(round(float(price), 2))
    integer_part, fractional_part = price.split('.')
    integer_part = '{0:,}'.format(int(integer_part)).replace(',', ' ')
    pretty_price = integer_part+'.'+fractional_part
    return pretty_price

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print("Error: Empty argument, try format_price.py <price>")
        exit()
    price = sys.argv[1]
    print(format_price(price))

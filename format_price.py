import sys

def format_price(price):

    price = round(float(price), 2)
    pretty_price = '{0:,.2f}'.format(price).replace(',', ' ')
    return pretty_price

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print("Error: Empty argument, try format_price.py <price>")
        exit()
    price = sys.argv[1]
    print(format_price(price))

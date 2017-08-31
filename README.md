# Price Formatter

This is function that convert prices into pretty looking format.
For example "1999.999" --> "2 000.00"

Run in CLI mode
```
$ python format_price.py 1999.999
> 2 000.00
```
or use it as an external module
```
from format_price import format_price
```
Use tests.py for unit testing with these cases.

0
1000
1000.999
1000.000099
1000.
1000000
00.00
000.1000
.777
-10
abc

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

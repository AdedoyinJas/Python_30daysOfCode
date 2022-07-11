#divmod() is part of python's standard library which takes two numbers as parameters and gives the quotient and remainder of their division as a tuple
#No digits: {:02d} , 1 digit: {:02d} , 2: {:02d} , 3 : {:02d}.format(0,7,42,151)
#result = 00 , 1 digit: 07 ,2:42 , 3:151'
#'\r' = CR (carriage return) used as a new line character in mac os before x ///// moves the cursor to the beginning of the line without advancing to the next line
#'\n' = LF(line Feed) used as a new line character in unix/ mac os ///// moves the cursor to the next line without returning   to the beginning of the line.
#'\r\n' = CR + LF used as a new line c---- in windows///// \r\n (End of line) a combination

import time
def countdown(t):
    while t:
        mins, secs =  divmod(t,60)
        result = "{:02d} : {:02d} " .format (mins, secs)
        print (result, end = "\r")
        time.sleep(1)
        t -= 1
    print('stop!')

countdown(int(10))


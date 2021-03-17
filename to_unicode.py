# COMP 202 Assignment 2 Part 3
# Author: Dailun Li
# Student ID: 260888965
from char_to_braille import *
import doctest

INCOMPLETE = -1


def ostring_to_raisedpos(s):
    ''' (str) -> str
    Convert a braille letter represented by '##\n##\n##' o-string format
    to raised position format. Provided to students. Do not edit this function.

    Braille cell dot position numbers:
    1 .. 4
    2 .. 5
    3 .. 6
    7 .. 8 (optional)

    >>> ostring_to_raisedpos('..\\n..\\n..')
    ''
    >>> ostring_to_raisedpos('oo\\noo\\noo')
    '142536'
    >>> ostring_to_raisedpos('o.\\noo\\n..')
    '125'
    >>> ostring_to_raisedpos('o.\\noo\\n..\\n.o')
    '1258'
    '''
    res = ''
    inds = [1, 4, 2, 5, 3, 6, 7, 8]
    s = s.replace('\n', '')
    for i, c in enumerate(s):
        if c == 'o':
            res += str(inds[i])
    return res 


def raisedpos_to_binary(s):
    ''' (str) -> str
    Convert a string representing a braille character in raised-position
    representation  into the binary representation.
    TODO: For students to complete.

    >>> raisedpos_to_binary('')
    '00000000'
    >>> raisedpos_to_binary('142536')
    '11111100'
    >>> raisedpos_to_binary('14253678')
    '11111111'
    >>> raisedpos_to_binary('123')
    '11100000'
    >>> raisedpos_to_binary('125')
    '11001000'
    '''
    
    # assume there is a string range 8 (01234567) (8 number strings)
    r = ''
    #then the first letter will be range 0
    #second will be range 1
    #......
    for i in range(8):
        #but numbers are from 1-8, not 0-7, so we input i+1
        #and the 'in' requires both to be strings
        if str(i+1) in s:
        #if 1/2/3/4...is in s
        #r will add 1 to the 1st/2nd/3rd/4th...letter    
            r += '1'
        else:
            r += '0'
    return r


def binary_to_hex(s):
    '''(str) -> str
    Convert a Braille character represented by an 8-bit binary string
    to a string representing a hexadecimal number.

    TODO: For students to complete.

    The first braille letter has the hex value 2800. Every letter
    therafter comes after it.

    To get the hex number for a braille letter based on binary representation:
    1. reverse the string
    2. convert it from binary to hex
    3. add 2800 (in base 16)

    >>> binary_to_hex('00000000')
    '2800'
    >>> binary_to_hex('11111100')
    '283f'
    >>> binary_to_hex('11111111')
    '28ff'
    >>> binary_to_hex('11001000')
    '2813'
    '''

    #first, reverset the string, use [::-1]
    reverse_str = s[::-1]
    #change it to hex then to base 10
    hex_func = hex(int(reverse_str, 2))
    #2800 is 10240 in base 10
    p = int(10240) + int(hex_func, 16)
    #then print the final result in base 16
    result = hex(p)[2:]
    return result

def hex_to_unicode(n):
    '''(str) -> str
    Convert a braille character represented by a hexadecimal number
    into the appropriate unicode character.
    Provided to students. Do not edit this function.

    >>> hex_to_unicode('2800')
    '⠀'
    >>> hex_to_unicode('2813')
    '⠓'
    >>> hex_to_unicode('2888')
    '⢈'
    '''
    # source: https://stackoverflow.com/questions/49958062/how-to-print-unicode-like-uvariable-in-python-2-7
    return chr(int(str(n),16))


def is_ostring(s):
    '''(str) -> bool
    Is s formatted like an o-string? It can be 6-dot or 8-dot.
    TODO: For students to complete.
    >>> is_ostring('o.\\noo\\n..')
    True
    >>> is_ostring('o.\\noo\\n..\\noo')
    True
    >>> is_ostring('o.\\n00\\n..\\noo')
    False
    >>> is_ostring('o.\\noo')
    False
    >>> is_ostring('o.o\\no\\n..')
    False
    >>> is_ostring('o.\\noo\\n..\\noo\\noo')
    False
    >>> is_ostring('\\n')
    False
    >>> is_ostring('A')
    False
    '''
    
    #check if there are always two dots in between
    if len(s) != 8 and len(s) != 11:
            return False
        

    dot_left = 2
    # use numbers to represent '.' and 'o' in a string
    for i in s:
    # from left.s to right.s
        if i != 'o' and i != '.' and i != '\n':
            return False
    # the term \n should be considered separately because it may appear at an unusual place
        elif i == '\n':
            dot_left = 2
    # everytime back to \n, there are 2 dots waiting for evaluation
    # if i is not \n, then go to else
        else:
            dot_left -= 1
    # when there are more than 2 dots in a role
    # dot_left will be < 0
    # once dot_left < 0, the program evaluate to False
            if dot_left < 0:
                return False
    #if if pass the test then return True
        
       
    return True

def ostring_to_unicode(s):
    '''
    (str) -> str
    If s is a Braille cell in o-string format, convert it to unicode.
    Else return s.

    Remember from page 4 of the pdf:
    o-string -> raisedpos -> binary -> hex -> Unicode

    TODO: For students to complete.

    >>> ostring_to_unicode('o.\\noo\\n..')
    '⠓'
    >>> ostring_to_unicode('o.\\no.\\no.\\noo')
    '⣇'
    >>> ostring_to_unicode('oo\\noo\\noo\\noo')
    '⣿'
    >>> ostring_to_unicode('oo\\noo\\noo')
    '⠿'
    >>> ostring_to_unicode('..\\n..\\n..')
    '⠀'
    >>> ostring_to_unicode('a')
    'a'
    >>> ostring_to_unicode('\\n')
    '\\n'
    '''
    if is_ostring(s) == True:
        return hex_to_unicode(binary_to_hex(raisedpos_to_binary(ostring_to_raisedpos(s))))
    else:
        return s
    

if __name__ == '__main__':
    doctest.testmod()

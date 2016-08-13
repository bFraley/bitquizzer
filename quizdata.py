# quizdata.py -  bitquizzer - Interactive quizzer for bitwise practice.
# Copyright by Brett Fraley 2016

menu = [
    '*******************************************',
    'Bit Quizzer - Interactive Bitwise Practice\n',
    'Return to this menu by typing --> menu',
    'Close this program by typing  --> quit\n',
    '1. Memorize Powers',
    '2. Binary 1-20',
    '\nChoose a menu option to begin\n'
]

quizinfo = {
    'base2':
        ['Base 2 Powers 0-10',
        '\nType the integer value of the base 2 power.\n'],

    'bincount':
        ['Binary Numbers 1-20',
        '\nType the binary number of the given integer. Use 0b format.\n']
}

base2 = {
    '2**0':1,
    '2**1':2,
    '2**2':4,
    '2**3':8,
    '2**4':16,
    '2**5':32,
    '2**6':64,
    '2**7':128,
    '2**8':256,
    '2**9':512,
    '2**10':1024
}

bincount20 = {
    '1':0b01,
    '2':0b10,
    '3':0b11,
    '4':0b100,
    '5':0b101,
    '6':0b110,
    '7':0b111,
    '8':0b1000,
    '9':0b1001,
    '10':0b1010,
    '11':0b1011,
    '12':0b1100,
    '14':0b1110,
    '15':0b1111,
    '16':0b10000,
    '17':0b10001,
    '18':0b10010,
    '19':0b10011,
    '20':0b10100
}
                        

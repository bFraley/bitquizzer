bincount = {
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

run = True
correct = 0

while run:
    for key in bincount:
        ans = input(key + ": ")

        if ans == bin(bincount[key]):
            print("Correct")
            correct += 1
        else:
            print("Incorrect Answer")
            correct = 0

    # This program ends once 100 correct answers are given in a row!

    if correct == 100:
        run = False

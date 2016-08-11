# This only includes Powers of 2 Memorization for now.
# Copyright by Brett Fraley 2016

powers_of_2 = {
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

run = True
correct = 0

while run:
    for key in powers_of_2:
        ans = input(key + ": ")
        
        if int(ans) == powers_of_2[key]:
            print("Correct")
            correct += 1
        else:
            print("Incorrect Answer")
            correct = 0

    # This program ends once 100 correct answers are given in a row!

    if correct == 100:
        run = False

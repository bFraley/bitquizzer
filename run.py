#!/usr/bin/env python3

# run.py -  bitquizzer - Interactive quizzer for bitwise practice.
# Copyright by Brett Fraley 2016

import quizlib
import quizdata
import dialogue

def bitquizzer():

    correct = 0
    program_data = 0
    run = True

    # Methods that check quiz answers.
    check = quizlib.AnswerCheck('default')

    # Print menu.
    for line in dialogue.menu:
        print(line) 

    # Prompt for option.
    option = quizlib.prompt('Option # ')   
    
    if option == '1':
        program_data = quizdata.base2
        check_answer = check.base2

    elif option == '2':  
        program_data = quizdata.bincount20
        check_answer = check.bincount

    print('Starting %s' % program_data['name'])
    print(program_data['howto'])

    while run:
               
        for key in program_data:
            if key == 'howto':
                break

            if key == 'name':
                break
            
            ans = quizlib.prompt(key + ": ")

            if ans == 'quit':
                exit(0)

            elif check_answer(ans, program_data[key]):
                print("Correct")
                correct += 1
            else:
                print("Incorrect Answer")
                correct = 0

        # This program ends once 100 correct answers are given in a row!
        if correct == 100:
            run = False


bitquizzer()


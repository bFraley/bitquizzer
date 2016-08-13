#!/usr/bin/env python3

# run.py -  bitquizzer - Interactive quizzer for bitwise practice.
# Copyright by Brett Fraley 2016

import os
import quizlib
import quizdata
import dialogue

os.system('clear')

def bitquizzer():

    correct = 0
    program_data = 0
    run = True
    repeated = []

    # Methods that check quiz answers.
    check = quizlib.AnswerCheck('default')

    # Print menu.
    for line in dialogue.menu:
        print(line) 

    # Prompt for option.
    option = quizlib.prompt('Option # ')
    
    # Check for 'quit' keyword, exit program.
    if option == 'quit':
        exit(0)

    # Reset if zero or invalid input.
    if len(option) < 1 or not option.isdigit():
        return bitquizzer()         
    
    # Get the quiz option number.
    if option == '1':
        quiz_name = 'base2'
        program_data = quizdata.base2
        check_answer = check.base2

    elif option == '2': 
        quiz_name = 'bincount'
        program_data = quizdata.bincount20
        check_answer = check.bincount
    
    # Launch the quiz.
    os.system('clear')
    print('Starting %s' % quizdata.quizinfo[quiz_name][0])
    print(quizdata.quizinfo[quiz_name][1])

    # Quiz runtime loop.
    while run:

        for key in program_data:

            # Get answer and check if correct.
            ans = quizlib.prompt(key + ": ")
            len_ans = len(ans)

            # Break if zero input or excessive input > 40.
            if len_ans < 1 or len_ans > 40:
                break
           
            # Check for 'menu' keyword, return to menu.
            if ans == 'menu':
                os.system('clear')
                return bitquizzer()
       
            # Check for 'quit' keyword, exit program.
            if ans == 'quit':
               exit(0)

            # Verify answer.
            elif check_answer(ans, program_data[key]):
                print("Correct\n")
                correct += 1
            else:
                print("Incorrect\n")
                correct = 0

        # Quiz ends once 100 correct answers are given in a row!
        if correct == 100:
            os.system('clear')
            return bitquizzer()

bitquizzer()


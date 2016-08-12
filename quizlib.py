# quizlib.py -  bitquizzer - Interactive quizzer for bitwise practice.
# Copyright by Brett Fraley 2016

#-----------------
# Helper Functions
#-----------------

# Prompt user for input.
# @param - Accepts a [msg] string.

def prompt(msg):
    return input(msg)

# Compare two strings.
# @param - Accepts 2 strings [string1, string2].

def compare_strings(string1, string2):
    if string1 == string2:
        return True
    else:
        return False

# Compare integer string to an integer.
# @param - Accepts [string integer] [int].

def compare_intstring_to_int(intstring, intnum):
    if int(intstring) == intnum:
        return True
    else:
        return False

# Compare float string to a float.
# @param - Accepts [string float] [float].

def compare_floatstring_tofloat(floatstring, floatnum):
    if float(floatstring) == floatnum:
        return True
    else:
        return False


# Evaluate answers in different quiz program contexts.

class AnswerCheck():
    def __init__(self, quizname):
        self.quizname = quizname

    def base2(self, answer, data):
        if int(answer) == data:
            return True
        else:
            return False

    def bincount(self, answer, data):
        if answer == bin(data):
            return True
        else:
            return False


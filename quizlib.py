# Interactive Quizzer for Bitwise Practice, in Python
# Brett Fraley 2016

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

def compare_intstring_to_int(numstring, intnum):
    if int(numstring) == num:
        return True
    else:
        return False

# Compare float string to a float.
# @param - Accepts [string float] [float].

def compare_floatstring_tofloat(floatstring, floatnum):
    if float(floatstring == floatnum):
        return True
    else:
        return False

#---------------
# Menu
#---------------

class Menu():
    def __init__(self):
        self.stars = "******************************************"
        self.title = "Bit Quizzer - Iteractive Bitwise Practice"
        self.options = [
            "1. Memorize Powers",
            "2. Head Count"
        ]




        
        
           

        



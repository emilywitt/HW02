#!/usr/bin/env python
# HW02_ex03_05

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated
# sequence:

# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the 
# value printed next appears on the same line.

# print '+', 
# print '-'

# The output of these statements is '+ -'.

# A print statement all by itself ends the current line and goes to the next line.

# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def half_line_one():
    print '+ - - - -',

def half_line_two():
    print '|        ',

def full_line_one():
    do_twice(half_line_one)
    print '+'

def full_line_two():
    do_twice(half_line_two)
    print '|'

def draw_row():
    full_line_one()
    do_four(full_line_two)

def draw_small_grid():
    do_twice(draw_row)
    full_line_one()

draw_small_grid()

def double_line_one():
	do_four(half_line_one)
	print '+'

def double_line_two():
	do_four(half_line_two)
	print '|'

def draw_double_row():
	double_line_one()
	do_four(double_line_two)

def draw_double_columns():
	do_twice(draw_double_row)

def draw_large_grid():
	do_twice(draw_double_columns)
	double_line_one()

draw_large_grid()







# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    



if __name__ == "__main__":
    main()
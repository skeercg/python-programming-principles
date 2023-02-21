'''
For your assignment, please use the code below first and then write your code.
DO NOT DELETE THE FOLLOWING CODE
'''
import sys
try:
    input1 = sys.argv[1]
    input2 = sys.argv[2]
except:
    print("You didn't put any input when you run your code! Please add an input!")
'''
The objective of this assignment is to print the calculations of the input1 and input2.
Several tests will be done with your file with several inputs.
You can find them in the instruction document.
You can write you code after this comment :
'''

#Your code here:
input1 = int(input1)
input2 = int(input2)
print(input1, '+', input2, '=', input1 + input2)
print(input1, '-', input2, '=', input1 - input2)
print(input1, '*', input2, '=', input1 * input2)
print(input1, '/', input2, '=', input1 / input2)

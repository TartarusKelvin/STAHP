# STAHP
stahp is a pure stack oriented programming language, currently implemented in python. 

# How to use STAHP
Simply run python on main.py there are no dependancies apart from python 3. 
To exit stahp write \\\\ each token is read from the right of the line to the left
and each token is added to the stack for instance 1 2 3 will add 3 to the stack then 
2 and then 1. operators are also added onto the stack in a similar fashion by default 
when an operator enters the stack it is executed immediatly however to defer execution
append a ` infront of the operator. The full list of operators are below. 

The stack itself is emptied after every new line, to save data of the stack 
use > and < to box and unbox data. E.g > vara 1 2 3 will create a variable vara with the contents
1 2 3 the stack is emptied after >. To unbox simply do < a  which will put 1 2 3 back on the stack.

# Operators

- "." print the top of the stack
- ";" print the entire stack
- "\\\\" exit
- "+" add the top two numbers of the stack
- "*" multiply the top two numbers of the stack
- "_" remove the top element from the stack
- ">" box
- "<" unbox
- "¬" replay the stack removing one layer of deffered. (i.e ¬ `+ 1 2 will result in 3)
- "'" unbox the top element in the stack infront of each element and apply ¬
- "/" same as above except does not unbox for the last element

# Example Programs

## Calculating 5 Factorial
To calculate factorial we can simply use / `* 1 2 3 4 5

## Defining Custom functions
You can add your function to the stack using defered then box into a function name. If you then want to call the function then unbox the function and call ¬
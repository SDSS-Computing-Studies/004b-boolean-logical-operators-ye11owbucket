#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger

You can use an if statement to determine which is larger, or use the
max() function to determine the larger of the two
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
y = float(input("Enter a number: "))
x = float(input("Enter another number: "))
list1 = [x,y]
list1.sort()
a = list1[1]
wabungus = list1[0]
if a%wabungus == 0:
    print(int(wabungus), "is a factor of", int(a))
else:
    print (int(wabungus), "is not a factor of", int(a))
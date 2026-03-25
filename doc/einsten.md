CSE 231 Spring 2008
Programming Project #2
Assignment Overview
This project focuses on some mathematical manipulation, in particular integer operations. It is
worth 20 points (2% of your overall grade). It is due Monday, January 21st before midnight.
The Problem
(from the Handley Math Page,
http://141.104.22.210/Div/Winchester/jhhs/math/puzzles/mtricks.html)
It is said that Albert Einstein used to take great delight in baffling friends with the puzzle below.
First, write the number 1089 on a piece of paper, fold it, and hand it to a friend for safekeeping.
What you wrote down is not to be read until you have completed your amazing mental feat.
Next, ask your friend to write down any three-digit number, emphasizing that the first and last
digits must differ by at least two. Close your eyes or turn your back while this is being done.
Better still, have someone blindfold you.
After your friend has written down the three-digit number, ask him to reverse it, then subtract the
smaller from the larger.
Example: 654 - 456 = 198.
Once this is done, tell your friend to reverse the new number.
Example: 198 becomes 891.
Next ask your friend to add the new number and its reverse together.
Example: 198 + 891 = 1089.
If all goes as planned, your friend will be amazed. The number you wrote down at the start --
1089 -- will always be the same as the end result of this mathematical trick.
Program Specifications
Your program will play the Einstein game as follows:
1. Print a message to the user about the game and explain the rules
2. Prompt the user for a 3 digit number as described
3. print out user number and the reverse of that number
4. print out the difference between the entered number and the reversed number. This
should always be a positive number.
5. print the reverse of the difference
6. print the sum of the difference and the reversed difference. It should be 1089 for any 3
digit number
Deliverables
proj02.py -- your source code solution (remember to include your section, the date, project
number and comments).
1. Please be sure to use the specified file name, i.e. “proj02.py”
2. Save a copy of your file in your CS account disk space (H drive on CS computers).
3. Electronically submit a copy of the file.
Assignment Notes:
One of the main issues here is that we are working with integers, and division with integer
numbers is a little different.
Integer division always returns an integer result. Thus 10/3 yields 3. The operation 4/5 yields
0.
There is another operator, called the modulus operator, which indicates the remainder after a
division. The modulus operator is indicated by the % sign. Thus 10%3 is 1 (a remainder of 1).
4%5 is 4.
You can use these facts to gather the digits in the hundred’s, ten’s and one’s place of a three digit
integer, and then reverse it. Try some experiments in the Python interpreter to see how to
accomplish this task.
One other problem. The specification mentions that we should always subtract the smaller of the
two numbers (the user number or its reverse) from the larger. Another way to do this is to take
the absolute value of any subtraction. The absolute value function is called abs in Python.
Thus abs(-27) yields 27. abs(45) yields 45
To clarify the problem specifications, we provide at the end of this document a snapshot of
interaction with the already written program.
Getting Started
1. Using IDLE create a new program.
2. If you are in a CSE lab, select the H: drive as the location to store your file
3. Save the name of the project: proj02.py
4. Create the preface print information and prompt for the user integer
5. Run the program and fix any errors
6. Use the web site to hand in the program (incomplete as this point but you should continually
hand things in)
7. Now, take the user number and isolate the three digits in the number
8. Given you can find those digits, you can create the reverse of the number
9. Now you enter a cycle of edit-run to incrementally develop your program.
10. Hand in your final version.
Questions for you to consider (not hand in)
1. What happens when enter a three digit number that does not differ by at least two in the
hundred’s and one’s digit?
2. What happens when you enter a letter instead of a number at the prompt?
Sample Interaction
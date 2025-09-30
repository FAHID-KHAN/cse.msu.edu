CSE 231 Spring 2010
Programming Project #2
Assignment Overview
This project focuses on some mathematical manipulation, in particular integer operations. It is
worth 20 points (2% of your overall grade). It is due Monday, January 25th before midnight.
The Problem (from the Handley Math Page,
http://141.104.22.210/Div/Winchester/jhhs/math/puzzles/mtricks.html)
Visitors, especially young ones, often waited for General Douglas MacArthur to perform a
miracle, or at least utter something profound, when they met him. The General could not always
live up to his press notices.
So, MacArthur started using a mathematical trick that he described as "the old number 115" as a
way to maintain his image, have some fun, and mystify his guests.
Ask your friend to write down the number of month in which he was born. (January is 1,
February is 2, and so on).
Turn your back so you cannot see what your friend is jotting down in response to your
instructions. Then have that person write down:
Month of birth (Example February): 2
Double it: 4
Add 5: 9
Multiply by 50: 450
Add friend's age (Example 40): 490
Subtract 365: 125
At this point, ask your friend to call out the total, which in this case, is 125. In your head, quickly
and secretly add 115. In this example, you will end up with 240. Then proclaim, "Why, you were
born in February and you're 40 years old."
Here's how he did it. The first number—and the second if the total is a four-digit number—will
indicate your friend's birth month, once you've added good old 115. The last two digits will
indicate his age.
Program Specifications
Your program will play the MacArthur game as follows:
1. Print a message to the user about the game and explain the rules
2. Prompt the user for both a birth month (1 for Jan, 2 for Feb etc.) and their age.
3. Print out the “special” number that results from the algorithm above.
4. Add 115 to the number, and find the value of the last two digits (age) and the first one or
two digits (birth month).
5. Print out the birth month and the age of the player
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
integer. Try some experiments in the Python interpreter to see how to accomplish this task.
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
7. Now, prompt for the two numbers and convert to integers (birth month and age).
8. Perform the calculations.
9. Separate the last two numbers from the sum (how to do that)? Print those numbers.
10. Now you enter a cycle of edit-run to incrementally develop your program.
11. Hand in your final version.
Questions for you to consider (not hand in)
1. What happens when enter a non-number as a month or age?
2. What happens when you enter an integer age larger than 99?
Sample Interaction
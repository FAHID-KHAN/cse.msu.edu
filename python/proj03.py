# CSE 231, Fall 2007
# Programming Project 03
# Section:  
# Date: February 4, 2026
#
# A simple calculator that supports +, -, *, and / with floating-point operands.
# It continues prompting until the user declines to perform another calculation.

try:
    raw_input  # type: ignore[name-defined]
except NameError:  # Python 3 compatibility
    raw_input = input  # type: ignore[assignment]


def main():
    keep_going = True

    while keep_going:
        expr = raw_input("Enter an expression (operand operator operand): ")

        try:
            left_str, op, right_str = expr.split()
            left = float(left_str)
            right = float(right_str)
        except ValueError:
            print("Error: illegal operand or missing spaces.")
        else:
            if op == "+":
                print(left + right)
            elif op == "-":
                print(left - right)
            elif op == "*":
                print(left * right)
            elif op == "/":
                if right == 0.0:
                    print("Error: division by zero.")
                else:
                    print(left / right)
            else:
                print("Error: illegal operator.")

        choice = raw_input("Another calculation? (y/yes to continue): ")
        choice = choice.strip().lower()
        keep_going = choice in ("y", "yes")


if __name__ == "__main__":
    main()
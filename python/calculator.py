try:
    raw_input 
except NameError:
    raw_input = input 


def main():
    keep_going = True 
    
    while keep_going:
        expr = raw_input("Enter an expression (operand operator operand): ")

        try:
            left_str,op,right_str = expr.split()
            left = float(left_str)
            right = float(right_str)
        except ValueError:
            print("Error: illegal operand or missing spaces")
        else:
            if op == "+":
                print(left + right)
            elif op == "-":
                print(left-right)
            elif op == "*":
                print(left * right)
            elif op == "/":
                if right == 0.0:
                    print("Error: division by zero")
                else:
                    print(left/right)
            else:
                print("Error: illegal operator")
        
        choice = raw_input("Another calculation? (y/yes to continue): ")
        choice = choice.strip().lower()
        keep_going = choice in ("y","yes")

if __name__ == "__main__":
    main()



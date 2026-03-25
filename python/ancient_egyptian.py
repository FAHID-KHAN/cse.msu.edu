# CSE 231, Spring 2008
# Programming Project 03
# Ancient Egyptian Multiplication Algorithm
# Date: January 28th
# This program implements the Russian Peasant/Ancient Egyptian multiplication method

def get_user_input():
    """Get two integers from user input."""
    input_str = input("Please input the 2 numbers separated by a space:")
    numbers = input_str.split()
    a = int(numbers[0])
    b = int(numbers[1])
    return a, b

def prepare_values(a, b):
    """Handle negative numbers and return absolute values with negative count."""
    negative_count = 0
    if a < 0:
        negative_count += 1
        a = -a
    if b < 0:
        negative_count += 1
        b = -b
    return a, b, negative_count

def ancient_egyptian_multiply(a, b, original_a):
    """Perform the Ancient Egyptian multiplication algorithm."""
    print("A =", original_a, "and B =", b)
    product = 0
    
    while b > 0:
        if b % 2 == 1:
            product += a
            print("B was odd, we add A to make the product:", product)
        
        a = a * 2
        b = b // 2
        
        if b > 0:
            print("A =", a, "and B =", b)
    
    return product

def determine_sign(product, negative_count):
    """Determine and apply the sign of the final product."""
    if product == 0:
        print("Product is zero")
        return 0
    elif negative_count == 1:
        print("Product is negative")
        return -product
    else:
        print("Product is positive")
        return product

def ask_continue():
    """Ask user if they want to continue and validate input."""
    continue_calc = input("Do you want to continue?(y/n)")
    
    if continue_calc == 'y' or continue_calc == 'Y':
        print("====================================================")
        return True
    elif continue_calc == 'n' or continue_calc == 'N':
        print("Thank you for using the Ancient Egyptian calculator!")
        return False
    else:
        print("Bad input, quitting")
        return False

def main():
    """Main program loop."""
    while True:
        # Get input
        a, b = get_user_input()
        original_a = a
        
        # Prepare values (handle negatives)
        a, b, negative_count = prepare_values(a, b)
        
        # Perform multiplication
        product = ancient_egyptian_multiply(a, b, original_a)
        
        # Determine final sign and value
        final_product = determine_sign(product, negative_count)
        
        # Print result
        print("The product of the two numbers is:", final_product)
        
        # Ask to continue
        if not ask_continue():
            break

# Run the program
if __name__ == "__main__":
    main()
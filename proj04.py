"""
CSE 231 Fall 2013
Computer Project #4
Bank Transaction Processing System
"""

def get_number(one_line):
    """
    Extract and return the account number from one line of the master file.
    Account number is the first 6 characters.
    """
    return one_line[:6]


def get_balance(one_line):
    """
    Extract and return the account balance as a float from one line of the master file.
    Balance is in positions 7-16 (after account number and space).
    """
    # Split the line into parts
    parts = one_line.split()
    # Second part is the balance
    return float(parts[1])


def get_name(one_line):
    """
    Extract and return the account holder's name from one line of the master file.
    Name is everything after the second space (after account number and balance).
    """
    # Find the position after the second space
    first_space = one_line.index(' ')
    second_space = one_line.index(' ', first_space + 1)
    # Everything after the second space is the name
    return one_line[second_space + 1:].strip()


def equal_floats(x_flt, y_flt):
    """
    Compare two floating point values for equality.
    Returns True if the absolute value of their difference is less than 1.0e-8.
    """
    return abs(x_flt - y_flt) < 1.0e-8


def main():
    """
    Main program to process bank transactions.
    """
    # Step 1: Get file prefix from user
    prefix = input("Enter file prefix: ")
    old_filename = prefix + ".old.txt"
    new_filename = prefix + ".new.txt"
    
    # Step 2: Try to open files
    try:
        old_file = open(old_filename, 'r')
        new_file = open(new_filename, 'w')
    except IOError:
        print("Error: Unable to open files.")
        return
    
    # Step 3: Process each customer record
    while True:
        line = old_file.readline().strip()
        
        # Check for sentinel (end of file marker)
        if not line:
            continue
            
        account_number = get_number(line)
        
        if account_number == "999999":
            # Write sentinel to new file and exit
            new_file.write("999999\n")
            break
        
        # Extract customer information
        balance = get_balance(line)
        name = get_name(line)
        
        # Display customer information
        print(f"\n{account_number} {balance:.2f} {name}")
        
        # Step 4: Process transactions for this customer
        account_closed = False
        
        while True:
            transaction_code = input("Transaction code: ").strip().lower()
            
            # Validate transaction code
            if transaction_code not in ['d', 'w', 'c', 'a']:
                print("Error: Invalid transaction code.")
                continue
            
            # Process deposit
            if transaction_code == 'd':
                try:
                    amount = float(input("Amount to deposit: "))
                    
                    if amount < 0:
                        print("Error: Amount cannot be negative.")
                        continue
                    
                    new_balance = balance + amount
                    
                    if new_balance > 9999999.99:
                        print("Error: Deposit exceeds maximum balance.")
                    else:
                        balance = new_balance
                        
                except ValueError:
                    print("Error: Invalid amount.")
            
            # Process withdrawal
            elif transaction_code == 'w':
                try:
                    amount = float(input("Amount to withdraw: "))
                    
                    if amount < 0:
                        print("Error: Amount cannot be negative.")
                        continue
                    
                    new_balance = balance - amount
                    
                    if new_balance < 0.00:
                        print("Error: Insufficient funds.")
                    else:
                        balance = new_balance
                        
                except ValueError:
                    print("Error: Invalid amount.")
            
            # Process close account
            elif transaction_code == 'c':
                if equal_floats(balance, 0.00):
                    account_closed = True
                    break  # Exit transaction loop, don't write to file
                else:
                    print("Error: Account balance must be zero to close.")
            
            # Process advance to next customer
            elif transaction_code == 'a':
                break  # Exit transaction loop
        
        # Step 5: Write updated record to new file (unless account was closed)
        if not account_closed:
            # Format: account_number balance name
            new_file.write(f"{account_number} {balance:.2f} {name}\n")
    
    # Step 6: Close files
    old_file.close()
    new_file.close()


# Execute main program
if __name__ == "__main__":
    main()

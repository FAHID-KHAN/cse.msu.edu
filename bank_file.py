def get_number(one_line):
    return one_line[:6]


def get_balance(one_line):
    parts = one_line.split()
    return float(parts[1])

def get_name(one_line):
    first_space = one_line.index(' ')
    second_space = one_line.index(' ',first_space + 1)
    return one_line[second_space + 1:].strip()

def equal_float(x_flt,y_flt):
    return abs(x_flt - y_flt) < 1.0e-8



def main():
    prefix = input("Enter file prefix: ")
    old_filename = prefix + ".old.txt"
    new_filename = prefix + ".new.txt"

    try:
        old_file = open(old_filename,"r")
        new_file = open(new_filename,"w")
    except IOError:
        print("Error:Unable to open files.")
        return 
    
    while True:
        line = old_file.readline().strip()
        if not line:
            continue

        account_number = get_number(line)
        if account_number == "999999":
            new_file.write("999999\n")
            break

        balance = get_balance(line)
        name = get_name(line)
        print(f"\n{account_number} {balance:.2f} {name}")
        account_closed = False 
        while True:
            transaction_code = input("Transaction code: ").strip().lower()
            if transaction_code not in ["d","w","c","a"]:
                print("Error: invalid transaction code.")
                continue
            if transaction_code == "d":
                try:
                    amount = float(input("Amount to deposit"))
                    if amount < 0:
                        print("Error: Amount cannot be negative ")
                        continue
                    new_balance = balance + amount 
                    if new_balance > 9999999.99:
                        print("Error: Deposit exceeds maximum balance ")
                    else:
                        balance = new_balance
                except ValueError:
                    print("Error: invalid amount")

            elif transaction_code == "w":
                try:
                    amount = float(input("Enter amount to withdraw"))
                    if amount < 0:
                        print("Error: Amount cannot be negative ")
                        continue 
                    new_balance = balance - amount 
                    if new_balance < 0.00:
                        print("Error: Insufficient funds")
                    else:
                        balance = new_balance
                except ValueError:
                    print("Error: Invalid amount ")
            
            elif transaction_code == "c":
                if equal_float(balance,0.00):
                    account_closed = True
                    break
                else:
                    print("Error: Account balance must be zero to close")
            elif transaction_code == "a":
                break
        if not account_closed:
            new_file.write(f"{account_number} {balance:.2f} {name}\n")
    
    old_file.close()
    new_file.close()



if __name__ == "__main__":
    main()
# proj02.py
# CSE 231 - Fall 2013
# Water billing program

def main():
    # loop forever; break on invalid code
    while True:
        code = input("Enter customer code (r, c, i) or other key to quit: ")

        # check for valid code
        if code == 'r' or code == 'c' or code == 'i':
            # get readings
            beginning = int(input("Enter beginning meter reading: "))
            ending = int(input("Enter ending meter reading: "))

            # compute tenths of gallon used
            if ending >= beginning:
                tenths_used = ending - beginning
            else:
                # meter rolled over 1,000,000,000 (tenths)
                tenths_used = (1_000_000_000 - beginning) + ending

            gallons_used = tenths_used / 10.0

            # compute bill
            if code == 'r':
                bill = 5.00 + 0.0005 * gallons_used
            elif code == 'c':
                if gallons_used <= 4_000_000:
                    bill = 1000.00
                else:
                    extra = gallons_used - 4_000_000
                    bill = 1000.00 + 0.00025 * extra
            else:  # code == 'i'
                if gallons_used <= 4_000_000:
                    bill = 1000.00
                elif gallons_used <= 10_000_000:
                    bill = 2000.00
                else:
                    extra = gallons_used - 10_000_000
                    bill = 2000.00 + 0.00025 * extra

            # display results
            print("Customer code:", code)
            print("Beginning meter reading:", beginning)
            print("Ending meter reading:", ending)
            print("Gallons of water used:", gallons_used)
            print("Amount billed: ${:.2f}".format(bill))
            print()  # blank line for readability

        else:
            # invalid code -> stop
            print("Invalid customer code. Exiting.")
            break

if __name__ == "__main__":
    main()

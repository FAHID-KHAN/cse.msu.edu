def calculate_debt_height():
    bill_thickness = 0.0043 # in inches
    inches_per_mile = 63360 # in inches
    distance_to_moon_miles = 238855 # average distance to the moon in miles

    try:
        debt = float(input("Enter the total debt in dollars: "))
        bill = float(input("Enter the denomination of the bill in dollars: "))
        if bill <= 0:
            raise ValueError("Bill denomination must be higher than 0.")
            return
      
        number_of_bills = debt / bill
      
        total_height_inches = number_of_bills * bill_thickness
     
        height_in_miles = total_height_inches / inches_per_mile
   
        moon_ratio = height_in_miles / distance_to_moon_miles
        print(f"Total height of the debt in miles: {height_in_miles:.2f} miles")
        print(f"This is {moon_ratio:.6f} times the distance to the moon.")
    except ValueError as e:
        print(f"Invalid input: {e}")
def main():
    calculate_debt_height()
if __name__ == "__main__":
    main()      
"""

This is a python program to measure the gasoline price .Number of gallons and and barrels of oil required will be measured from this program.
Args :

"""
def main():
    gallons = float(input("Enter the number of gallons of gasoline: "))
    liters = gallons * 3.7854
    barrels = gallons / 19.5
    pounds_co2 = gallons * 20 
    ethanol_gallons = (gallons * 115000) / 75700
    price = gallons * 4.00

    print(f"\n You entered {gallons:.2f} gallons of gasoline")
    print(f"Which is equiavalent to {liters:.2f} litres")
    print(f"Barrels of oil required:{barrels:.2f}")
    print(f"Pounds of CO2 produced: {pounds_co2:.2f}")
    print(f"Equivalent energy amount in ethanol gallons: {ethanol_gallons:.2f}")
    print(f"Price in US dollars: ${price:.2f}")



if __name__ == "__main__":
    main()

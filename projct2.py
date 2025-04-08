## This assignment is the design ,implementation and testing of a python program to display information about the nergy release by earthquakes .

# the richter scale is a way to quantify the energy released in jules
#Required Objectives
"""
Convert a richter scale value into energy release in jules
Energy release in tons of tnt
Handle both predefined values and user input
"""
import math




def display_intro():
    print("=" * 50)
    print("🌍  Richter Scale Energy Calculator  🌋")
    print("=" * 50)
    print("This program converts Richter scale values into:")
    print("- Energy in joules")
    print("- Equivalent energy in tons of TNT 💥")
    print()

def energy_in_jules(magnitude: float) -> float:
    energy = math.pow(10, 1.5*magnitude+4.8)
    return energy

def convert_joules_to_tnt(energy_jules: float) -> float:
    TNT_EQUIVALENT_JULES = 4.184e9
    tons = energy_jules / TNT_EQUIVALENT_JULES
    return tons

def main():
    display_intro()
    predefined_values = [1.0,5.0,9.1,9.2,9.5]
    for magnitude in predefined_values:
        energy = energy_in_jules(magnitude)
        tnt = convert_joules_to_tnt(energy)
        print(f"Richter Scale: {magnitude}")
        print(f"Energy: {energy:.2e} joules")
        print(f"TNT equivalent: {tnt:.2e} tons\n")
    try:
        user_input = float(input("Enter a richter scale measurement: "))
        energy = energy_in_jules(user_input)
        tnt = convert_joules_to_tnt(energy)
        print("\nYour input result: ")
        print(f"Richter Scale: {user_input}")
        print(f"Energy: {energy: .2e} joules")
        print(f"TNT equiavlent: {tnt:.2e} tons\n")
    except ValueError:
        print("Invalid input: Please enter a numeric value.")

if __name__ == "__main__":
    main()

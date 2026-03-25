"""
This program will prompt the user for an floating point value representing miles/hour.We will have to reprint the value in
'barleycons/day,
'furlongs/fortnight,
'Mach Number,
'percantage of the speed of light,
"""


def convert_speed_units(mph):
    meters_per_second = mph * 1609.34 / 3600
    barleycons_per_day = meters_per_second * 117.647 * 86400
    furlongs_per_fortnight = meters_per_second * 0.000125 * 1209600
    macch_number = meters_per_second / 343
    percentage_of_speed_of_light = meters_per_second / 299792458 * 100
    return {
        'barleycons_per_day': barleycons_per_day,
        'furlongs_per_fortnight': furlongs_per_fortnight,
        'mach_number': macch_number,
        'percentage_of_speed_of_light': percentage_of_speed_of_light
    }

mph = float(input("Enter speed in miles/hour: "))

try:
    mph = float(mph)
    results = convert_speed_units(mph)
    print(f"Speed in barleycons/day: {results['barleycons_per_day']:.2f}")  
    print(f"Speed in furlongs/fortnight: {results['furlongs_per_fortnight']:.2f}")
    print(f"Speed in Mach Number: {results['mach_number']:.2f}")
    print(f"Speed in percentage of the speed of light: {results['percentage_of_speed_of_light']:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
    

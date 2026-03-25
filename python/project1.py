def get_rods_input():
    rod_str = input("Input rods: ")
    rods = float(rod_str)
    return rods

def calculate_conversions(rods):
    meters_per_rod = 5.0292  # Correct value from your assignment
    feet_per_meter = 1/0.3048
    miles_per_meter = 1/1609.34
    furlongs_per_rod = 1/40
    walking_speed_mph = 3.1
    #calculations
    meters = rods * meters_per_rod
    feet = meters * feet_per_meter
    miles = meters * miles_per_meter
    furlongs = rods * furlongs_per_rod
    time_minutes = (miles/walking_speed_mph) * 60

    return meters,feet,miles,furlongs,time_minutes

def display_conversions(rods):
    meters,feet,miles,furlongs,time_minutes = calculate_conversions(rods)
    print(f"{rods} rods is:")
    print(f"  {meters:.2f} meters")
    print(f"  {feet:.2f} feet")
    print(f"  {miles:.4f} miles")
    print(f"  {furlongs:.4f} furlongs")
    print(f"  {time_minutes:.2f} minutes to walk")

def main():
    rods = get_rods_input()
    display_conversions(rods)

if __name__== "__main__":
    main()
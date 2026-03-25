import math

def time_travel(velocity):
    """
    This function simulates a time travel experience
    valeocity is percantage of the speed of light
    Args:
        velocity (float): The speed of the ship as a percentage of the speed of light.
    Returns:
        None
    Raises:
        ValueError: If the velocity is not between 0 and 100.
    100% of the speed of light is 299792458 m/s 
    """
    weight_of_ship = 70000 #in kg
    speed_of_light = 299792458 #in m/s
    factor = 1/ math.sqrt(1-velocity**2/speed_of_light**2)
    print(f"The sheep is travelling at {velocity}% times the speed of light")
    print(f"Weight of the ship is {weight_of_ship * factor} kg")
    print(f" Percieved time to travel to Alpha Centauri is {4.367 * factor} years")
    print(f"Percieved time to travel to Andromeda Galaxy is {2.537 * factor} million years")
    print(f"Percieved time to travel to the edge of the observable universe is {46.5 * factor} billion years")
    print(f"Percieved time to travel to the end of the universe is {13.8 * factor} billion years")


def main():
    try:
        velocity = float(input("Enter the speed of the ship as a percentage of the speed of light (0-100): "))
        if velocity < 0 or velocity > 100:
            raise ValueError("Velocity must be between 0 and 100.")
        time_travel(velocity)
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()



    
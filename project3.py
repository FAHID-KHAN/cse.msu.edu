"""
This is a python windchill program which basically calculates the windchill
based on the temperature and wind speed.
The formula used is:
    W = 35.74 + 0.6215*T - 35.75*(V**0.16) + 0.4275*T*(V**0.16)
where:
    W = wind chill in Fahrenheit
    T = temperature in Fahrenheit
    V = wind speed in miles per hour
"""


def calculate_windchill(temperature, wind_speed):
    """
    Calculate the wind chill based on the temperature and wind speed.
    :param temperature: Temperature in Fahrenheit
    :param wind_speed: Wind speed in miles per hour
    :return: Wind chill in Fahrenheit
    """
    return 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)

def main():
    """
    Main function to get user input and calculate wind chill.
    """
    try:
        temperature = float(input("Enter the temperature in Fahrenheit: "))
        wind_speed = float(input("Enter the wind speed in miles per hour: "))
        if temperature < -459.67:
            raise ValueError("Temperature cannot be below absolute zero.")
        if wind_speed < 0:
            raise ValueError("Wind speed cannot be negative.")
        wind_chill = calculate_windchill(temperature, wind_speed)
        print(f"The wind chill is: {wind_chill:.2f} °F")
    except ValueError as e:
        print(f"Invalid input: {e}")
if __name__ == "__main__":
    main()
# Test cases
def test_calculate_windchill():
    assert abs(calculate_windchill(32, 10) - 24.0) < 0.01, "Test case 1 failed"
    assert abs(calculate_windchill(50, 5) - 47.0) < 0.01, "Test case 2 failed"
    assert abs(calculate_windchill(0, 20) - -19.0) < 0.01, "Test case 3 failed"
    assert abs(calculate_windchill(-10, 15) - -28.0) < 0.01, "Test case 4 failed"
    print("All test cases passed!")
if __name__ == "__main__":
    test_calculate_windchill()
    main()
# The code above is a simple wind chill calculator that takes temperature and wind speed as input and calculates the wind chill using the formula provided. It also includes test cases to validate the functionality of the calculate_windchill function.
# The test cases cover different scenarios to ensure the function works correctly. The main function handles user input and output, while the calculate_windchill function performs the actual calculation.
# The code is structured to be easily readable and maintainable, with clear function definitions and error handling for invalid inputs.
# The test cases are designed to check the correctness of the wind chill calculation, and they will raise an assertion error if any of the test cases fail.
# The code is also designed to be run as a standalone script, with the main function being executed when the script is run directly.
# The test cases are executed before the main function to ensure that the functionality is validated before taking user input.
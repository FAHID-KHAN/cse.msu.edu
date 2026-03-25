def calculate_windchill(temperature,wind_speed):
    """
    Calculate the wind chill speed based on the temperature and wind speed """

    return  35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)


def main():
    try:
        temperature = float(input("Enter the temperature in Farenheit"))
        wind_speed = float(input("Enter the wind speed in miles per hour"))
        if temperature < -459.67:
            raise ValueError("Temperature cannot be below absolute zero.")
        if wind_speed < 0:
            raise ValueError("Wind speed cannot be negative.")
        wind_chill = calculate_windchill(temperature,wind_speed)
        print(f"The wind chill is:{wind_chill:.2f} °F")
    except ValueError as e:
        print(f"Invalid input: {e}")
if __name__ == "__main__":
    main()
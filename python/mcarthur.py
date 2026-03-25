def play_macarthur():
    print("Welcome to play mcarhur game!")
    print("This is fun math trick that will amaze you")
    print("Here is how it works:")
    print("1. You will enter the number of the month you were born (January is 1 ,February is 2 etc..)")
    print("2.You will also enter your age")
    print("3. The program will perform a series of revelation and reveal your birth month and age in a magical way")
    birth_month = int(input("Enter your birth month in numbers ,Ex 1 for jan 2 for feb"))
    age = int(input("Enter your number"))

    doubles_birth_month = birth_month*2
    doubles_birth_month += 5
    doubles_birth_month *= 50
    doubles_birth_month += age
    doubles_birth_month -= 365

    special_number = doubles_birth_month

    final_number = special_number + 115
    revealed_month = final_number // 100
    revealed_age = final_number % 100

    print(f"\nAfter the magic ,we add 115 to your special number: {final_number}")
    print(f"Your birth month is :{revealed_month}")
    print(f"Your age is :{revealed_age}")





if __name__ == "__main__":
    play_macarthur()
    
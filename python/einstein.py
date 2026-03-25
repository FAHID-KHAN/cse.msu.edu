def reverse_number(n):
    return int(str(n)[::-1])



def main():
    print("Welcome to the Einstein 1089 game!")
    print("Rules")
    print("1.Enter any three digit number where the first and last digits differ by at least 2")
    print("2.The program will reverse your number,substract,reverse again and amaze with you with results ")

    user_input = input("Enter a three digit number(first and last digits differ by at least 2): ")
    while not (user_input.isdigit() and len(user_input) and abs(int(user_input[0])-int(user_input[2])) >=2):
        user_input = input("Invalid input.Please enter a valid three digit number: ")
    num = int(user_input)
    rev_num = reverse_number(num)
    print(f"Your number: {num}")
    print(f"reversed num: {num}")

    diff = abs(num - rev_num)
    print(f"difference always positive: {diff}")

    rev_diff = reverse_number(diff)
    print("reverse of the difference {rev_diff}")

    result = diff + rev_diff
    print(f"Sum of differences and its reverse:{result}")
    print("\n Amazing! The result is always 1809")

if __name__ == "__main__":
    main()
import math 


def my_part():
    while True:
        try:
            answer = int(input("Please enter a number between 10 and 49"))
        except ValueError:
            print("Please enter an integer")
            continue
        if 10<=answer <= 49:
            break
        print("Number must be between 10 and 49")
    factor = 99 - answer 
    print("Keep your answer secret .Factor has been computed ")
    return answer,factor 

def friend_part(factor):
    while True:
        try:
            friend = int(input("Friend,select a number between 50 and 99"))
        except ValueError:
            print("Please enter an integer")
            continue
        if 50<= friend <= 99:
            break
        print("Number must be between 50 and 99")
    
    added = friend + factor 
    hundreds = added / 108
    tens = (added % 100) // 10
    units = added % 10

    new_units = units + hundreds
    transformed = tens * 10 + new_units

    result = friend - transformed

    print(f"/nFriends original number: {friend}")
    print(f"after removing factor: {friend} + {factor}={added}")
    print(f"Remove hundreds digit ({hundreds}) and add to units ({units}) : transformed = {transformed}")
    print(f"substract transformed from original :{friend} - {transformed} = {result} \n")
    return result 


def main():
    answer,factor = my_part()
    result = friend_part(factor)
    print(f"The revealed answer is : { result}")
    print(f"Your original secret answer was : {answer}")

if __name__ == "__main__":
    main()

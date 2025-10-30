def is_valid_number(s):
    """Check if a string is a valid whole number """
    return s.isdigit()

def is_valid_split_size(num_str,split_size_str):
    """Check if split size is valid for the given number """
    if not split_size_str.isdigit():
        return False
    split_size = int(split_size_str)
    return split_size > 0 and len(num_str) % split_size == 0

def split_number(num_str,split_size):
    pieces = []
    result = " "
    # split the number into pieces 
    for i in range(0,len(num_str),split_size):
        piece = num_str[i:i+split_size]
        pieces.append(piece)
        if result:
            result += ", "
        result += piece
    return pieces,result

def is_increasing(pieces):
    """Check if pieces are in increasing order"""
    if len(pieces) == 1:
        return True
    for i in range(len(pieces)-1):
        if pieces[i] >= pieces[i+1]:
            return False
    return True



def main():
    while True:
        num = input("Enter a whole number ")
        if is_valid_number(num):
            break
        print("Invalid input - please enter a whole number ")

    while True:
        split_size = input("Enter the split size ")
        if is_valid_split_size(num,split_size):
            break
        print("Invalid input - split size must divide ")
    
    pieces,formatted_result = split_number(num,int(split_size))
    print(f"The pieces are: {formatted_result}")
    if is_increasing(pieces):
        print("the pieces are increasing")
    else:
        print("The pieces are not in increasing order")


if __name__ == "__main__":
    main()

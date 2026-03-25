import math 

def triangular(k:int) -> int:
    return k*(k+1) // 2

def main():
    s_str = input("Enter a square number: ").strip()

    if not s_str.isdigit():
        print("Error: input must be a positive integer")
        return
    s = int(s_str)
    if s<=0:
        print("Error: input must be a positive integer")
        return 
    n = int(math.sqrt(s))
    if n * n != s:
        print("Error: that number is not a perfect square")
        return
    
    t1 = triangular(n)
    t2 = triangular(n-1)
    print(f"{s} = {t1} + {t2}")
    print(f"Triangular numbers: {t1} and {t2}")
    print(f"Square number: {s} (which is {n}^2)")

if __name__ == "__main__":
    main()
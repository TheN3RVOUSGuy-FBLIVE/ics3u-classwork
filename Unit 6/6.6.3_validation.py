def main():
    while True:
        try:
            age = int(input("Please enter your age: "))
            break
        except ValueError:
            print("Need to input an integer!\n")
    print(f"Wow, you are {age} years old.")


if __name__ == "__main__":
    main()

# 1 value error
# 4 loop does not break because it keeps trying the line of code until it gets valid input
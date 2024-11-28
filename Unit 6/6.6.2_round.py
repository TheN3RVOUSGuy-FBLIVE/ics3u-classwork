def main():
    while True:
        try:
            num = float(input("input a value from 0.0 - 1.0: "))
            if num > 1.0 or num < 0.0:
                raise ValueError
            break
        except ValueError:
            print("invalid input")
    print(percent(num))
    

def percent(num):
    per_cent = round(num * 100)
    return str(per_cent) + "%"


if __name__ == "__main__":
    main()
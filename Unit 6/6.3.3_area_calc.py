import math

run = True

def main():
    print("""
1) Triangle
2) Rectangle
3) Square
4) Circle
5) Quit \n""")
    choice = float(input("which shape: "))

    if choice == 1:
        base = float(input("base: "))
        height = float(input("height: "))
        print(f"area is {a_triangle(base, height)}")

    elif choice == 2:
        length = float(input("length: "))
        width = float(input("width: "))
        print(f"area is {a_rect(length, width)}")

    elif choice == 3:
        side = float(input("side: "))
        print(f"area is {a_square(side)}")

    elif choice == 4:
        radius = float(input("radius: "))
        print(f"area is {a_circle(radius)}")

    elif choice == 5:
        run = False
        return run
    
    def a_circle(radius):
        a = math.pi * radius ** 2
        return a

    def a_rect(length, width):
        a = length * width
        return a

    def a_square(side):
        a = side ** 2
        return a
        
    def a_triangle(base, height):
        a = (base * height) / 2
        return a

if run:
    main()


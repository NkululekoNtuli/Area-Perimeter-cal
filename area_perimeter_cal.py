import math

def get_input():
    shapes = ["TRIANGLE", "CIRCLE", "RECTANGLE"]
    count = 0
    while count == 0:
        print("Choose shape:")
        for i in range(len(shapes)):
            print(shapes[i])
        flage = 0
        choice = ""
        while flage == 0:
            choice = input("\nEnter choice here>>")
            if choice.upper() in shapes:
                flage = 1
                choice = choice.upper()
            else:
                flage = 0
                print("\nEnter valid option!")
            
            if choice in "TRIANGLE":
                triangle_base = int(input("Enter lenght of rectangle>> "))
                triangle_width = int(input("Enter width of rectangle>> "))
                dimetions1 = [triangle_base, triangle_width]
                return "Area: " + str(0.5* dimetions1[0] * dimetions1(1)) + "\nPerimeter: " + str(dimetions1[0] + dimetions1[1] + (dimetions1[0] ** 2 + dimetions1[1] ** 2))

            elif choice in "RECTANGLE":
                rectangle_len = int(input("Enter lenght of rectangle>> "))
                rectangle_width = int(input("Enter width of rectangle>> "))
                dimetions2 = [rectangle_len, rectangle_width]
                return "Area: " + str(dimetions2[0] * dimetions2[1]) + "squared \nPerimeter: " + str(2 * (dimetions2[0] + dimetions2[1]))

            elif choice in "CIRCLE":
                radius = int(input("Enter radius of circle>> "))
                return "Area: " + str(math.pi * (radius ** 2)) + "\nPerimeter: " + str(2 * math.pi * radius)
        
        repeat_program = input("Calculate agine>>").upper()
        if "YES" in repeat_program :
            count = 0
        else:
            count = 1

if __name__ == '__main__':
    print(get_input())
    count = 0
    while count == 0:
        repeat_program = input("\nEnter 'yes' to calculate agine, anything else to exite>>").upper()
        if "YES" in repeat_program :
            print(get_input())
            count = 0
        else:
            count = 1

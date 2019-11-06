#class que contem metodos para os algoritmos 50 - 55
import math as m

class Geometrics:
    def perimeterRectangle():
        base = float(input("Enter a base: "))
        height = float(input("Enter a height: "))
        return round(2 *(base + height),2)
    
    def areaRectangle():
        base = float(input("Enter a base: "))
        height = float(input("Enter a height: "))
        return round(base * height,2)

    def diagonalRectangle():
        base = float(input("Enter a base: "))
        height = float(input("Enter a height: "))
        return round(m.sqrt((base**2) + (height**2)),2)
    
    def perimeterCircle():
        radius = float(input("Enter a radius: "))
        return round((2 * m.pi * radius), 2)
    
    def areaCircle():
        radius = float(input("Enter a radius: "))
        return round((m.pi * (radius**2)),2)
    
    def perimeterSquare():
        base = float(input("Enter a side: "))
        return round(side*4,2)

    def areaSquare():
        side = float(input("Enter a side: "))
        return round(side**2,2)

    def diagonalSquare():
        side = float(input("Enter a side: "))
        return round((side * m.sqrt(2)),2)
    
    def diagonalParallelepiped ():
        a = float(input("Enter a side: "))
        b = float(input("Enter a side: "))
        b = float(input("Enter a side: "))
        return round(m.sqrt(a**2, b**2, c**2),2)
    
    def areaTriangle():
        base = float(input("Enter a base: "))
        height = float(input("Enter a base: "))
        return round((base * height)/2, 2)
    
    def areaRhombus():
        diagS = float(input("Enter a smaller diagonal: "))
        diagL = float(input("Enter a large diagonal: "))
        return round(((diagS*diagS)/2),2)

    
    option = 0
    while option != 12:
        print(''' 
        1 : perimeterRectangle
        2 : areaRectangle
        3 : diagonalRectangle
        4 : perimeterCircle
        5 : areaCircle
        6 : perimeterSquare
        7 : areaSquare
        8 : diagonalSquare
        9 : diagonalParallelepiped
        10 : areaTriangle
        11: areaRhombus''')
        option = int(input("Choose an option below:. Choose 12 to exit: "))

        if option == 1:
            print("Perimeter of a rectangle: ", perimeterRectangle())
        elif option == 2:
            print("Area of a rectangle: ", areaRectangle())
        elif option == 3:
            print("Diagonal of a rectangle: ", diagonalRectangle())
        elif option == 4:
            print("Perimeter of a circle: ", perimeterCircle())
        elif option == 5:
            print("Area of a circle: ", areaCircle())
        elif option == 6:
            print("Area of a square: ", areaSquare())
        elif option == 8:
            print("Diagonal Square: ", diagonalSquare())
        elif option == 9:
            print("Diagonal of a Parallelepiped: ", diagonalParallelepiped())
        elif option == 10:
            print("Area of a Triangle: ", areaTriangle())
        elif option == 11:
            print("Area of a Rhombus: ", areaRhombus())
        elif option == 12:
            break
        else:
            print("It´s not a valid option")








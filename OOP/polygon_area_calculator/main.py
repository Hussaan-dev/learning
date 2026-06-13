class Rectangle:
    def __init__(self,width: int,height: int):
        self.width=width
        self.height=height
        
    def set_width(self,width: int):
        self.width=width

    def set_height(self,height: int):
        self.height=height

    def get_area(self):
        return self.height*self.width

    def get_perimeter(self):
        return 2*(self.height+self.width)
    
    def get_diagonal(self):
        return pow((self.width**2)+(self.height**2),0.5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        diagram=""
        for i in range(0,self.height):
            for j in range(0,self.width):
                diagram+="*"
            diagram+='\n'
        return diagram

    def get_amount_inside(self,shape: "Rectangle"):
        across=self.width // shape.width
        down=self.height // shape.height
        return across*down

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self,side: int):
        super().__init__(side,side)

    def set_height(self,height: int):
        self.height=self.width=height

    def set_width(self,width: int):
        self.height=self.width=width

    def set_side(self,side: int):
        self.height=self.width=side

    def __str__(self):
        return f"Square(side={self.height})"

def main() -> None:
    rect = Rectangle(15, 10)
    square = Square(5)

    print("\nRectangle:")
    print(rect)
    print(f"Area: {rect.get_area()}")
    print(f"Perimeter: {rect.get_perimeter()}")
    print(f"Diagonal: {rect.get_diagonal():.2f}")

    print("\nSquare:")
    print(square)
    print(f"Area: {square.get_area()}")
    print(f"Perimeter: {square.get_perimeter()}")
    print(f"Diagonal: {square.get_diagonal():.2f}")

    print("\nShapes Inside:")
    print(f"{square} fits inside {rect} {rect.get_amount_inside(square)} times")

    print("\nRectangle Picture:")
    small_rect = Rectangle(4, 3)
    print(small_rect.get_picture())

    print("Updating Square Side:")
    square.set_side(7)
    print(square)

    print("\nUsing set_width on Square:")
    square.set_width(9)
    print(square)


main()
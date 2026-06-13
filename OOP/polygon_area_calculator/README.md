# Polygon Area Calculator

A small object-oriented Python project that models rectangles and squares.

This project was completed as part of the FreeCodeCamp Scientific Computing with Python curriculum and focuses on practicing inheritance, method overriding, dunder method and basic geometric calculations.

## Features

### Rectangle

* Set width and height
* Calculate area
* Calculate perimeter
* Calculate diagonal length
* Generate a text-based picture of the shape
* Determine how many smaller shapes can fit inside

### Square

* Inherits from `Rectangle`
* Maintains equal width and height
* Supports updating dimensions through:

  * `set_width()`
  * `set_height()`
  * `set_side()`

## Concepts Practiced

* Classes and objects
* Inheritance
* Method overriding
* Encapsulation
* String representations with `__str__`
* Type hints
* Basic geometry

## Example

```python
rect = Rectangle(15, 10)
square = Square(5)

print(rect.get_area())              # 150
print(square.get_perimeter())       # 20
print(rect.get_amount_inside(square))  # 6
```

## Project Structure

```text
polygon_area_calculator/
└── main.py
```

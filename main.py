import shapes
print("Choose a shape to calculate area")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")
choice = input("Enter your choice: ")
if choice ==1:
radius = float(input("Enter radius of circle: "))
result = shapes.circle_area(radius)
print("Area of circle =", round(result,2))
elif choice == 2:
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
result = shapes.rectangle_area(length, width)
print("Area of rectangle =", result)
elif choice == 3:
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
result = shapes.triangle_area(base, height)
print("Area of triangle =", result)
else:
print("Invalid choice")

import math
def circle_area(radius):
area = math.pi * radius * radius
return area
def rectangle_area(length, width):
area = length * width
return area
def triangle_area(base, height):
area = 0.5 * base * height
return area


import shape
print("Choose a shape to calculate area")
print("1.area_of_circle")
print("2.area_of_reactagle")

choice=int(input("enter your choice="))
if choice==1:
    radius=float(input("enter the radius="))
    result=shape.area_of_circle(radius)
    print("area of circle is=",result)
elif choice==2:
    height=int(input("enter the height of reactangle="))
    width=int(input("enter the width of reatangle="))
    result=shape.area_of_rectangle(height,width)
    print("area_of rectangle=",result)

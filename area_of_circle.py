import math

def area_of_circle(r):
    pi=math.pi
    area=pi*r**2
    return area

area=0
radius=int(input("Input the radius: "))
area=area_of_circle(radius)
print("The area is: ", area)

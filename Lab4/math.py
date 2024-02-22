#TASK 1
import math
x = 15
radian = x*(math.pi/180)
print(f"Output radian:{radian:.6f}")

#TASK 2
a = int(input("Height:"))
b = int(input("Base, first value:"))
c = int(input("Base, second value:"))
print("Expected Output:", (b+c)/2*a)

#TASK 3
side = int(input("Input number of sides:"))
length = int(input("Input the length of a side:"))
apothem = length/(2*math.tan(math.pi/side))
print("The are of the poligon is:", (side*length*apothem)/2)

#TASK 4
lob = int(input("Length of base:"))
hop = int(input("Height of parallelogram:"))
print("Expected Output:", lob*hop)
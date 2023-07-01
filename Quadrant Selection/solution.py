x_coordinate= int(input())
y_coordinate= int(input())


if x_coordinate>0:
    quadrant_num= 1
else:
    quadrant_num= 2

if y_coordinate<0:
    quadrant_num= 5-quadrant_num

print(quadrant_num)

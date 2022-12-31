from collections import namedtuple

age=float(input("please enter person's age in years: "))
height=float(input("please enter person's height in cm: "))
weight = float(input("please enter person's weight in kg: "))
name=str(input("please enter person's name: "))

d={1:age, 2:height,3:weight,4:name}
print(d)

if d.get(1)>0 and d.get(1)<=18:
    a='teenager'
elif d.get(1)>19 and d.get(1)<=40:
    a='young man'
elif d.get(1)>40:
    a='adult'

if d.get(2)>0 and d.get(2)<=100:
    b='short height'
elif d.get(2)>100 and d.get(2)<=180:
    b='average height'
elif d.get(2)>180 and d.get(2)<=300:
    b='tall'

if d.get(3)>0 and d.get(3)<=60:
    c='low weight'
elif d.get(3)>60 and d.get(3)<=80:
    c='average weight'
elif d.get(3)>80:
    c='high weight'

Point = namedtuple("Point", ["x", "y", "z", "i"])
point = Point(x=a, y=b, z=c, i=d.get(4))
print(point.i, point.x, point.y, point.z)
print(f"Hi,\n your name is\n", point.i,"\nyour age is\n",point.x, "\nyour height is\n",point.y, "\nand\n ","\nyour weight is\n", point.z)



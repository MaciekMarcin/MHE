import random
import matplotlib.pyplot as plt
import math

class Qube:
    def __init__(self):
        super().__init__()

def problem():
    print('test')

def solution():
    for point in points:
        if(point == 'x'):
            elements = math.sqrt(len(points))
            for element in range(1,int(elements)+1):
                if(points.count(element) < int(elements)):
                    print(str(element) + ' is a x')
        else:
            continue

def solution_t():
    goal = 0

#for point in points:
#    temp = points[]
#    Latin square

points = [1,'x',3,2,3,1,3,1,2]

solution()
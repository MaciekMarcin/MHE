import random
import math

#Klasa obiektu Cube które nic nie robi póki co
class Square:
    def __init__(self):
        print('test')

#Funkcja problem która wstawia w losowe miejsca niewiadome.
def problem(i):
    while i > 0:
        x = random.randint(0,len(points_v2)-1)
        y = random.randint(0,len(points_v2)-1)
        points_v2[x][y] = 'x'
        print('Generated problem: ', *points_v2,sep='\n',end='\n\n')
        points_transposed = list(map(list, points_v2))
        i = i - 1

#Funkcja rozwiązania która próbuje z problemu osiągnąć stan na wejściu
def solution_v2():

    #Booleany które potem przydają sięprzy sprawdzaniu czy wystąpił błąd przy wypełnieniu list.
    Status_transposed_boolean = False
    Status_normal_boolean = False

    for points in points_v2:
        for point in points:
            #Jeżeli element to string to sprawdzam jaki jest rozmiar listy i pętlą for sprawdzam ile dana liczba razy wystąpiła 
            # i jeśli jedna liczba nie wystąpiła to jest ona tą zmienną.
            if(type(point) is str):
                elements = len(points)
                for element in range(1,int(elements)+1):
                    if(points.count(element) < 1):
                        print(str(element) + ' is a x')
                        points_v2_normal[points_v2.index(points)][points.index(point)] = element
                        possible_elements_normal.append(element)
                        new_points_normal.append(element)

    points_v2_normal_reversed = list(map(list, zip(points_v2_normal[0],points_v2_normal[1],points_v2_normal[2])))
    print('Normal: ', points_v2_normal, sep='\n', end='\n\n')
    for points in points_v2_normal_reversed:
        for point in points:
            if(points.count(point) > 1):
                print('Error', point)
                Status_normal_boolean = True

    for points in points_transposed:
        for point in points:
            if(type(point) is str):
                elements_transposed = len(points)
                for element_transposed in range(1,int(elements_transposed)+1):
                    if(points.count(element_transposed) < 1):
                        print(str(element_transposed) + ' is a x')
                        points_v2_transposed[points_transposed.index(points)][points.index(point)] = element_transposed
                        possible_elements_transposed.append(element_transposed)
                        new_points_transposed.append(element_transposed)

    points_v2_transposed_reversed = list(map(list, zip(points_v2_transposed[0],points_v2_transposed[1],points_v2_transposed[2])))
    print('Transposed: ', points_v2_transposed, sep='\n', end='\n\n')    
    for points in points_v2_transposed_reversed:
        for point in points:
            if(points.count(point) > 1):
                print('Error', point)
                Status_transposed_boolean = True

    if((Status_transposed_boolean == True) and Status_normal_boolean != True):
        print('Correct outcome: ', points_v2_normal)
    elif((Status_transposed_boolean != True) and Status_normal_boolean == True):
        print('Correct outcome: ', points_v2_transposed_reversed)
    elif((Status_transposed_boolean == False) and Status_normal_boolean == False):
        print('Correct outcome: ', points_v2_normal)
    else:
        print("The answer isn't here or try manual input")

#Funkcja która nic nie robi póki co
def solution_t():
    goal = 0

#Listy na kompletne listy z liczbami zamiast zmiennej
new_points_normal = []
new_points_transposed = []

#Listy z możliwymi liczbami które można podstawić za zmienną
possible_elements_normal = []
possible_elements_transposed = []

#Tworzenie setów do porównywania czy jeden zbiór jest podzbiorem drugiego
set_normal = set(possible_elements_normal)
set_transposed = set(possible_elements_transposed)

#Listy z danymi wejściowymi, danymi po transpozycji oraz liczbą elementów w liście
points_v2 = [[2, 1, 3],[3, 2, 1],[1, 3, 2]]

points_transposed = list(map(list, zip(points_v2[0],points_v2[1],points_v2[2])))
amount_of_elements = len(points_v2)*len(points_v2)

points_v2_normal = points_v2
points_v2_transposed = points_transposed

#Wywołanie funkcji
problem(3)
solution_v2()
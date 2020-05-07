import random
import math

#Klasa obiektu Cube które nic nie robi póki co
#class Square:
#    def __init__(self):
#        print('test')
Square_array = []
def Square(i):
    for i in range(1,i):
        for j in range(1,i):
            Square_array.append()


#Funkcja problem która wstawia w losowe miejsca niewiadome.
def problem(i):
    while i > 0:
        x = random.randint(0,len(points_v2)-1)
        y = random.randint(0,len(points_v2)-1)
        if(points_v2[x][y] == 'x'):
            continue
        else:
            points_v2[x][y] = 'x'
            i = i - 1
    print('Generated problem: ', *points_v2,sep='\n',end='\n\n')

#Funkcja rozwiązania która próbuje z problemu osiągnąć stan na wejściu
def solution_v2():

    for points in points_v2:
        for point in points:
            #Jeżeli element to string to sprawdzam jaki jest rozmiar listy i pętlą for sprawdzam ile dana liczba razy wystąpiła 
            # i jeśli jedna liczba nie wystąpiła to jest ona tą zmienną.
            if(type(point) is str):
                elements = len(points)
                for element in range(1,int(elements)+1):
                    if(points.count(element) < 1):
                        print(str(element) + ' is a x')
                        if((points_v2_normal[(points_v2.index(points)+1)%3][points.index(point)] == element) or (points_v2_normal[(points_v2.index(points)+2)%3][points.index(point)] == element)):
                            if(((element + 1)%4) == 0):
                                points_v2_normal[points_v2.index(points)][points.index(point)] = 1
                            else:
                                if((points_v2_normal[(points_v2.index(points)+1)%3][points.index(point)] == element + 1) or (points_v2_normal[(points_v2.index(points)+2)%3][points.index(point)] == element + 1)):
                                    if(((element + 1)%4) == 0):
                                        points_v2_normal[points_v2.index(points)][points.index(point)] = 1
                                    elif(element + 2 == 4):
                                        points_v2_normal[points_v2.index(points)][points.index(point)] = 1
                                    else:
                                        points_v2_normal[points_v2.index(points)][points.index(point)] = (element + 2)
                                else:
                                    points_v2_normal[points_v2.index(points)][points.index(point)] = (element + 1)
                        else:
                            points_v2_normal[points_v2.index(points)][points.index(point)] = element
                        #possible_elements_normal.append(element)
                        #new_points_normal.append(element)
                        

#    for points in points_transposed:
#        for point in points:
#            if(type(point) is str):
#                elements_transposed = len(points)
#                for element_transposed in range(1,int(elements_transposed)+1):
#                    if(points.count(element_transposed) < 1):
#                        print(str(element_transposed) + ' is a x')
#                        points_v2_transposed[points_transposed.index(points)][points.index(point)] = element_transposed
#                        #possible_elements_transposed.append(element_transposed)
#                        #new_points_transposed.append(element_transposed)

    points_v2_normal_reversed = list(map(list, zip(points_v2_normal[0],points_v2_normal[1],points_v2_normal[2])))
    points_v2_transposed_reversed = list(map(list, zip(points_v2_transposed[0],points_v2_transposed[1],points_v2_transposed[2])))

    #Dla normal
    print('Normal: ', *points_v2_normal, sep='\n', end='\n\n')
    #for points in points_v2_normal_reversed:
    #    for point in points:
    #        if(points.count(point) > 1):
    #            print('Error', point)
    #            Status_normal_boolean = True
                #print(points_v2_normal_reversed.index(points))
                #point = 'x'
                #print(points_v2_normal_reversed)
                #solution_v2()
    #print(*points_v2_normal_reversed, sep='\n', end='\n\n')

    #Dla transposed
    print('Transposed: ', *points_v2_transposed, sep='\n', end='\n\n')    
    #for points in points_v2_transposed_reversed:
    #    for point in points:
    #        if(points.count(point) > 1):
    #            print('Error', point)
    #            Status_transposed_boolean = True
                #point = 'x'
                #print(points_v2_transposed_reversed)
                #solution_v2
    #print(*points_v2_transposed_reversed, sep='\n', end='\n\n')


#Funkcja która nic nie robi póki co
def solution_t():
    i = 0
    for points in points_v2_normal:
        for point in points:
            elements = len(points)
            for element in range(1,int(elements)+1):
                if(points.count(element) == 1):
                    i = i + (1/3)
                    #print(round(i,2))
                    #possible_elements_normal.append(element)
                    #new_points_normal.append(element)
    for points in points_v2_normal_reversed:
        for point in points:
            elements = len(points)
            for element in range(1,int(elements)+1):
                if(points.count(element) == 1):
                    i = i + (1/3)
                    #print(round(i,2))
                    #possible_elements_normal.append(element)
                    #new_points_normal.append(element)
    i = i/(amount_of_elements*2)
    print((round(i,2)*100),'%',sep='')


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
#points_v2 = [[1,2,3,4,5,6,7,8],[2,3,4,5,6,7,8,1],[3,4,5,6,7,8,1,2],[4,5,6,7,8,1,2,3],[5,6,7,8,1,2,3,4],[6,7,8,1,2,3,4,5],[7,8,1,2,3,4,5,6],[8,1,2,3,4,5,6,7]]

#points_transposed = list(map(list, zip(points_v2[0],points_v2[1],points_v2[2],points_v2[3],points_v2[4],points_v2[5],points_v2[6],points_v2[7])))


#Kopia listy do ocenienia jakości oraz kopia listy z niewiadomymi oraz kopia listy po transpozycji

#Wywołanie funkcji

problem(8)

points_transposed = list(map(list, zip(points_v2[0],points_v2[1],points_v2[2])))
amount_of_elements = len(points_v2)*len(points_v2)
points_v2_normal = points_v2
points_v2_transposed = points_transposed

solution_v2()
points_v2_normal_reversed = list(map(list, zip(points_v2_normal[0],points_v2_normal[1],points_v2_normal[2])))
solution_t()
#print(transpose(points_v2_normal))
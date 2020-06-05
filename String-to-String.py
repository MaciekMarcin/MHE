import random
import math
from datetime import datetime
import numpy as np
from itertools import combinations
import copy

#Utowrzenie latin square
def create_square(size: int):
    row = [i for i in range(1, size+1)]
    #print(row)
    return [row[i:] + row[:i] for i in range(size)]


#Funkcja problem która wstawia w losowe miejsca niewiadome.
def problem(i,points_v2_normal):
    while i > 0:
        x = random.randint(0,len(points_v2_normal)-1)
        y = random.randint(0,len(points_v2_normal)-1)
        if(points_v2_normal[x][y] == 'x'):
            continue
        else:
            points_v2_normal[x][y] = 'x'
            i = i - 1
    print('Generated problem: ', *points_v2_normal,sep='\n',end='\n\n')

def get_rid_of_strings(points_v2_wo_strings):
    #global wo_strings 
    points_v2_wo_strings = [[int(i) if i.isdigit() else i for i in j] for j in points_v2_wo_strings]
    #print(points_v2_wo_strings)
    wo_strings = points_v2_wo_strings
    return wo_strings


#Funkcja rozwiązania która próbuje z problemu osiągnąć stan na wejściu
def solution_v2(points_v2_normal):
    #print(points_v2_normal)
    outcome = []
    whole_row_in_x_counter = 0
    for points in points_v2_normal:
        check_for_x = points.count('x')
        i = 0
        #print(points)
        if(check_for_x == 0):
            outcome.append(points)
        elif(check_for_x == size):
            whole_row_in_x_counter = whole_row_in_x_counter + 1
            outcome.append(points)
        else:
            Highest_similarity = 0
            elements = len(points)
            x = []
            for each in range(1,size+1):
                x.append(each)
            for each in range(0,size):
                if(check_for_x == 0):
                    break
                rotate_list = x
                rotate_list = rotate_list[each:] + rotate_list[:each]
                Common_elements = [i for i, j in zip(rotate_list, points) if i == j]
                similarity = len(Common_elements)/size
                if(similarity > Highest_similarity):
                    outcome.append(rotate_list)
    print('OUTCOME')
    print(outcome)
    print(whole_row_in_x_counter)

    if(whole_row_in_x_counter == size):
        print('Incorrect input')
        quit()
    if(whole_row_in_x_counter > 0):
        outcome = np.transpose(outcome)
        outcome = outcome.tolist()
        outcome_wo_strings = get_rid_of_strings(outcome)
        print('outcome_solution')
        print(outcome_wo_strings)
        return solution_v2(outcome_wo_strings)
        #print('TRANSPOSITION TIME')
    if(whole_row_in_x_counter == 0):
        #outcome_final = outcome
        print('Final outcome')
        for row in outcome:
            print(row)
        #print(outcome)
        result = outcome
        return result

def climbing(points_v2_climbing):
    #Stworzenie wszystkich możliwych rozwiązań z otoczenia
    #Iterować po każdym punkcie gdzie jest x i forem sprawdzać która wartość zwraca najlepszy wynik i jechać dalej
    outcome = []
    for points in points_v2_climbing:
        for point in points:
            #print(point)
            if(point == 'x'):
                test_list = copy.deepcopy(points_v2_climbing)
                #test_list[test_list.index(points)][points.index(point)] = len(points)
                final_point_score = solution_t(test_list,problem_amount)
                print('Final point score ' + str(final_point_score))
                for each in range(1,2*(len(points)+1)):
                    i = random.randint(1,len(points_v2_climbing))
                    print('i: ' + str(i))
                    test_list = copy.deepcopy(points_v2_climbing)
                    loop_list = copy.deepcopy(points_v2_climbing) #jedyna opcja działająca kopiowania listy
                    #Trzeba pracować na kopii listy niż na oryginale
                    loop_list[loop_list.index(points)][points.index(point)] = i
                    score = solution_t(loop_list,problem_amount)
                    print('score of point: ' + str(score))
                    if(score >= final_point_score):
                        final_point_score = score
                        points_v2_climbing[points_v2_climbing.index(points)][points.index(point)] = int(i)
                        #print('inserted ' + str(i) + ' at ['+ str(points_v2_climbing.index(points)) + ',' + str(points.index(i)) + ']')
                        #print('example ' + str(points_v2_climbing))
                        break
    print(points_v2_climbing)

    ##########RANDOM################

    #for each in range(1,2*(len(points)+1)):
    #                i = random.randint(1,len(points_v2_climbing))
    #                print('i: ' + str(i))
    #                test_list = copy.deepcopy(points_v2_climbing)
    #                loop_list = copy.deepcopy(points_v2_climbing) #jedyna opcja działająca kopiowania listy
    #                #Trzeba pracować na kopii listy niż na oryginale
    #                loop_list[loop_list.index(points)][points.index(point)] = i
    #                score = solution_t(loop_list,problem_amount)
    #                print('score of point: ' + str(score))
    #                if(score > final_point_score):
    #                    final_point_score = score
    #                    points_v2_climbing[points_v2_climbing.index(points)][points.index(point)] = int(i)
    #                    #print('inserted ' + str(i) + ' at ['+ str(points_v2_climbing.index(points)) + ',' + str(points.index(i)) + ']')
    #                    #print('example ' + str(points_v2_climbing))
    #                    break

    #h = 0 #x counter
    #for points in points_v2_climbing:
    #    for point in points:
    #        if(point == 'x'):
    #            h = h + 1
    #if(h > 0):
    #    points_v2_climbing = np.transpose(points_v2_climbing)
    #    points_v2_climbing = points_v2_climbing.tolist()
    #    points_v2_climbing = get_rid_of_strings(points_v2_climbing)
    #    for points in points_v2_climbing:
    #        for point in points:
    #            #print(point)
    #            if(point == 'x'):
    #                test_list = copy.deepcopy(points_v2_climbing)
    #                test_list[test_list.index(points)][points.index(point)] = len(points)
    #                final_point_score = solution_t(test_list,problem_amount)
    #                #print('Final point score ' + str(final_point_score))
    #                for i in range(1,len(points)+1):
    #                    #print('i: ' + str(i))
    #                    test_list = copy.deepcopy(points_v2_climbing)
    #                    loop_list = copy.deepcopy(points_v2_climbing) #jedyna opcja działająca kopiowania listy
    #                    #Trzeba pracować na kopii listy niż na oryginale
    #                    loop_list[loop_list.index(points)][points.index(point)] = i
    #                    score = solution_t(loop_list,problem_amount)
    #                    #print('score of point: ' + str(score))
    #                    if(score > final_point_score):
    #                        final_point_score = score
    #                        points_v2_climbing[points_v2_climbing.index(points)][points.index(point)] = int(i)
    #                        #print('inserted ' + str(i) + ' at ['+ str(points_v2_climbing.index(points)) + ',' + str(points.index(i)) + ']')
    #                        #print('example ' + str(points_v2_climbing))
    #                        break
                    #Dodań kolejną pętle aby wstawić cokolwiek co ma najwyższy score LUB na start dobierać 1 i dodawać to co ma lepszy score lub domyslnie 1
    print('final list ' + str(points_v2_climbing)) #print final list
    return points_v2_climbing


def taboo(points_v2_normal):
    for points in points_v2_normal:
        for point in points:
            if(point == 'x'):
                candidates = []
                points_v2_transposed = np.transpose(points_v2_normal)
                points_v2_transposed = points_v2_transposed.tolist()
                points_v2_transposed = get_rid_of_strings(points_v2_transposed)
                taboo_list = sorted(np.unique(points+points_v2_transposed[points.index(point)]))
                print(taboo_list)
                ####COPY OF HILL CLIMBING#####
                test_list = copy.deepcopy(points_v2_normal)
                #test_list[test_list.index(points)][points.index(point)] = len(points)
                final_point_score = solution_t(test_list,problem_amount)
                print('Final point score ' + str(final_point_score))
                for each in range(1,2*(len(points)+1)):
                    i = random.randint(1,len(points_v2_normal))
                    test_list = copy.deepcopy(points_v2_normal)
                    loop_list = copy.deepcopy(points_v2_normal) #jedyna opcja działająca kopiowania listy
                    #Trzeba pracować na kopii listy niż na oryginale
                    loop_list[loop_list.index(points)][points.index(point)] = i
                    score = solution_t(loop_list,problem_amount)
                    #print('score of point: ' + str(score))
                    point_and_score = [i,score]
                    candidates.append(point_and_score)
                    #print('Candidates: ' + str(candidates))
                for candidate in candidates:
                    if(candidate[0] in taboo_list):
                        candidates.remove(candidate)
                        print('Candidate without taboo: ' + str(candidates))
                highest_score = candidates[0]
                for point_score in candidates:
                    if(point_score[1] > highest_score[1]):
                        highest_score = point_score
                points_v2_normal[points_v2_normal.index(points)][points.index(point)] = highest_score[0]
                print('Inserted: ' + str(highest_score[0]))
    print('final list ' + str(points_v2_normal)) #print final list
    return points_v2_normal

def SA():
    print('test')


    #Zainicjować
        #Na start lista na wejście + lista po transpozycji do stworzenia listy tabu
    #Stworzyć listę kandydatów na sąsiadów obecnego rozwiązania (W tym wypadku pętla for i jechane po każdej wartości)
    #Znalezienie rozwiązania z najlepszą wartością
    #Sprawdzenie czy nie jest w tabu
    #Jeśli jest to sprawdzenie jeszcze raz, ale bez tej wartości, a jak nie to przyjąc to jako nowy stan początkowy
    #Czy kryterium końcowe zostało spełnione
    #Koniec

#def format_outcome(outcome):
#    solution = solution_v2(outcome)
#    print(*outcome, sep='\n', end='\n\n')


def solution_t(points_v2_score,problem_amount):
    i = 0
    j = 0
    for points in points_v2_score:
        for point in points:
            elements = len(points)
            if(point == 'x'):
                i = i# - 1
            elif(points.count(point) == 1):
                i = i + 1
            else:
                i = i# - 1
    points_v2_transposed = np.transpose(points_v2_score)
    points_v2_transposed = points_v2_transposed.tolist()
    #points_v2_transposed = get_rid_of_strings(points_v2_transposed) # dopiero dodana 04.06.2020
    for points in points_v2_transposed:
        for point in points:
            elements = len(points)
            if(point == 'x'):
                j = j# - 1
            elif(points.count(point) == 1):
                j = j + 1
            else:
                j = j# - 1#+ (1/2)
    #print('I_SCORE: ' + str(i))
    #print('J_SCORE: ' + str(j))
    score = (i + j)#/((elements*elements)*2)
    #score = round((i + j)/(amount_of_elements*2),2)*100
    #print(score,'%',sep='')
    return score

def load_from_file():
    text_file_source = open('Source.txt', 'r').read()#.replace('\n','')
    size = len(text_file_source)
    #data = open('Source.txt', 'r').read().replace('\n','')
    for line in range(0,3):
        temp_list = []
        for item in text_file_source:
            print(item)
            #stripped_line = line.strip()
            #line_list = stripped_line.split()
            temp_list.append(item)
        points_from_txt.append(temp_list)
    print(points_from_txt)


#Listy na kompletne listy z liczbami zamiast zmiennej
new_points_normal = []
new_points_transposed = []


problem_amount = 0
solution_amount = 0
trial_amount = int(input('How many test cases?: '))
algorithm = int(input('Select algorithm:\n1-Bruteforce\n2-Climbing\n3-Taboo Search\n'))
source = int(input('Select data source:\n1-From txt file\n2-Default source data\n'))
size = int(input('Input number (not applicable if you want input from file): '))
problem_amount = int(input('How many unknown values do you want? (Max amount is: ' + str(size*size) + '): '))

points_v2 = create_square(size)
#outcome_final = []
points_from_txt = []

#print(points_v2_transposed.tolist())

amount_of_elements = len(points_v2)*len(points_v2)

def trial(trial_amount, problem_amount):
    interval_sum = 0
    score_sum = 0
    i = 1
    if(source == 1):
        load_from_file()
        #points_v2 = points_from_txt
    text_file = open('Result.txt', 'w')
    
    for each in range(0, trial_amount):
        before = datetime.now()
        points_v2_normal = points_v2
        
        problem(problem_amount,points_v2_normal)
        #points_v2_climbing = copy.deepcopy(points_v2_normal) # zbędna linia bo tylko kopiuje referencje i puszczam jeden algorytm naraz
        text_file.write('Problem ' + str(each + 1) + ':\n')
        for row in points_v2_normal:
            text_file.write(str(row) + '\n')
        text_file.write('\n')
        #######FROM HERE ONWARD BRUTEFORCE############
        if(algorithm == 1):
            final_outcome = solution_v2(points_v2_normal)
        elif(algorithm == 2):
            final_outcome = climbing(points_v2_normal)
        elif(algorithm == 3):
            final_outcome = taboo(points_v2_normal)
        score = solution_t(final_outcome,problem_amount)
        after = datetime.now()
        interval = after - before
        if(type(interval_sum) == int):
            interval_sum = interval
        else:
            interval_sum = interval_sum + interval
        if(score_sum == 0):
            score_sum = score
        else:
            score_sum = score_sum + score
        text_file.write('Latin square ' + str(each + 1) + ':\n')
        for row in final_outcome:
            text_file.write(str(row) + '\n')
        text_file.write('Time: ' + str(interval) + '\nScore: ' + str(round(score,0)) + '%\n')
        text_file.write('\n--------------------------------------------------------\n\n')
        
        print(interval)
        print(score/(amount_of_elements*2))
        print(i)
        i = i + 1
    Avg_score = round((score_sum/trial_amount),2)
    Avg_time = (interval_sum/trial_amount)
    text_file.write('Total time: ' + str(interval_sum) + '\nAverage time: ' + str(Avg_time) + '\nAverage score: ' + str(Avg_score) + '%\n\n')
    text_file.close()
    print(interval_sum)

trial(trial_amount,problem_amount)
#print(outcome_final)



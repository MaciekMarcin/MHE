import random
import math
from datetime import datetime
import numpy as np
from itertools import combinations

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
    global wo_strings 
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
            #for row in outcome:
            #    if(set(points).issubset(set(row))):
            #        break
            #    else:
            #        i = i + 1
            #print(i)
            #print(size)
            #if(i == size):
            outcome.append(points)
        elif(check_for_x == size):
            #for row in outcome:
            #    if(set(points).issubset(set(row))):
            #        break
            #    else:
            #        i = i + 1
            #print(i)
            #print(size)
            #if(i == size):
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
                #print(rotate_list)
                Common_elements = [i for i, j in zip(rotate_list, points) if i == j]
                similarity = len(Common_elements)/size
                #print(similarity)
                if(similarity > Highest_similarity):
                    outcome.append(rotate_list)
                #elif(points.count('x') < 1):
                #    outcome.append(points)
                #print(points)
                #print('--------------------------------')
    print('OUTCOME')
    print(outcome)
    print(whole_row_in_x_counter)
    #print(points_v2_normal)
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
        print(outcome)
        result = outcome
        return result


    #Dla normal
    #print('Normal: ', *solution, sep='\n', end='\n\n')
    #print(*points_v2_normal_reversed, sep='\n', end='\n\n')
    #points_v2_transposed = list(map(list, zip(points_v2_normal[0],points_v2_normal[1],points_v2_normal[2])))
def format_outcome(outcome):
    solution = solution_v2(outcome)
    print(*outcome, sep='\n', end='\n\n')


def solution_t(points_v2_normal,problem_amount):
    i = 0
    j = 0
    for points in points_v2_normal:
        for point in points:
            elements = len(points)
            if(points.count(point) == 1):
                i = i + 1
            else:
                i = i #+ (1/2)
    points_v2_transposed = np.transpose(points_v2_normal)
    points_v2_transposed = points_v2_transposed.tolist()
    for points in points_v2_transposed:
        for point in points:
            elements = len(points)
            if(points.count(point) == 1):
                j = j + 1
            else:
                j = j #+ (1/2)
    print(i)
    print(j)
    score = i + j
    score = round((i + j)/(amount_of_elements*2),2)*100
    print(score,'%',sep='')
    return score

def load_from_file():
    text_file_source = open('Source.txt', 'r').read().replace('\n','')
    #data = open('Source.txt', 'r').read().replace('\n','')
    for line in text_file_source:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        points_from_txt.append(line_list)
    print(points_from_txt)


#Listy na kompletne listy z liczbami zamiast zmiennej
new_points_normal = []
new_points_transposed = []


problem_amount = 0
solution_amount = 0
trial_amount = int(input('How many test cases?: '))
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
        text_file.write('Problem ' + str(each + 1) + ':\n')
        for row in points_v2_normal:
            text_file.write(str(row) + '\n')
        text_file.write('\n')
        final_outcome = solution_v2(points_v2_normal)
        print(final_outcome)
        score = solution_t(points_v2_normal,problem_amount)
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
        for row in points_v2_normal:
            text_file.write(str(row) + '\n')
        text_file.write('Time: ' + str(interval) + '\nScore: ' + str(round(score,0)) + '%\n')
        text_file.write('\n--------------------------------------------------------\n\n')
        
        print(interval)
        print(i)
        i = i + 1
    Avg_score = round((score_sum/trial_amount),2)
    Avg_time = (interval_sum/trial_amount)
    text_file.write('Total time: ' + str(interval_sum) + '%\nAverage time: ' + str(Avg_time) + '\nAverage score: ' + str(Avg_score) + '%\n\n')
    text_file.close()
    print(interval_sum)

trial(trial_amount,problem_amount)
#print(outcome_final)



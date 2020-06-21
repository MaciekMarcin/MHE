import random
import math
from datetime import datetime
import numpy as np
#from itertools import combinations
import copy
import operator
from scipy.stats import uniform
import sys
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib

#Utowrzenie latin square
def create_square(size: int):
    row = [i for i in range(1, size+1)]
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
    #size = len(points_v2_normal)
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
        print(size)
        result = outcome
        return result

def bruteforce_hard_way(points_v2_normal, problem_amount):
    Failed_tries = []
    while(True):
        problem_square = copy.deepcopy(points_v2_normal)
        for points in problem_square:
            for point in points:
                if(point == 'x'):
                    problem_square[problem_square.index(points)][points.index(point)] = random.randint(1,len(problem_square))
        if(problem_square in Failed_tries):
            continue
        score = solution_t(problem_square,problem_amount)
        if(score != 1):
            Failed_tries.append(problem_square)
        elif(score == 1):
            return problem_square
            break

def complete_bruteforce(points_v2_normal, problem_amount):
    easy_bruteforce = solution_v2(points_v2_normal)
    easy_bruteforce_score = solution_t(easy_bruteforce, problem_amount)
    if(easy_bruteforce_score < 1):
        hard_way_score = bruteforce_hard_way(points_v2_normal, problem_amount)
        return hard_way_score
    return easy_bruteforce
    

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
                final_point = None
                print('Final point score: ' + str(final_point_score))
                for each in range(1,len(points)+1):
                    i = each #random.randint(1,len(points_v2_climbing))
                    print('i: ' + str(i))
                    test_list = copy.deepcopy(points_v2_climbing)
                    loop_list = copy.deepcopy(points_v2_climbing) #jedyna opcja działająca kopiowania listy
                    #Trzeba pracować na kopii listy niż na oryginale
                    loop_list[loop_list.index(points)][points.index(point)] = i
                    score = solution_t(loop_list,problem_amount)
                    print('score of point: ' + str(score))
                    if(score >= final_point_score):
                        final_point_score = score
                        final_point = int(i)
                    if(each == len(points)):
                        points_v2_climbing[points_v2_climbing.index(points)][points.index(point)] = final_point
    print('final list: ' + str(points_v2_climbing)) #print final list
    return points_v2_climbing

def tabu_search_for_x(points_v2):
    x_counter = 0
    for points in points_v2:
        for point in points:
            if(point == 'x'):
                x_counter = x_counter + 1
    return x_counter


def taboo(points_v3):
    points_v2_normal = copy.deepcopy(points_v3)
    retry_list = copy.deepcopy(points_v3)
    h = 0
    for points in points_v2_normal:
        #points_v2_normal = np.transpose(points_v2_normal)
        #points_v2_normal = points_v2_normal.tolist()
        #points_v2_normal = get_rid_of_strings(points_v2_normal)
        j = 0
        for point in points:
            if(point == 'x'):
                
                print(j)
                candidates = []
                points_v2_transposed = np.transpose(points_v2_normal)
                points_v2_transposed = points_v2_transposed.tolist()
                points_v2_transposed = get_rid_of_strings(points_v2_transposed)
                taboo_list = sorted(np.unique(points+points_v2_transposed[j]))
                #taboo_list_x = sorted(np.unique(points))
                #taboo_list_y = sorted(np.unique(points_v2_transposed[points.index(point)]))
                print('points: ' + str(points))
                print('points_transposed: ' + str(points_v2_transposed[j]))
                #taboo_list = get_rid_of_strings(taboo_list)
                print(taboo_list)
                ####COPY OF HILL CLIMBING#####
                test_list = copy.deepcopy(points_v2_normal)
                #test_list[test_list.index(points)][points.index(point)] = len(points)
                final_point_score = solution_t(test_list,problem_amount)
                print('Final point score ' + str(final_point_score))
                #if(amount_of_generated_elements == 0):
                #    amount_of_generated_elements = 3*(len(points)+1)
                for each in range(1,len(points)+1):
                    i = each #random.randint(1,len(points_v2_normal))
                    test_list = copy.deepcopy(points_v2_normal)
                    loop_list = copy.deepcopy(points_v2_normal) #jedyna opcja działająca kopiowania listy
                    #Trzeba pracować na kopii listy niż na oryginale
                    loop_list[loop_list.index(points)][j] = i
                    score = solution_t(loop_list,problem_amount)
                    #print('score of point: ' + str(score))
                    point_and_score = [i,score]
                    candidates.append(point_and_score)
                    #print('Candidates: ' + str(candidates))
                print('Candidate with taboo: ' + str(candidates))
                #candidates = sorted(candidates, key=operator.itemgetter(0))
                for candidate in candidates[:]:
                    if(str(candidate[0]) in taboo_list):
                        candidates.remove(candidate)
                print('Candidate without taboo: ' + str(candidates))
                if(len(candidates) == 0):
                    highest_score = 'x'
                else:
                    #highest_score = candidates[0]
                    highest_score = ['x',solution_t(points_v2_normal,problem_amount)]
                for point_score in candidates:
                    if(point_score[1] > highest_score[1]):
                        highest_score = point_score
                points_v2_normal[points_v2_normal.index(points)][points.index(point)] = highest_score[0]
                print('Inserted: ' + str(highest_score[0]))
                taboo_list = []
            j = j + 1
        h = h + 1
    x_variable = tabu_search_for_x(points_v2_normal)
    #if(x_variable > 0):
    #    taboo(retry_list,amount_of_generated_elements)
    #else:
    print('final list ' + str(points_v2_normal)) #print final list

    ###########HYBRID BUILD START HERE#################
    x_final_counter = 0
    for points in points_v2_normal:
        for point in points:
            if(point == 'x'):
                x_final_counter = x_final_counter + 1
    if(x_final_counter > 0):
        points_v2_normal = climbing(points_v2_normal)
    ############HYBRID BUILD END HERE###################

    return points_v2_normal


def SA(points_v2_normal,first_temperature):
    
    #była możliwość zmiany funkcji temperatury.
    #była możliwość zmiany parametrów funkcji temperatury.
    #była możliwość ustalenia liczby iteracji.
    #była możliwość wypisania wartości funkcji celu dla kolejnych iteracji.

    #def T(k):
    #    T = 4000/k
    #    return T
    outcome = []
    for points in points_v2_normal:
        for point in points:
            #print(point)
            if(point == 'x'):
                test_list = copy.deepcopy(points_v2_normal)
                #test_list[test_list.index(points)][points.index(point)] = len(points)
                final_point_score = solution_t(test_list,problem_amount)
                final_point = None
                print('Final point score: ' + str(final_point_score))
                #if(amount_of_generated_elements == 0):
                #    amount_of_generated_elements = 4*(len(points)+1)
                for each in range(1,len(points)+1):
                    i = each #random.randint(1,len(points_v2_normal))
                    print('i: ' + str(i))
                    test_list = copy.deepcopy(points_v2_normal)
                    loop_list = copy.deepcopy(points_v2_normal) #jedyna opcja działająca kopiowania listy
                    #Trzeba pracować na kopii listy niż na oryginale
                    loop_list[loop_list.index(points)][points.index(point)] = i
                    score = solution_t(loop_list,problem_amount)
                    print('score of point: ' + str(score))
                    if(score >= final_point_score):
                        final_point_score = score
                        final_point = int(i)
                    else:
                        U = random.uniform(0,1)
                        counter = abs(score-final_point_score)
                        temperature = first_temperature/each
                        inside = counter/temperature
                        whole = math.exp(-inside)
                        if(U < whole):
                            final_point_score = score
                            final_point = int(i)
                        #else:
                        #    final_point_score = final_point_score
                        #    final_point = final_point

                    if(each == len(points)):
                        points_v2_normal[points_v2_normal.index(points)][points.index(point)] = final_point
    print(points_v2_normal)
                    #Dodań kolejną pętle aby wstawić cokolwiek co ma najwyższy score LUB na start dobierać 1 i dodawać to co ma lepszy score lub domyslnie 1
    print('final list: ' + str(points_v2_normal)) #print final list
    return points_v2_normal

def fitness(points_v2_score):
    i = 0
    j = 0
    for points in points_v2_score:
        for point in points:
            elements = len(points)
            if(point == 'x'):
                i = i# - 2
            elif(points.count(point) == 1):
                i = i + 1
            else:
                i = i# - 1# + 0.25
    points_v2_transposed = np.transpose(points_v2_score)
    points_v2_transposed = points_v2_transposed.tolist()
    print(points_v2_transposed)
    for points in points_v2_transposed:
        for point in points:
            elements = len(points)
            if(point == 'x'):
                j = j# - 2
            elif(points.count(point) == 1):
                j = j + 1
            else:   
                j = j# - 1# + 0.25
    score = (i + j)/(2*(len(points_v2_score)*len(points_v2_score)))
    return score

def mating_pool(pool_size,scores):
    scores_sorted = copy.deepcopy(scores)
    scores_sorted.sort(key=lambda sublist: sublist[0], reverse=True)
    pool = scores_sorted[:int(pool_size)]
    print('pool: ' + str(pool))
    return pool

def crossover_probability(a, b, probability):
    new_member_a = copy.deepcopy(a)
    new_member_b = copy.deepcopy(b)
    for points in new_member_a:
        for point in points:
            #if(point != new_member_b[new_member_a.index(point)]):
            #    if(probability < 1):
            #        if(random.random() <= probability):
            #            new_member_b[new_member_a.index(point)] = point
            print('test')
    for points in new_member_b:
        for point in points:
            #if(point != new_member_a[new_member_b.index(point)]):
            #    if(probability < 1):
            #        if(random.random() <= probability):
            #            new_member_a[new_member_b.index(point)] = point
            print('test')

    return new_member_a, new_member_b

def crossover_2nd_degree(parent_1, parent_2):
    crossover_index = random.randrange(1, round(len(parent_1)/2,0))
    crossover_index_2 = random.randrange(crossover_index + 1, len(parent_1))
    child_1 = parent_1[:crossover_index] + parent_2[crossover_index:]
    child_2 = parent_2[:crossover_index] + parent_1[crossover_index:]
    return child_1, child_2

def crossover_simple(parent_1, parent_2):
    crossover_index = random.randrange(1, len(parent_1))
    child_1 = parent_1[:crossover_index] + parent_2[crossover_index:]
    child_2 = parent_2[:crossover_index] + parent_1[crossover_index:]
    return child_1, child_2
        

def mutation(member, probability):
    New_member = copy.deepcopy(member)
    for points in New_member:
        for point in points:
            if(random.random() <= probability):
                New_member[New_member.index(points)][points.index(point)] = random.randint(1,len(New_member))
                print('MUTATION')
    return New_member

def create_population(problem_square):
    New_member = copy.deepcopy(problem_square)
    for points in New_member:
        for point in points:
            if(point == 'x'):
                New_member[New_member.index(points)][points.index(point)] = random.randint(1,len(New_member))
    return New_member

def create_generation(problem_square,amount):
    population = []
    for i in range(1,amount+1):
        population.append(create_population(problem_square))
    return population

def score_generation(population):
    scores = []
    for i in population:
        scores.append([fitness(i),i])
    scores.sort(key=lambda sublist: sublist[0], reverse=True)
    return scores


def Genetic(points_v2_normal,generation_size,mating_pool_size,iterations,cs_probability_percent,mutation_probability):
    population = create_generation(points_v2_normal,generation_size)
    best_candidates_scores = []
    score = []
    for each in population:
        print('each: ' + str(each))
    while(iterations > 0):
        scores_iteration = []
        print('SCORE: ' + str(scores_iteration))
        Sum_score = 0.0
        for i in population:
            scores_iteration.append([fitness(i),i])
            Sum_score = Sum_score + fitness(i)
        Avg_score = Sum_score/generation_size
        pool = mating_pool(mating_pool_size,scores_iteration)

        before_crossover = []
        crossover_population = []
        crossover_generation = []
        for each in pool:
            before_crossover.append(each[1])
        print('Before: ' + str(before_crossover))
        for element in before_crossover:
            crossover_population.append(element)
            before_crossover.remove(element)
            for parent in before_crossover:
                chance = random.random()
                if(chance < 0.5):
                    a, b = crossover_2nd_degree(element,parent)
                else:
                    a, b = crossover_simple(element,parent)
                #a, b = crossover_probability(element,parent,cs_probability_percent)                
                crossover_generation.append(a)
                crossover_generation.append(b)
        print('After: ' + str(crossover_generation))

        population_mutated = []
        for sample in crossover_generation:
            x = mutation(sample,mutation_probability)
            population_mutated.append(x)
        last_scoring = score_generation(population_mutated)
        print('Avg_score: ' + str(Avg_score))
        best_candidate = last_scoring[0]
        if(best_candidate[0] == 1):
            iterations = 0
        scores_iteration = []
        population = population_mutated
        iterations = iterations - 1
        print('Best: ' + str(best_candidate[1]))
    return best_candidate[1]


def solution_t(points_v2_score,problem_amount):
    i = 0
    j = 0
    for points in points_v2_score:
        for point in points:
            elements = len(points)
            if(point == 'x'):
                i = i# - 2
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
                j = j# - 2
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

def pick_algorithms():
    algorithms = []
    checked = '[x]'
    not_checked = '[ ]'
    bruteforce_check = not_checked
    hillclimb_check = not_checked
    tabu_check = not_checked
    SA_check = not_checked
    GA_check = not_checked
    while(True):
        choice = int(input('Select algorithm:\n' + str(bruteforce_check) + '1-Bruteforce\n' + str(hillclimb_check) + '2-Climbing\n' + str(tabu_check) + '3-Tabu Search\n' + str(SA_check) + '4-SA\n' + str(GA_check) + '5-GA\n6-Proceed\n'))
        if(choice != 6):
            if(choice == 1):
                if(bruteforce_check == checked):
                    bruteforce_check = not_checked
                    algorithms.remove(1)
                else:
                    bruteforce_check = checked
                    algorithms.append(1)
            if(choice == 2):
                if(hillclimb_check == checked):
                    hillclimb_check = not_checked
                    algorithms.remove(2)
                else:
                    hillclimb_check = checked
                    algorithms.append(2)
            if(choice == 3):
                if(tabu_check == checked):
                    tabu_check = not_checked
                    algorithms.remove(3)
                else:
                    tabu_check = checked
                    algorithms.append(3)
            if(choice == 4):
                if(SA_check == checked):
                    SA_check = not_checked
                    algorithms.remove(4)
                else:
                    SA_check = checked
                    algorithms.append(4)
            if(choice == 5):
                if(GA_check == checked):
                    GA_check = not_checked
                    algorithms.remove(5)
                else:
                    GA_check = checked
                    algorithms.append(5)
        else:
            return algorithms
            break

#Mode = int(input('Select mode:\n1-Trial\n2-Experiment\n'))
#Listy na kompletne listy z liczbami zamiast zmiennej
new_points_normal = []
new_points_transposed = []

problem_amount = 0
solution_amount = 0
trial_amount = int(input('How many test cases?: '))
print('Select algorithm:\n1-Bruteforce\n2-Climbing\n3-Taboo Search\n4-SA\n5-GA\n')
algorithm = pick_algorithms()
if(len(algorithm) == 0):
    sys.exit()
if(4 in algorithm):
    first_temp = int(input('Input the first temperature:\n'))
if(5 in algorithm):
    generation_size = int(input('Insert generation size: '))
    mating_pool_size = int(input('Declare mating pool: '))
    crossover_probability = float(input('Insert crossover probability from 0.01 to 1.00: '))
    mutation_probability = float(input('Insert mutation probability from 0.01 to 1.00: '))
    amount_of_iterations = int(input('How many iterations do you want? (amount_of_generated_elements):\n'))
#source = int(input('Select data source:\n1-From txt file\n2-Default source data\n'))
random_decision = int(input('Select mode:\n1-Manual\n2-Random\n'))
if(random_decision == 1):
    size = int(input('Input number (not applicable if you want input from file): '))
    problem_amount = int(input('How many unknown values do you want? (Max amount is: ' + str((size*size)-1) + '): '))
if(random_decision == 2):
    size = random.randint(2,10)
    problem_amount = random.randint(1,(size*size)-1)

points_v2 = create_square(size)
#outcome_final = []
points_from_txt = []

#print(points_v2_transposed.tolist())

amount_of_elements = len(points_v2)*len(points_v2)

def trial(trial_amount, problem_amount,option):
    interval_sum = 0
    score_sum = 0
    i = 1
    #if(source == 1):
    #    load_from_file()
    #    #points_v2 = points_from_txt
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
        if(option == 1):
            final_outcome = complete_bruteforce(points_v2_normal,problem_amount)
        elif(option == 2):
            final_outcome = climbing(points_v2_normal)
        elif(option == 3):
            final_outcome = taboo(points_v2_normal)
        elif(option == 4):
            final_outcome = SA(points_v2_normal,first_temp)
        elif(option == 5):
            final_outcome = Genetic(points_v2_normal,generation_size,mating_pool_size,amount_of_iterations,crossover_probability,mutation_probability)
        score = solution_t(final_outcome,problem_amount)
        score = (score-problem_amount)/((amount_of_elements-problem_amount)*2)
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
        print(score)
        print(i)
        i = i + 1
    Avg_score = round((score_sum/trial_amount),2)
    Avg_time = (interval_sum/trial_amount)
    text_file.write('Total time: ' + str(interval_sum) + '\nAverage time: ' + str(Avg_time) + '\nAverage score: ' + str(Avg_score) + '%\n\n')
    text_file.close()
    print(interval_sum)
    return interval_sum, Avg_time, Avg_score

def trial_v2(trial_amount, problem_amount,option):
    interval_sum = 0
    score_sum = 0
    i = 1
    #if(source == 1):
    #    load_from_file()
    #    #points_v2 = points_from_txt
    for each in range(0, trial_amount):
        before = datetime.now()
        points_v2_normal = copy.deepcopy(points_v2)
        problem(problem_amount,points_v2_normal)
        #points_v2_climbing = copy.deepcopy(points_v2_normal) # zbędna linia bo tylko kopiuje referencje i puszczam jeden algorytm naraz
        #######FROM HERE ONWARD BRUTEFORCE############
        if(option == 1):
            final_outcome = complete_bruteforce(points_v2_normal,problem_amount)
        elif(option == 2):
            final_outcome = climbing(points_v2_normal)
        elif(option == 3):
            final_outcome = taboo(points_v2_normal)
        elif(option == 4):
            final_outcome = SA(points_v2_normal,first_temp)
        elif(option == 5):
            final_outcome = Genetic(points_v2_normal,generation_size,mating_pool_size,amount_of_iterations,crossover_probability,mutation_probability)
        score = solution_t(final_outcome,problem_amount)
        score = score/(amount_of_elements*2)
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
        i = i + 1
    Avg_score = round((score_sum/trial_amount)*100,2)
    Avg_time = (interval_sum/trial_amount)
    return interval_sum, Avg_time, Avg_score

##########HERE GOES TRIAL BUT WITH MORE PROBLEMS##############
def final_go():
    Outcomes = []
    text_file = open('Result.txt', 'w')
    algorithm_name = None
    for each in algorithm:
        print(each)
        if(each == 1):
            algorithm_name = 'Bruteforce'
        elif(each == 2):
            algorithm_name = 'Hillclimb'
        elif(each == 3):
            algorithm_name = 'Tabu search'
        elif(each == 4):
            algorithm_name = 'SA'
        elif(each == 5):
            algorithm_name = 'Genetic algorithm'
        total_time, avg_time, avg_score = trial_v2(trial_amount,problem_amount,each)
        print(total_time)
        print(avg_time)
        print(avg_score)
        text_file.write('Algorithm: ' + str(algorithm_name) + '\n' + 'Total time: ' + str(total_time) + '\nAverage time: ' + str(avg_time) + '\nAverage score: ' + str(avg_score) + '%\n\n')
        x = [algorithm_name,str(total_time),str(avg_time),avg_score]
        Outcomes.append(x)
        total_time = None
        avg_time = None
        avg_score = None
    text_file.close()
    #return Outcomes
    graph = input('Do you want to see a bar chart? Y/N: \n')
    if(graph.upper() =='Y'):
        present_outcome_v2(Outcomes)
    else:
        sys.exit()

def time_converter(time):
    time = time * (10 ** -6)
    return time

def present_outcome_v2(outcomes):
    N = 2

    data_bruteforce = None
    data_hillclimbing = None
    data_tabu = None
    data_SA = None
    data_GA = None

    combined_timestamps = []
    for result in outcomes:
        stand_in = matplotlib.dates.datestr2num(result[1])
        stand_in = time_converter(stand_in)
        combined_timestamps.append(stand_in)
    print(combined_timestamps)

    avg_timestamps = []
    for result in outcomes:
        stand_in_avg = matplotlib.dates.datestr2num(result[2])
        stand_in_avg = time_converter(stand_in_avg)
        avg_timestamps.append(stand_in_avg)
    print(avg_timestamps)

    all_scores = []
    for result in outcomes:
        all_scores.append(result[3])
    print(all_scores)

    algorithms_names = []

    for result in outcomes:
        if(result[0] == 'Bruteforce'):
            algorithms_names.append(result[0])
        elif(result[0] == 'Hillclimb'):
            algorithms_names.append(result[0])
        elif(result[0] == 'Tabu search'):
            algorithms_names.append(result[0])
        elif(result[0] == 'SA'):
            algorithms_names.append(result[0])
        elif(result[0] == 'Genetic algorithm'):
            algorithms_names.append(result[0])

    objects = tuple(algorithms_names)
    y_pos = np.arange(len(outcomes))
    
    plt.bar(y_pos, tuple(all_scores), align='center', alpha=0.8)
    plt.xticks(y_pos, objects)
    plt.ylabel('Average score in %')
    plt.title('Average score per algorithm')
    
    plt.show()

    plt.bar(y_pos, tuple(combined_timestamps), align='center', alpha=0.8)
    plt.xticks(y_pos, objects)
    plt.ylabel('Total time in seconds')
    plt.title('Total time per algorithm')
    
    plt.show()

    plt.bar(y_pos, tuple(avg_timestamps), align='center', alpha=0.8)
    plt.xticks(y_pos, objects)
    plt.ylabel('Average time in seconds')
    plt.title('Average time per algorithm')
    
    plt.show()

final_go()


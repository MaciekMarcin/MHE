# MHE
Repozytorium MHE zaoczne 2019/2020

Tematem moim jest Latin Square i problem czy jest możliwe dokończenie niekompletnego kwadratu tak aby w osi poziomej jak i pionowej występował tylko raz każdy element.

Kwadrat jest reprezentowany jako Listy zagnieżdżone w Liście. Element nieznany jest generowany losowo, ilość takich elementów przekazuje się w parametrze. Ilość nieznanych elementów może wynosić maksymalnie (n^n)-1 gdzie n to liczba elementów w rzędzie, a -1 dlatego że problem opiera się na dokończeniu niekompletnego rozwiązania zamiast stworzenia nowego kwadratu.

Po głębszym zastanowieniu się, problem ten przypomina sudoku, ale gorsze. Dlaczego?
-Sudoku posiada określony rozmiar planszy (9 kwadratów rozmiaru 3x3), gdzie tutaj mamy dowolność.
-W przypadku uzupełniania sudoku możemy korzystać z zależności że kwadrat składa się z 9 mniejszych kwadratów przez co łatwiej da się go wypełnić
-Niektóre metaheurystyki/algorytmy nie mają sensu w przypadku latin square.

Program pierw uzupełnia każdą listę która jest w pozycji początkowej po czym obraca tę listę na poniższej zasadzie:

*Zmienia*:
|1|a|b
|-|-|-
|2|c|d

*Na*:
|1|a|c
|-|-|-
|2|b|d

Jeżeli nie ma dwóch takich samych wartości w żadnej liście to jest ona uzupełniona poprawnie. Taką samą procedurę wykonuje, ale w drugą stronę. W przeciwnym wypadku jakość rozwiązania które nie byłoby idealne może być mierzone poprzez sprawdzenie ile pozycji, które zostały zastąpione niewiadomymi, zgadza się z oryginalną tabelą na wejściu.

Brutefore polega na sprawdzeniu podobieństwa aktualnego rzędu z każdą możliwą kombinacją i ta kombinacja która jest najbardziej prawdopodobna zajmuje miejsce tego rzędu. Wszystko to przy założeniu początkowym że elementy następują po sobie w jakiejś kolejności. Jeśli jakiś rząd jest pusty to po transpozycji, będzie on zawierał przynajmniej jeden element i jest to wystarczająca ilość aby dopasować jakąś kombinacje dla tego rzędu.

Algorytm wspinaczkowy polega na wstawieniu do listy na miejsce niewiadomej każdego możliwego rozwiązania po czym sprawdza wynik ogólny. Na koniec umieszczany jest w liście element przy którym ogólny wynik był największy.

Algorytm wyszukiwania tabu działa podobnie do algorytmu wspinaczkowego lecz dodaje już istniejące elementy z listy poziomej i pionowej do tabu aby tych elementów nie wstawiać do listy nawet jeśli wynik jest większy.

Algorytm symulowanego wyżarzania działa podobnie do algorytmu wspinaczkowego/tabu lecz jest tam również temperatura i może przez to wybrać gorze rozwiązanie jeżeli jest prawdopodobieństwo osiągnięcia wyższego wyniku w późniejszym okresie, poza maksimum lokalnym.

Algorytm genetyczny różni się od poprzednich poprzez uzupełnienie kwadretu na samym początku kilka razy, w zależności od określonego rozmiaru populacji w generacji, losowymi liczbami z zakresu. Po czym następuje wybranie próbek do rozmnożenia które zostanną poddane krzyżowaniu jednopunkowemu lub wielopunktowemu oraz mutacji po czym proces zacznie się na nowo, w zależności od tego ile iteracji zostało przewidzianych na początku. Lub gdy znajdziemy idealnego kandydata z maksymalnym wynikiem.

Rezultaty są potem zbieranie i są przedstawiane na wykresach. 
Do rezultatów zalicza się:
-Całkowity czas działania
-Średni czas działania
-Średni wynik



# MHE
Repozytorium MHE zaoczne 2019/2020

Tematem moim jest Latin Square i problem czy jest możliwe dokończenie niekompletnego kwadratu tak aby w osi poziomej jak i pionowej występował tylko raz każdy element.

Kwadrat jest reprezentowany jako Listy zagnieżdżone w Liście. Element nieznany jest generowany losowo, ilość takich elementów przekazuje się w parametrze. Ilość nieznanych elementów może wynosić maksymalnie (n^n)-1 gdzie n to liczba elementów w rzędzie, a -1 dlatego że problem opiera się na dokończeniu niekompletnego rozwiązania zamiast stworzenia nowego kwadratu.

Program pierw uzupełnia każdą listę która jest w pozycji początkowej po czym obraca tę listę na poniższej zasadzie:

*Zmienia*:
|1|a|b
|-|-|-
|2|c|d

*Na*:
|1|a|c
|-|-|-
|2|b|d

Jeżeli nie ma dwóch takich samych wartości w żadnej liście to jest ona uzupełniona poprawnie. Taką samą procedurę wykonuje, ale w drugą stronę gdyż najczęściej tylko 1 z 2 tych opcji działa bez pomyłek. W przeciwnym wypadku jakość rozwiązania które nie byłoby idealne może być mierzone poprzez sprawdzenie ile pozycji, które zostały zastąpione niewiadomymi, zgadza się z oryginalną tabelą na wejściu.

Dla uproszczenia program działła tylko na kwadratach 3x3. Większe byłyby może i możliwe gdyby nie transpozycja na którą ciężko znaleść inną metodę, póki co może działać i na większą liczbę niż 3x3, ale polega to na dokładaniu dodatkowego parametru/linii kodu w kilku/kilkunastu miejscach, ale generalnie sam koncept i wykonanie wygląda dalej tak samo.

Brutefore polega na sprawdzeniu podobieństwa aktualnego rzędu z każdą możliwą kombinacją i ta kombinacja która jest najbardziej prawdopodobna zajmuje miejsce tego rzędu. Wszystko to przy założeniu początkowym że elementy następują po sobie w jakiejś kolejności. Jeśli jakiś rząd jest pusty to po transpozycji, będzie on zawierał przynajmniej jeden element i jest to wystarczająca ilość aby dopasować jakąś kombinacje dla tego rzędu.

Algorytm wspinaczkowy polega na wstawieniu do listy na miejsce niewiadomej każdego możliwego rozwiązania po czym sprawdza wynik ogólny. Na koniec umieszczany jest w liście element przy którym ogólny wynik był największy.

Algorytm wyszukiwania tabu działa podobnie do algorytmu wspinaczkowego lecz dodaje już istniejące elementy z listy poziomej i pionowej do tab u aby tych elementó nie wstawiać do listy nawet jeśli wynik jest większy.

Rezultaty są nawet eksportowane do excela i tam są one dopieszczane.



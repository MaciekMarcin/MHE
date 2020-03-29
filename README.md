# MHE
Repozytorium MHE zaoczne 2019/2020

Tematem moim jest Latin Square i problem czy jest możliwe dokończenie niekompletnego kwadratu tak aby w osi poziomej jak i pionowej występował tylko raz każdy element.

Kwadrat jest reprezentowany jako Listy zagnieżdżone w Liście. Element nieznany jest generowany losowo, ilość takich elementów przekazuje się w parametrze choć na chwilę obecną mogą być dwa nieznane elementy na jednym miejscu przez co jest faktycznie jeden tylko taki element, zależy od RNG. W Przypadku większej liczby elementów program działa dość "Na czuja" jako że łatwiej jest zrobić latin square niż próbować go dokończyć z brakującymi elementami już istniejącymi.

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

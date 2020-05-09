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

Dla uproszczenia program działła tylko na kwadratach 3x3. Większe byłyby może i możliwe gdyby nie transpozycja na którą ciężko znaleść inną metodę, póki co może działać i na większą liczbę niż 3x3, ale polega to na dokładaniu dodatkowego parametru/linii kodu w kilku/kilkunastu miejscach, ale generalnie sam koncept i wykonanie wygląda dalej tak samo.

Brutefore polega na sprawdzeniu innych pozycji na liście i tych które są w liscie pionowej aby upewnić się czy aby napewno ten element wstawić.

Rezultaty są nawet eksportowane do excela i tam są one dopieszczane.



uruchomienie projektu poprzez uruchomienie modułu main.py

uruchomienie testów poprzez uruchomienie modułu test.py

Sposob działania programu:
1. wczytuje jedno wyrazenie ze standardowego wejścia
2. sprawdza czy podane wyrazenie jest poprawne, jesli jest kontynuuje
3. sprawdza czy jest Tautologią albo zawsze sprzeczne i konczy dzialanie zwracajac T badz F
4. tworzy mozliwie jak najkrotsze wyrazenie DNF uzywajac tablicy prawdy wyrazenia podanego uzywajac kodu z labolarium
   (zbedne zmienne sa usuwane)
5. probuje znalezc krótsze wyrazenie niz znalezione DNF czy podane
   z uzyciem generowania wszystkich mozliwych najkrotszych, poprawnych wyrazen w postaci ONP 
   ktore sa takie same pod wzgledem tablicy prawdy
   (ma na to okreslona liczbe prob stala MAX_ITERATIONS)
6. zwraca najkrotsze ze znalezionych wyrazen w postaci normalnej

Algorytm bewzglednie zwraca poprawne wyrazenie.

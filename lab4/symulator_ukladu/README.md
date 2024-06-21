# uruchomienie

## generowanie pliku ukladu bramek:

```bash
python 01_bramki.py
```

## aplikacja okienkowa:

```bash
python led.py
```

## aplikacja symulacji:

```bash
python sim0.py <nazwa_pliku>.ttl
```

## do projeku

zmapowac wazne punkty na graf
potrzebny slownik tak aby znac stan punktu (0/1)

monza naraz graf ewaulowac albo nie i pomijac niektore fragmenty

```python
uklad = [ ('NAND', a , b , p1), ('NAND' , c ,d , p2), ('NAND', p1 , p2 , o2) ]

no i to jest kolejka fifo, do ewaluacji z uzyciem cashu stanu

```

wdl mnie ten obliczacz
to powinien byc bfs albo dfs po tych bramkach
idacy z inputupw na outputy

### TODO

zrobic inteligenty frontend co ciagnie z pliku konguracyjnego ile i jakie zarowki
zrobic wyswietlacz siedem segmentow

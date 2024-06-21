# Instrukcja uruchomienia
gra sklada sie z kilku modulow:

- sama gra z trojkatami (przykład działania)

  ```python triangle_game.py```
- modul główny

  ```python main.py```

zainstalować potrzebne biblioteki:
```bash
pip install -r requirements.txt
```

uruchomić grę można z poziomu katalogu projektu:
```bash
python main.py
```

# Informacje o grze
Moja gra polega na odpowiednim ułożeniem trójkątów w taki sposób,
aby wszystkie trójkąty były w tym samym kolorze.
Po naciśnieciu w trójkat zmienia sie jego kolor na kolejny i jego sąsiadów.
Sąsiadami są wszystkie trójkąty, które mają część wspólną z kołem opisanym na tym trójkącie.

# Opis modułów
- triangle_game.py
  - zawiera logike gry z trójkątami
  - może być uruchomiony samodzielnie w trybie testowym
- main.py
  - moduł główny z interfejsem użytkownika
  - uruchamia grę
- LinkedListsCollection.py
  - klasa CyclicList - przechowuje listę elementów w sposób cykliczny
- GameEngineCreator.py
  - klasa GameEngineCreator - tworzy obiekt ogólny obiekt gry
  - używając tej klasy ala fabryki można stworzyć obiekt gry z dowolnymi parametrami
  - np. można stworzyć grę z trójkątami o dowolnej ilości wierszy i kolumn
  - można stworzyć inne gry, które korzystają z tej samej logiki gry z innymi krztałtami itd.
- Options.py
  - klasa Options - przechowuje opcje dla gry
- Shapes.py
  - klasa ClickablePolygon - klasa bazowa dla kształtów, które można kliknąć
  - klasa ClickableTriangle - klasa dla trójkąta z możliwością kliknięcia, dziedzicza po ClickablePolygon



# 🎮 Projekt 3: Analiza Rynku Gier (Steam)

### 🎯 Cel projektu
Eksploracyjna analiza danych (EDA) potężnego zbioru informacji o ponad 26 000 pozycjach z platformy Steam. Projekt ma na celu wyczyszczenie surowych danych oraz wyciągnięcie wniosków biznesowych dotyczących cen, popularności (playtime) i konkretnych deweloperów.

### 🛠️ Narzędzia i Biblioteki
* **Python 3.x**
* **Pandas:** Do czyszczenia (Data Wrangling), filtrowania i agregacji danych.
* **PyCharm & Git:** Środowisko pracy i kontrola wersji.

### 🔍 Aktualne postępy i wnioski
1. **Wczytanie i Inspekcja:** Załadowanie bazy ponad 26 tys. wierszy i analiza braków danych (tzw. missing values).
2. **Czyszczenie Danych (Data Cleaning):** Wyizolowanie i usunięcie wierszy z brakującymi tytułami gier przy użyciu `.dropna(subset)`.
3. **Analiza Cen (Anomalie):** Posortowanie bazy według ceny wykazało, że najdroższymi "grami" na platformie są w rzeczywistości specjalistyczne programy użytkowe (np. silniki graficzne i programy do edycji wideo, kosztujące nawet blisko 600$).

### 🔜 Planowane analizy (Work in Progress)
* [ ] Znalezienie gier z najwyższym wskaźnikiem zaangażowania graczy (average playtime).
* [ ] Analiza polskiego gamedevu (filtrowanie po deweloperach takich jak CD PROJEKT RED).
# 🍿 Projekt 2: Analiza bazy Netflix (Python & Pandas)

### 🎯 Cel projektu
Głównym celem tego projektu było przeprowadzenie procesu **Data Wrangling** (czyszczenia i transformacji danych) na dużym, rzeczywistym zbiorze zawierającym ponad 8000 tytułów z platformy Netflix. Skupiłem się na analizie brakujących informacji, filtrowaniu określonych typów treści oraz wyciąganiu technicznych wniosków.

### 🛠️ Narzędzia i Biblioteki
* **Python 3.x**
* **Pandas:** Do manipulacji i czyszczenia danych.
* **PyCharm:** Jako główne środowisko programistyczne (IDE).
* **Git i GitHub:** Do kontroli wersji i publikacji projektu.

### 🔍 Główne zadania techniczne
1. **Obsługa brakujących danych:** Zidentyfikowanie i wypełnienie blisko 2000 brakujących wartości w kolumnie `director` (reżyser).
2. **Transformacja typów danych:** Konwersja kolumny `duration` (czas trwania) z formatu tekstowego (np. "90 min") na liczby całkowite (integers), aby umożliwić obliczenia matematyczne.
3. **Zaawansowane filtrowanie:** Zastosowanie masek logicznych (Boolean Masking) do oddzielenia filmów od seriali oraz sprawnego wyszukiwania konkretnych tytułów na podstawie lat premier.

### 💡 Wyniki i Wnioski
* **Najdłuższy film:** Ustalono, że najdłuższym filmem na platformie jest "Black Mirror: Bandersnatch" z czasem trwania **312 minut**.
* **Filtrowanie historyczne:** Z powodzeniem wyekstrahowano klasyki z 1942 roku, takie jak "Prelude to War".
* **Wydajność:** Pomyślnie załadowano i przetworzono potężną bazę danych składającą się z **8807 wierszy** i **12 kolumn**, co w Excelu byłoby uciążliwe.
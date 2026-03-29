-- 1. Kto zarabia powyzej 10k?
SELECT Stanowisko, Miasto, Pensja_PLN FROM zarobki_it WHERE Pensja_PLN > 10000;

-- 2. Zarobki w Olsztynie malejaco
SELECT * FROM zarobki_it WHERE Miasto = 'Olsztyn' ORDER BY Pensja_PLN DESC;

-- 3. Srednia pensja dla Pythona
SELECT Jezyk, ROUND(AVG(Pensja_PLN), 0) AS Srednia_Pensja FROM zarobki_it WHERE Jezyk = 'Python';
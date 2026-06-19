# System organizacji imprez i wydarzeń

Projekt zaliczeniowy realizujący architekturę MVC w technologii Django. Aplikacja służy do planowania wydarzeń oraz dynamicznego zarządzania powiązanymi z nimi listami gości.

---

## Spis treści
1. [Funkcjonalności projektu](#funkcjonalności-projektu)
2. [Instrukcja obsługi (Uruchomienie aplikacji)](#instrukcja-obsługi-uruchomienie-aplikacji)

---

## Funkcjonalności projektu

W systemie zaimplementowano następujące mechanizmy:
* **Chronologiczna lista wydarzeń:** Przegląd wszystkich zaplanowanych imprez automatycznie posortowanych od najbliższej do najdalszej.
* **Tworzenie i edycja wydarzeń (CRUD):** Formularze pozwalające dodawać nowe oraz modyfikować istniejące imprezy (nazwa oraz data/godzina wybierana z kalendarza, która automatycznie zachowuje swoją wartość podczas edycji).
* **Zarządzanie listą gości:** Dedykowany podgląd szczegółów każdego wydarzenia z listą zapisanych osób oraz licznikiem uczestników.
* **Szybkie dodawanie gości w formularzu:** Możliwość wpisania pierwszych gości od razu podczas tworzenia wydarzenia.
* **Dynamiczne rozszerzanie listy (JavaScript):** Przycisk na froncie pozwalający na asynchroniczne dodawanie kolejnych pól dla gości w formularzu (bez przeładowywania strony).
* **Interaktywna zmiana obecności:** Szybkie przełączanie statusu gościa (*Potwierdzony* / *Oczekuje*) jednym kliknięciem myszy bezpośrednio na liście gości.

---

## Instrukcja obsługi (Uruchomienie aplikacji)

Aby zainstalować wymagane paczki i uruchomić aplikację w środowisku lokalnym, wykonaj poniższe kroki w terminalu:

### 1. Przygotowanie środowiska wirtualnego
* **macOS / Linux:**

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

* **Windows:**

  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

### 2. Instalacja wymaganych pakietów
Projekt wymaga instalacji frameworka Django. Wpisz w terminalu:

### **Uwaga** Na Windows w ponizszych komendach uzyj słowa python zamiast python3
```bash
python3 -m pip install django
```

### 3. Inicjalizacja bazy danych (Migracje):
Przygotuj strukturę tabel w pliku lokalnej bazy danych SQLite:

```bash
python3 manage.py makemigrations events
python3 manage.py migrate
```

### 4. Uruchomienie lokalnego serwera:
Wystartuj aplikację komendą:

```bash
python3 manage.py runserver
```

Po uruchomieniu serwera aplikacja jest gotowa do użytku. Otwórz przeglądarkę internetową i przejdź pod adres wyświetlony w terminalu, np. http://127.0.0.1:8000/


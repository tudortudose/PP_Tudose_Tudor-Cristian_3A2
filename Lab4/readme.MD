# ♣ Python Programming ~ Lab 4 ♣️

## Tasks: ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/100)

```
✅ 1) Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director. 

Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul dat ca parametru.

Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’ 

✅ 2) Să se scrie o funcție ce primește ca argumente două căi: director si fișier. 

Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută a fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A. 

✅ 3) Să se scrie o funcție ce primește ca parametru un string my_path.

Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului. Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count), sortată descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie. Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru. 

✅ 4) Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.

Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie, deci nu va apărea în lista finală. 

✅ 5) Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și returneaza o listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier, se caută doar in fișierul respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel director. Dacă target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.

✅ 6) Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că primește un parametru în plus: o funcție callback, care primește un parametru, iar pentru fiecare eroare apărută în procesarea fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru.

✅ 7) Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer si returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier, file_size = dimensiunea fisierului in octeti, file_extension = extensia fisierului (daca are) sau "", can_read, can_write = True/False daca se poate citi din/scrie in fisier.

✅ 8) Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea către un director aflat pe disc. Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path.

Exemplu apel funcție: functie("C:\\director") va returna ["C:\\director\\fisier1.txt", "C:\\director\\fisier2.txt"]
```

#### Note: Each exercise is solved in a separated file (with its name) and tested in main file.

### Author: Tudor-Cristian Tudose 3A2
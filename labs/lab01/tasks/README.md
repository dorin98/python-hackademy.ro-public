# Lab 1

##### Install `pytest` using `install-pytest.sh`.
##### Run the checker using `pytest-3 check.py`.

1. Sa se citeasca un numar N de la tastatura si sa se afiseze toate numerele 
prime <= N.

2. Se citeste un numar N si N tupluri de forma (x, y, t).
Sa se afiseze, in functie de t, urmatoarele:
 - t = 'i' -> rezultatul impartirii lui x la y ca numere intregi
 - t = 'f' -> rezultatul impartirii lui x la y ca si numere reale 
 - t = 'p' -> rezultatul ridicarii lui x la puterea y

3. Fie doua liste citite de la tastatura ce contin numere intregi. Creati o a 
treia lista care sa contina:
a) reuniunea
b) intersectia
c) diferenta

4. Creati un program care sa calculeze al N-lea termen Fibonacci, N fiind citit 
de la tastatura.

5. Dandu-se doua liste, sortati fiecare lista, dupa care interclasati-le.

6. List Comprehensions!
Se citesc 3 litere - L1, L2, L3. Sa se afiseze toate perechile (i, j, k), unde 
i <= L1, j <= L2, k <= L3, ce nu contin doua vocale/consoane consecutive.

```
Ex.
    L1 = L2 = 'b'
    L3 = 'c'
Rezultat:    
a b a
b a b
b a c
```

7. 	Splits & Joins!
Sa se transforme o adresa de email de tipul `prenume1_prenume2.nume@yahoo.com` 
in `prenume1.nume@gmail.com`.

```python
string = "This\\is\\a\\Windows\\path"
print(string)
print(string.replace('\\', '/').replace('Windows', 'Linux'))
# Pentru a 'modifica' stringul initial folositi urmatoarea instructiune:
# string = string.replace('\\', '/').replace('Windows', 'Linux')
# [Reminder] Strings are immutable!

# _string_.split(_token_) returneaza o lista
url = 'www.google.com'
tokens = url.split('.')
print(tokens)

# '_token_'.join(_list_) returneaza un string
# Obs: .split() are ca argument default caracterul spatiu
function = 'bad~!$@ function name'
f = '_'.join(function.split()[1:]) # Ce credeti ca face [1:]?
print(f)
```

8. Dandu-se un text si o lista de cuvinte, inlocuiti toate aparitiile acestor
cuvinte cu rasturnatele lor.

9. Scrieti un program care primeste un string S si un numar K si elimina toate
caracterele de pe pozitiile mulipli de K.

10. Cititi un text de la tastatura si sortati cuvintele descrescator dupa 
numarul de aparitii.

11. Creati o functie care primeste doua dictionare si le unifica intr-un nou
dictionar, pe care il returneaza ulterior.

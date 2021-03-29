#!/usr/bin/env python
# coding: utf-8

# # Laboratorium 2

# ## Przypomnienie

# In[1]:


-493092, -313, 1, 19209, 3294052823049210391203910293003481039      # liczba całkowita
-393923.8132132, -1.0000001, 9031023901248120.2103912               # liczba zmiennoprzecinkowa
'kotek ma płotek', "kota", 'lubię pisać programy w Pythonie'        # Łańcuchy znakowe
True, False                                                         # Wartości logiczne


# ### Zmienna
# Zmienną nazwany obszar w pamięci komputera pod którym można przechowywać dane. Innaczej można sobie wyobrazić ją jako podpisane (na początku puste) pudełko do którego wsadzamy określone rzeczy. 
# 
# Nazwa zmiennej jest dowolna, jednak sugerowane jest nazywanie jest zgodnie z przeznaczeniem lub informacją którą ma przechowywać.
# 
# przykłady:
# 

# In[2]:


imie = 'Michał'             # zmienna przechowująca łańcuch znakowy Michał
liczba_calkowita = 5        # zmienna przechowująca wartość liczbową 5
liczba_rzeczywista = 3.44   # zmienna przechowująca liczbę rzeczywistą 3.44
prawda = True               # zmienna przechowująca wartość logiczną (True / False)
type(imie), type(liczba_calkowita), type(liczba_rzeczywista), type(prawda)


# Język Python jest dynamicznym językiem programowania, typ zmiennej jest określany w trakcie przypisania na podstawie wartości.

# In[3]:


zmienna1 = 'Paweł'    # jest to teraz zmienna typu str (String - Łańcuch znakowy)
print(f'zmienna1={zmienna1}, typ={type(zmienna1)}')
zmienna1 = 12345      # teraz typ zostanie określony na int (Integer - liczba całkowita)
print(f'zmienna1={zmienna1}, typ={type(zmienna1)}')
zmienna1 = 0.4533113  # nowy typ na podstawie przypisania wartości do zmiennej będzie: float (liczba zmienno przecinkowa)
print(f'zmienna1={zmienna1}, typ={type(zmienna1)}')


# ### Operacje artmetyczne
# 
# przykłady:

# In[4]:


# Dodawanie
5 + 10


# In[5]:


# Odejmowanie
4 - 8


# In[6]:


# mnożenie
7 * 19


# In[7]:


# Potęgowanie
3 ** 4


# In[8]:


# Dzielenie
8 / 9


# In[9]:


# Dzielenie całkowite
8 // 9   # to samo co: int(8 / 9)


# In[10]:


# Reszta z dzielenia (znak modulo)
9 % 4  


# ### Operacje na łańcucach znakowych
# 
# przykłady:

# In[11]:


# łączenie łańcuchów znakowych
'kot' + ' lubi mleko'


# In[12]:


# łączenie łańcuchów znakowych z przypisaniem do nowej zmiennej
tekst = 'kot' + ' lubi mleko'
print(tekst)


# In[13]:


# łączenie dwóch zmiennych typu str (string) z wykorzystaniem znaku +
kot = 'Kot'
lubi = 'lubi mleko'
tekst = kot + ' ' + lubi  # ' ' znak spacji dodany po środku, w innym przypadku otrzymalibyśmy 'Kotlubi mleko'
print(tekst)


# In[14]:


# powielanie łańcuchów znakowych
'$' * 10


# In[15]:


# Długość łańcucha znakowego
len('ala ma kota')


# In[16]:


tekst = 'ala ma kota'
len(tekst)


# In[17]:


# porównanie , operator ==
tekst1 = 'ala ma kota'
tekst2 = 'ala ma psa'
tekst1 == tekst2


# In[18]:


# porównanie , operator ==
tekst1 = 'ala ma kota'
tekst2 = 'ala ma kota'
tekst1 == tekst2


# Formatowanie tekstu:

# In[19]:


# z wykorzystaniem f-string
imie = 'Ala'
co = 'Kota'
wiadomosc = f'{imie} ma {co}'
wiadomosc


# In[20]:


# z wykorzystaniem  str.format() (https://docs.python.org/3/library/stdtypes.html#str.format)
imie = 'Ala'
co = 'Kota'
wiadomosc = '{} ma {}'.format(imie, co)  # kolejność ma znaczenie
wiadomosc


# In[21]:


# Stary sposób formatowania z wykorzystaniem %
imie = 'Ala'
co = 'Kota'
wiadomosc = '%s  ma %s' % (imie, co)
wiadomosc


# ### Wbudowane funkcje
# 
# * [help](https://docs.python.org/3/library/functions.html#help)
# * [print](https://docs.python.org/3/library/functions.html#print)
# * [input](https://docs.python.org/3/library/functions.html#input)
# * [len](https://docs.python.org/3/library/functions.html#len)
# * [type](https://docs.python.org/3/library/functions.html#type)
# * [dir](https://docs.python.org/3/library/functions.html#dir)

# In[22]:


help(print)


# In[23]:


print('hello from python')
print("hello from print")


# In[24]:


tekst = input('Podaj jakiś łańcuch znakowy: ')


# In[25]:


print(tekst, len(tekst))


# ## Zadania

# ### Kolekcje danych

# #### Zadanie 1
# Utwórz listę zawierającą liczby całkowite, sprawdź jej rozmiar przy użyciu funkcji `len`.

# In[44]:


list = [1, 2, 3, 4, 5, 6]
len(list)


# #### Zadanie 2
# Zapisz listę do nowej zmiennej, następnie dodaj kolejną liczbę całkowitą korzystając z methody `append`, sprawdź zawartość obu list.

# In[45]:


list2 = list.copy()
list.append(7)
list, list2


# #### Zadanie 3
# Wykonaj operację dodawania na dwóch dowolnych listach zawierających liczby, a następnie zsumuj ([sum](https://docs.python.org/3/library/functions.html#sum)) wynik operacji dodawania i wyświetl go na ekranie.

# In[47]:


list3 = list + list2
print(list3)
print(sum(list3))


# #### Zadanie 4
# Utwórz dwa zbiory liczbowe a następnie wykonaj następujące działania na nich: 
# 
# 
# *   & (and)
# *   | (or)
# *   ^ (xor)
# 
# Zapisz wyniki do nowych zmiennych, oraz wyświetl je (zmienne) na ekranie.
#  
# 
# 

# In[52]:


X = {1, 2, 3, 6, 8, 9}
Y = {1, 3, 4, 7, 8, 9}

print(X & Y)
print(X | Y)
print(X ^ Y)


# #### Zadanie 5
# Wykonaj operację dodawania dwóch zbiorów (**?**). 
# 
# Czy da się taką operację wykonać? Jeżeli nie, to czy można coś z tym zrobić?
# 
# 
# 
# 

# In[53]:


Z = X.union(Y)  # X | Y
print(Z)


# #### Zadanie 6
# Utwórz słownik o nazwie koszyk w którym kluczami będą nazwy owoców a wartościami dowolna liczba całkowita. Wyświetl na ekranie wartość dla dowolnie wybranego przez Ciebie klucza.
# 

# In[56]:


basket = {
    'apple': 2,
    'banana': 8,
    'grape': 13
}

print(basket['grape'])


# #### Zadanie 7
# Korzystając z operatora przynależności `in`, sprawdź czy w poniższej liście znajduje się wartość `'kot'` oraz `3`. Wypisz wynik na ekranie.
# ```python
# li = [3,4,'pies', 1,2]
# ``` 
# 

# In[60]:


li = [3,4,'pies', 1,2]
print('kot' in li, 3 in li)


# ### Struktury kontrolne

# #### Zadanie 1
# Napisz kod który pobierze od użytkownika imię, jeżeli `imie == 'Azor'` to przywitaj go `'Dobry piesek!'`.
# 
# Przykład 1:
# ```shell
# Podaj imię > Michal
# Witaj Michal!
# ```
# 
# Przykład 2:
# ```shell
# Podaj imię > Azor
# Dobry piesek!
# ```
# 
# 

# In[64]:


imie = input('Podaj imię: ')
if imie == 'Azor':
  print('Dobry piesek!')
else:
  print(f'Witaj {imie}!')


# #### Zadanie 2
# Napisz prosty kalkulator, użytkownik powinien móc wprowadzić liczby zmiennoprzecinkowe (`float`).
# 
# przykład:
# ```shell
# Podaj pierwszą liczbę > 1.5
# Podaj drugą liczbę > 3.5
# Podaj operację (+,-,*,/) > -
# wynik: -2.0
# ```

# In[113]:


first_number = float(input('Podaj pierwszą liczbę > '))
second_number = float(input('Podaj drugą liczbę > '))
operation = input('Podaj operację (+,-,*,/) > ')
try:
    if operation == '+':
      wynik = first_number + second_number
    elif operation == '-':
      wynik = first_number - second_number
    elif operation == '*':
      wynik = first_number * second_number
    elif operation == '/':
      wynik = first_number / second_number
    else:
      wynik = 'Błąd!'

    print(f'Wynik: {wynik}')
except ZeroDivisionError:
    print('Hej! Nie dziel przez zero!')


# #### Zadanie 3
# Korzystając z operatora przynależności `in` sprawdź czy podana wartość przez użytkownika znajduje się w liście (z dowolnymi wartościami wybranymi przez Ciebie). Jeżeli wartość znajduje się na liście wyświetl jakiś tekst użytkownikowi.
# 

# In[96]:


value = input('Wartosc: ')

if value in ['kraby', 'są', 'super', '!']:
  print(f'Brawo! Znaleziono {value} w liście.')
else:
  print('No niestety :(')


# #### Zadanie 4
# Przeiteruj po zbiorze liczb, oraz dodaj sprawdzenie czy aktualna liczba spełnia któryś z warunków:
# 
# *  większa
# *  mniejsza
# *  równa 0
# 
# Wyświetl informację użytkownikowi jaki warunek został spełniony.

# In[ ]:


for liczba in [3, 46, 2, 1, 6, 8, 45, -2, -6, 0]:
  if liczba > 0:
    print(f'{liczba} Jest większa od 0.')
  elif liczba < 0:
    print(f'{liczba} Jest mniejsza od 0.')
  else:
    print('liczba jest zerem!')


# #### Zadanie 5
# Przeiteruj po słowniku `koszyk` utworzonym wcześniej, i wyświetl na ekranie nazwę oraz ilość danego owoca w koszyku.
# 
# Na przykład:
# ```
# Banan : 3
# Jabłka : 2
# ```
# 

# In[102]:


for fruits in basket:
  print(f'{fruits}: {basket[fruits]}')


# #### Zadanie 6
# Pobierz od użytkownika 5 wartości i umieść je w zbiorze (set.add). Wyświetl zbiór na ekranie.
# 

# In[105]:


A = set()
while len(A) < 5:
  try:
    value = input('Podaj wartość: ')
    A.add(int(value))
  except ValueError:
    print('Podaj poprawną liczbę')

print(A)


# In[ ]:





# In[ ]:





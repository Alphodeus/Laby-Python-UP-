#!/usr/bin/env python
# coding: utf-8

# # Wprowadzenie do programoowania w języku Python

# ## Zadanie 1

# Instalacja środowiska Anaconda
# 
# ### krok 1. Pobranie pakietu instalacyjnego z strony Anacondy
# https://www.anaconda.com/products/individual#Downloads
# 
# ### Krok 2. Instalacja
# 
# ### Krok 3. Utworzenie nowego środowiska 
# `conda create -n programowanie1 python=3.8`
# 
# ### krok 4. Aktywacja środowiska
# `conda activate programowanie1`
# 
# ### krok 5. Uruchomienie Jupyter Notebook
# `jupyter notebook`

# ## Zadanie 2
# Zapoznaj się z dokumentacją opisującą następujące wbudowane funkcje:
# 
# * [help](https://docs.python.org/3/library/functions.html#help)
# * [print](https://docs.python.org/3/library/functions.html#print)
# * [input](https://docs.python.org/3/library/functions.html#input)
# * [len](https://docs.python.org/3/library/functions.html#len)
# * [type](https://docs.python.org/3/library/functions.html#type)
# * [dir](https://docs.python.org/3/library/functions.html#dir)
# 
# I spróbuj je wykorzystać

# In[2]:


help (input)
type (4)


# ## Zadanie 3
# Korzystając z funkcji `help()` dowiedzsię coś na temat:
# 
# * int
# * float
# * str
# * print
# * input
# * len

# In[12]:


help (input)


# ## Zadanie 4
# 
# Utwórz kilka zmiennych różnego typu.

# In[ ]:


zmien_x = 1
zmien_y = 3.14
zmien_z = 'rigcz'


# ## Zadanie 5
# Korzystając z funkcji `type()` sprawdź jakiego typu są to zmienne.

# In[ ]:


zmien_x = 13
zmien_y = 3.14
zmien_z = 'rigcz'
(type (zmien_x)
(type (zmien_y)
(type (zmien_z)


# ## Zadanie 6
# Zastosuj funkcję `print()` do wyświetlenia na ekranie tekstu 'Witaj Świecie!'.

# In[4]:


print('Witaj Świecie!')


# ## Zadanie 7
# 
# Zapoznaj się z dosłownym formatowaniem łańcuchowym [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings).

# In[ ]:


zmien_z = 'rigcz'

print(f'Witaj, czy masz {zmien_z}?')


# ## Zadanie 8
# Zastosuj funkcję `print()` do wyświetlenia na ekranie: zmienna1 = wartosc.

# In[6]:


zmien_x = 13

print(f'Zmienna X = {zmien_x}')


# ## Zadanie 9
# 
# Napisz kod który doda dwie zmienne typu int do siebie i wyświetli wartość na ekranie.

# In[7]:


x = 13
y = 22

print(x + y)

#Ewentualny sposób:
print (13+22)


# ## Zadanie 10
# 
# Napisz kod który wyświetli na ekranie '---------------------------------------' stosując pewną własność łańcuchów znakowych.

# In[8]:


print('-'*39)


# ## Zadanie 11
# 
# Napisz kod który wyświetli na ekranie '-bc--bc--bc--bc--bc-' stosując pewną własność łańcuchów znakowych.

# In[ ]:


print(('-b' + 'c-')*5)


# ## Zadanie 12
# Napisz kod który pobierze od użytkownika jego imię a następnie go powita.

# In[9]:


imie = input('Kim jesteś?: ')
print(f'Witaj {imie}!\nTrzy tysiące dukatów albo spadaj!')


# ## Zadanie 13
# Napisz kod który pobierze od użytkownika liczbę i wyświetli jej typ (`type()`) na ekranie.

# In[28]:


#liczba = input('Podaj liczbę: ')
#print(type(liczba))

#Input zawsze konwertuje na string. Nie wiem jak sprawdzić czy to float, int, double itp. Jeśli podam na przykład
#int(input()), zawsze będzie to integerem.

#Znalazłem za to rozwiązanie na internecie które rozwiązuje problem.

def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print(type (val))
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print(type (val))
        except ValueError:
            print("Input nie jest liczbą, to string.")


input1 = input("Napisz liczbę:")
check_user_input(input1)


# ## Zadanie 14
# Napisz kod podobny do poprzedniego, z tą różnicą, że jeżeli `imie == 'Azor'` to przywitaj go `'Dobry piesek!'`.
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

# In[26]:


imie2 = input('Szukam mojego psa, Azora. Jak Ci na imię?: ')
if imie2 == 'Azor':
  print('Dobry piesek!')
else:
  print(f'Witaj {imie}!')


# ## Zadanie 15
# Napisz prosty kalkulator.
# Pobierz dwie wartości od użytkownika oraz rodzaj operacji (+,-,*,/) a następnie wyświetl na ekranie rozwiązanie.
# 
# przykład:
# ```shell
# Podaj pierwszą liczbę > 1
# Podaj drugą liczbę > 3
# Podaj operację (+,-,*,/) > +
# wynik: 4
# ```

# In[ ]:


first_number = int(input('Podaj pierwszą liczbę (int): '))
second_number = int(input('Podaj drugą liczbę (int): '))
operation = input('Podaj operację (+,-,*,/): ')
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


# ## Zadanie 16
# Zmodyfikuj kalkulator z poprzedniego zadania tak, aby można było podawać liczby zmiennoprzecinkowe (`float`).
# 
# przykład:
# ```shell
# Podaj pierwszą liczbę > 1.5
# Podaj drugą liczbę > 3.5
# Podaj operację (+,-,*,/) > -
# wynik: -2.0
# ```

# In[11]:


first_number = float(input('Podaj pierwszą liczbę (float): '))
second_number = float(input('Podaj drugą liczbę (float): '))
operation = input('Podaj operację (+,-,*,/): ')
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


# In[ ]:





zmienna = 4

type(zmienna)

dir


#help(int)

# Zadanie 4
#Utwórz kilka zmiennych różnego typu.

zmien_x = 1
zmien_y = 3.14
zmien_z = 'rigcz'

#Zadanie 5
#Korzystając z funkcji `type()` sprawdź jakiego typu są to zmienne.

print (type (zmien_x))
print (type (zmien_y))
print (type (zmien_z))

#Zadanie 6
#Zastosuj funkcję `print()` do wyświetlenia na ekranie tekstu 'Witaj Świecie!'.

print('Witaj Świecie!')

#Zadanie 7
#Zapoznaj się z dosłownym formatowaniem łańcuchowym [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings).


print(f'Witaj, czy masz {zmien_z}?')

#Zadanie 8
#Zastosuj funkcję `print()` do wyświetlenia na ekranie: zmienna1 = wartosc.


print(f'Zmienna X = {zmien_x}')

#Zadanie 9
#Napisz kod który doda dwie zmienne typu int do siebie i wyświetli wartość na ekranie.


print(zmien_x + zmien_y)

#Zadanie 10
#Napisz kod który wyświetli na ekranie '---------------------------------------' stosując pewną własność łańcuchów znakowych.


print('-'*30)

#Zadanie 11
#Napisz kod który wyświetli na ekranie '-bc--bc--bc--bc--bc-' stosując pewną własność łańcuchów znakowych.


print(('-b' + 'c-')*5)

#Zadanie 12
#Napisz kod który pobierze od użytkownika jego imię a następnie go powita.


imie = input('Kim jesteś?: ')
print(f'Witaj {imie}!\nTrzy tysiące dukatów albo spadaj!')

#Zadanie 13
#Napisz kod który pobierze od użytkownika liczbę i wyświetli jej typ (`type()`) na ekranie.


liczba = input('Podaj liczbę, sprawdzę jej typ: ')
if type(liczba) == str:
    print('To nie liczba, to słowo lub litera.')
else:
    print(type(liczba))

#Zadanie 14
#Napisz kod podobny do poprzedniego, z tą różnicą, że jeżeli `imie == 'Azor'` to przywitaj go `'Dobry piesek!'`.

imie2 = input('Szukam mojego psa, Azora. Jak Ci na imię?: ')
if imie2 == 'Azor':
  print('Dobry piesek!')
else:
  print(f'Witaj {imie}!')

#Zadanie 15
#Napisz prosty kalkulator.
#Pobierz dwie wartości od użytkownika oraz rodzaj operacji (+,-,*,/) a następnie wyświetl na ekranie rozwiązanie.


first_numb = int(input('Podaj pierwszą liczbę (int): '))
second_numb = int(input('Podaj drugą liczbę (int): '))
operation = input('Podaj operację (+,-,*,/): ')
if operation == '+':
  wynik = first_numb + second_numb
elif operation == '-':
  wynik = first_numb - second_numb
elif operation == '*':
  wynik = first_numb * second_numb
elif operation == '/':
  wynik = first_numb / second_numb
else:
  wynik = 'blad'
print(f'wynik: {wynik}')

#Zadanie 16
#Zmodyfikuj kalkulator z poprzedniego zadania tak, aby można było podawać liczby zmiennoprzecinkowe (`float`).

first_numb = float(input('Podaj pierwszą liczbę (float): '))
second_numb = float(input('Podaj drugą liczbę (float): '))
operation = input('Podaj operację (+,-,*,/): ')
if operation == '+':
  wynik = first_numb + second_numb
elif operation == '-':
  wynik = first_numb - second_numb
elif operation == '*':
  wynik = first_numb * second_numb
elif operation == '/':
  wynik = first_numb / second_numb
else:
  wynik = 'blad'
print(f'wynik: {wynik}')
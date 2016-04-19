def linia(plik):
    l= plik.readline()
    while (l != ""):
        try:
          yield int(l.rstrip('\n\r').split(separator)[kolumna])
        except ValueError:
            yield 0
        l = plik.readline()


separator = ','
nazwa ="./phoneCalls.csv"
kolumna = 3
plik= open(nazwa, 'r')
print(sum(linia(plik, separator, kolumna)))
plik.close()

def kalkulator (a,b, operacja):
    pass

def operacja (x,y):
    return (x + y)

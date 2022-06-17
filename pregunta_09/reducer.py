#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    cont = 0
    for line in sys.stdin:
        lista = line.split('   ')
        sys.stdout.write("{}   {}   {}\n".format(lista[1], lista[2].strip(), int(lista[0])))
        if cont >= 5:
            break
        cont += 1
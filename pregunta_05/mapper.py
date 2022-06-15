#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        #se separan las columnas separadas
        lista = line.split('   ')
        mes = lista[1].split('-')
        #se genera la salida del dato llamando la columna objetivo
        sys.stdout.write("{}\t1\n".format(mes[1]))
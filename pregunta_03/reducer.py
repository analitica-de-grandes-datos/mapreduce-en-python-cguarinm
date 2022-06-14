#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys, operator

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    data = []
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        lineas = line.replace("\n", "")
        lineas = line.split('\t')
        data.append(lineas)

    dataord = sorted(data, key=operator.itemgetter(1), reverse=False)

    for row in dataord:
        sys.stdout.write("{},{}".format(row[0], row[1]))
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        lista = line.split('\t')
        val = line.split('\t')[1]
        val = int(val)

        sys.stdout.write("{}   {}   {}\n".format(
            lista[0], lista[2].strip(), val))
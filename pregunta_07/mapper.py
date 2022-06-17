#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        
        lista = line.split('   ')
        val = line.split('   ')[2].strip()
        val = val.zfill(4)
        
        sys.stdout.write("{}\t{}\t{}\n".format(lista[0], val, lista[1]))
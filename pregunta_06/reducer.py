#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    max_value = 0
    min_value = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
            
            if (val > max_value):
                max_value = val

            if (max_value < val):
                min_value = val

        else:
            
            if curkey is not None:
               
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, max_value, min_value))

            curkey = key
            max_value = val
            min_value = val

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, max_value, min_value))
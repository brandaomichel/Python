import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Numero de argumentos incorretoss')
        sys.exit(1)
    
    numero1 = float(sys.argv[0])
    numero2 = float(sys.argv[1])
    print(numero1 + numero2)
import os.path
import sys


def extract(input_path, output_path):
    input_file = open(input_path, 'r')
    output_file = open(output_path, 'w')

    input_file.readline()  # ignore la première ligne

    for line in input_file:
        line = line.split(",")

        if len(line) > 2:
            line = line[len(line) - 3].split(':')[1]
            print(line)
            output_file.write(line + "\n")

    return 1


def main():
    if len(sys.argv) != 3:
        print("Erreur: pas assez d'arguments")
        exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("Erreur: fichier ", sys.argv[1], "introuvable")  # dataset
        exit(1)

    print("Debut analyse")
    extract(sys.argv[1], sys.argv[2])
    print("fin analyse")


if __name__ == '__main__':
    main()

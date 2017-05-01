import argparse

import sys


def combine(data_path, result_path, output_path, nb_lines):
    data = open(data_path, 'r')
    result = open(result_path, 'r')
    output = open(output_path, 'w')

    while True:
        data_line = data.readline()
        output.write(data_line)
        if data_line.endswith(',?\n'):
            break

    result_line = result.readline()

    toolbar_width = 40
    toolbar_increment = int(nb_lines / 40)

    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))  # return to start of line, after '['

    counter = 0

    while True:
        output_tab = data_line.rsplit(',', 1)
        output_tab[-1] = result_line
        output.write(','.join(output_tab))
        data_line = data.readline()
        result_line = result.readline()

        if (counter + 1) % toolbar_increment == 0:
            sys.stdout.write("-")
            sys.stdout.flush()

        counter = counter + 1
        if result_line == '':
            break

    sys.stdout.write("\n")

    return 1


def main():
    parser = argparse.ArgumentParser(description="Combine le fichier de original en .arff et le fichier de résultat")

    parser.add_argument("data_file", metavar="data-file", type=str,
                        help="Le fichier contenant les commentaires")
    parser.add_argument("result_file", metavar="result-file", type=str,
                        help="Le fichier contenant les resultats")
    parser.add_argument("-o", "--output", metavar="output-file", type=str,
                        help="Le fichier contenant la combinaison des deux fichiers (predictions.arff par defaut)",
                        default="predictions.arff")
    parser.add_argument("-l", "--line-number", dest="line_number", metavar="line-number", type=int,
                        help="Nombre de lignes, utilisé pour la barre de chargement (4000 par defaut)",
                        default=4000)

    args = parser.parse_args()

    combine(args.data_file, args.result_file, args.output, args.line_number)


if __name__ == '__main__':
    main()

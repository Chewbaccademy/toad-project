from csvTools import *
import argparse


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE_NAME', help="nom du fichier source", type=str)
    parser.add_argument('NAME', help="type de données", type=str)
    parser.add_argument('COLUMN_INDEX', help="index de la colonne à prédire", type=int)
    parser.add_argument('-k', help="valeur de K pour le KNN", type=int, default=0)
    parser.add_argument('-o', '--optimize', help="optimiser la recherche", type=str, default="")
    parser.add_argument('-p', '--pondere', help="choisir le vote ponderer", action='store_true', default=False)
    parser.add_argument('-t', '--test', help="fichier à vérifier pour calculer l'efficacité du programme", type=str, default="")
    parsed_args = parser.parse_args()
    return (parsed_args.FILE_NAME, parsed_args.NAME, parsed_args.COLUMN_INDEX, parsed_args.k, parsed_args.optimize, parsed_args.pondere, parsed_args.test)


def afficherStats(filename, dataset, type_donnees, predictions):
    print(f"Chargement du fichier {filename}  contenant de individus de type {type_donnees}")
    nb_donnees = len(dataset.getData())
    nb_attr = dataset.getNbFields()
    print(f"{nb_donnees} individus de type {type_donnees}")
    print(f"{nb_attr} attributs")
    print(f"predictions : {predictions}")

if __name__ == "__main__":

    # TODO : changer le nom de variable de O
    FILE_NAME, NAME, COLUMN_INDEX, K, O, IS_PONDERE, TEST_FILE_NAME  = arg_parse()

    
    if len(O) != 0:
        optimized_indexes = O.split(SEPARATOR)
        optimized_indexes = [int(index) for index in optimized_indexes]
        optimized_indexes.append(COLUMN_INDEX)
        COLUMN_INDEX = len(optimized_indexes) - 1
    else:
        optimized_indexes = []

    dataset = parse_csv_file(FILE_NAME, optimized_indexes)

    if K == 0:
        K = int(input("Saisissez une valeur pour K : "))
    
    if TEST_FILE_NAME != "":
        testdata = parse_csv_file(TEST_FILE_NAME, optimized_indexes)
        for john in testdata:
            afficherStats(TEST_FILE_NAME, dataset, NAME, john.euclideanKNN(dataset, int(COLUMN_INDEX), K, IS_PONDERE))
    else:
        john = input("Saisissez une valeur pour john (q pour quitter) : ")
        while john != "q":
            datum_john = parse_csv_line(john)
            afficherStats(FILE_NAME, dataset, NAME, datum_john.euclideanKNN(dataset, int(COLUMN_INDEX), K, IS_PONDERE))
            john = input("Saisissez une valeur pour john (q pour quitter) : ")


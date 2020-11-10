# imports
import sys
import csv

# récupération et contrôle des arguments du programme
if(len(sys.argv) < 4):
    print("pas assez d'arguments passés pour le programme")
    sys.exit()


file_name = sys.argv[1]
data_type = sys.argv[2]
class_predict = sys.argv[3]

""" print("fichier : " + file_name)
print("type de données : " + data_type)
print("classe à prédire : " + class_predict) """

data_test = []

with open(file_name, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        data_test.append(row)

print(data_test)

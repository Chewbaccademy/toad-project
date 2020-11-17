import math

def parse_csv_line(line: str):
    """
    """
    return line.rstrip().split(',')


class Datum:
    """
    Représente un objet comparé ou comparant, avec différents attributs (par exemple un Datum peut représenter un champignon avec comme attributs la couleur, la taille...)

    fields :
        - attrs : une List des attributs de l'objet
    """
    
    def __init__(self, csv_line):
        self.attrs = parse_csv_line(csv_line)
        pass
        
    def distanceEuclide(self, compared, index_col):
        dist = 0
        for i in range(len(self.attrs) - 1):
            if self.attrs[i] != compared[i if i < index_col else (i + 1)]:
                dist += 0
            else:
                dist += 1
        return dist

    def euclideanKNN(self, dataset, classIndex: int):


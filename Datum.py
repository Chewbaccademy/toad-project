import math

def parse_csv_line(line: str):
    """
    """
    return line.rstrip().split(',')

def maximum(table:list):
    max = table[0]
    for i in table:
        if i > max:
            max = i
    return max


class Datum:
    """
    Représente un objet comparé ou comparant, avec différents attributs (par exemple un Datum peut représenter un champignon avec comme attributs la couleur, la taille...)

    fields :
        - attrs : une List des attributs de l'objet
    """
    
    def __init__(self, csv_line:list):
        self.attrs = csv_line
        pass
        
    def distanceEuclide(self, compared:Datum, index_col:int):
        dist = 0
        for i in range(len(self.attrs) - 1):
            if self.attrs[i] != compared[i if i < index_col else (i + 1)]:
                dist += 0
            else:
                dist += 1
        return dist



    def euclideanKNN(self, dataset, index_col: int, k:int):
        distances = []
        for datum in dataset:
            dist = (self.distanceEuclide(datum, index_col), datum.attrs[index_col])
            if(len(distances) < k):
                distances.append(dist)
            else:
                if(dist[0] < maximum(distances)):
                    distances[distances.index(maximum(distances))] = dist
        
        pass



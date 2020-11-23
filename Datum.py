import math

def maximum(table:list, index_tri:int):
    """
    renvoie l'indice duplus grand élément d'une liste de tuple

    @param {list} table : la liste dont on veut le maximum
    @param {int} index_tri : l'index des tuples que l'on considère pour le tri

    @return {int} l'indice du plus grand élément de table
    """
    max = table[0]
    for i in table:
        if i[index_tri] > max:
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
        """
        Calcule la distance euclidienne entre deux datum

        @param {Datum} compared le Datum que l'on compare à self  
        @param {int} index_col l'index de la colonne à rechercher et à ne pas prendre en compte

        @return retourne la distance entre les deux Datum
        """
        dist = 0
        for i in range(len(self.attrs) - 1):
            if self.attrs[i] != compared[i if i < index_col else (i + 1)]:
                dist += 0
            else:
                dist += 1
        return dist



    def euclideanKNN(self, dataset, index_col: int, k:int):
        """
        Renvoie la valeur du champ recherché

        @param {Dataset} dataset : le dataset de base qui sert de comparatif
        @param {int} index_col : l'index de la colonne à rechercher et à ne pas prendre en compte  
        @param {int} k : le nombre d'élément du dataset à prendre en compte pour la recherche de la valeur


        @return retourne la valeur du champ recherché
        """
        # calcul des k éléments les plus proches
        distances = []
        for datum in dataset:
            dist = (self.distanceEuclide(datum, index_col), datum.attrs[index_col])
            if(len(distances) < k):
                distances.append(dist)
            else:
                if(dist[0] < maximum(distances, 0)):
                    distances[distances.index(maximum(distances, 0))] = dist
        
        # retour de la valeur de la colonne recherchée en fonction des k éléments les plus proches

        #* comptage des valeurs si la distance compte

        # occurences = []
        # for elem in distances:
        #     value = elem[1]
        #     ponderation = 1 / elem[0]
        #     presence = False
        #     for i in range(len(occurences)):
        #         occurence = occurences[i]
        #         if value == occurence[1]:
        #             occurences[i] = (occurence[0] + ponderation, occurence[1])
        #             presence = True
        #     if not presence:
        #         occurences.append(ponderation, value)

        # comptage des valeurs si la distance ne compte pas

        occurences = []
        for element in distances:
            occurences.append(element[1])
        maxi = 0
        value = []
        for element in distances:
            if occurences.count(element[1]) > maxi:
                value = [element[1]]
                maxi = occurences.count(element[1])
            elif occurences.count(element[1]) == maxi:
                value.append(element[1])

        if len(value) == 1:
            return value[0]
        elif len(value) > 1:
            return value
        else:
            return None
        pass



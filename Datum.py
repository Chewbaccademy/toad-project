import math

def maximum(table):
    """
    renvoie l'indice du plus grand élément d'une liste de tuple

    @param {list} table : la liste dont on veut le maximum

    @return {int} l'indice du plus grand élément de table
    """
    max = table[0][0]
    for element in table:
        if element[0] > max:
            max = element[0]
    return max

    # [(1,2), (5,6), (1,5)]

def indexTuple(table, sub_element):
    """
    
    """
    for i in range(len(table)):
        element = table[i]
        if element[0] == sub_element:
            return i
    return -1

class Datum:
    """
    Représente un objet comparé ou comparant, avec différents attributs (par exemple un Datum peut représenter un champignon avec comme attributs la couleur, la taille...)

    fields :
        - attrs : une List des attributs de l'objet
    """
    
    def __init__(self, csv_line):
        self.attrs = csv_line
        pass
        

    def distanceEuclide(self, compared, index_col, dataset):
        """n
        Calcule la distance euclidienne entre deux datum

        @param {Datum} compared le Datum que l'on compare à self  
        @param {int} index_col l'index de la colonne à rechercher et à ne pas prendre en compte

        @return retourne la distance entre les deux Datum
        """
        dist = 0
        limits = dataset.getLimits()

        # Pour chaque attribut
        for i in range(len(self.attrs) - 1):

            # Si c'est un nombre pon calcule la distance euclidienne
            if limits[i] != None:
                dist += math.sqrt(self.attrs[i] - (compared.attrs[i if i < index_col else (i + 1)] / (limits[i][2] - limits[i[1]])) ** 2)
            
            # Si c'est une chaine de caractère on renvoie 0 ou 1
            if self.attrs[i] != compared.attrs[i if i < index_col else (i + 1)]:
                dist += 1
            else:
                dist += 0
        return dist



    def euclideanKNN(self, dataset, index_col, k, pondere):
        """
        Renvoie la liste des occurences des possibilités de la classe à prédire

        @param {Dataset} dataset : le dataset de base qui sert de comparatif
        @param {int} index_col : l'index de la colonne à rechercher et à ne pas prendre en compte  
        @param {int} k : le nombre d'élément du dataset à prendre en compte pour la recherche de la valeur


        @return retourne la liste des occurences des possibilités de la classe à prédire
        """
        # List de tuple sous la forme (<nombre d'iteration>, <etat>)
        distances = []
        
        # pour chaque datum
        for datum in dataset: 
            dist = (
                self.distanceEuclide(datum, index_col, dataset), 
                datum.attrs[index_col]
            )
            
            # si la liste ne contient pas encore les k plus proches éléments
            if(len(distances) < k):
                distances.append(dist)

            else:
                max = maximum(distances)
                
                # si le datum fait parti des k plus proches 
                if dist[0] < max:
                    distances[indexTuple(distances, max)] = dist
        
        # retour de la valeur de la colonne recherchée en fonction des k éléments les plus proches

        
        # dictionnaire des valeurs de pondération pour chaque possibilité de la classe à prédire
        # les valeurs de pondération sont égales aux occurences des possibilités lors d'un vote majoritaire
        ponderation = {}

        if pondere :
            # on parcours les k éléments les plus proches
            for elem in distances:

                # si l'élément est déjà présent, on incrémente sa pondération
                if elem[1] in ponderation:
                    if elem[0] != 0:
                        ponderation[elem[1]] += 1 / elem[0]

                # sinon on indique qu'il est présent pour la première fois
                else:
                    if elem[0] != 0:
                        ponderation[elem[1]] = 1 / elem[0]
                    else:
                        ponderation[elem[1]] = 0



        else :
            # on parcours les k éléments les plus proches
            for elem in distances:

                # si l'élément est déjà présent, on incrémente son occurence
                if elem[1] in ponderation:
                    ponderation[elem[1]] += 1

                # sinon on indique qu'il est présent pour la première fois
                else:
                    ponderation[elem[1]] = 1

        # on retourne la liste des occurences
        return ponderation

    def __getitem__(self, item):
        """
        Get the attribute at current index
        @param {int} item index of the data to return
        """
        return self.attrs[item]




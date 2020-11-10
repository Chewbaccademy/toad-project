Projet Toad par Bro Kiki et Bro Thony
=====================================

## données

### Input
- nom du fichier csv source
- type de données
- index de la colonne avec la classe à prédir
- valeur de K (K-NN)
- john

### Output
- prédiction de john

## scenario

1. parsing du fichier
2. calcul de la distance enter john et les éléments du fichier
3. détermination des K cas les plus proches de john
4. demander s'il y a d'autres johns à rentrer  
   4a. si oui, on retourne à l'étape 2
   4b. Si non, on passe à l'étape 5
5. retourner la valeur de la classe à prédir des johns

## varialbes globales
SEPARATOR
READ_MODE

## fonctions
parseCsvLine(csvLine:str):Dataset
parseCsvFile(filename:str)
euclideanKNN(dataSet:List[Datum], classIndex:int)

## classes

### Datum
constructor(csvLine:str)
euclideanDistance(compared:Datum, classIndex:int)
euclideanKNN(dataSet:List[Datum], classIndex:int)

### Dataset

data:List[Datum]
fields:List[str]
nbFields:int

constructor(fields:List[str], data:List[Datum])



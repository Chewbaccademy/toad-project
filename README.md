Projet Toad par Bro Kiki et Bro Thony
=====================================

## vocabulaire

**john** : l'objet dont on veut determiner une classe inconnue

## données

### Input

### en commande (facultaatif en italique)
- nom du fichier csv source (ex: ../data/tp_mushrooms_dataset_150.csv)
- type de données (ex: champignons)
- index de la colonne avec la classe à prédir (ex: 22)
- *valeur de K (K-NN)* (ex: -k 3)
- *indice des champs les plus utiles* (ex: -o 5,7,13)
- *vote pondere* (ex: -o)
- *fichier pour tester* (ex: -t ../data/tp_mushrooms_dataset_150.csv)

### en input
- k (si pas entrer en commande) (ex: 3)
- john (ex: g,f,g,h,i,i,p,e,g,h,g)

### Output
- prédiction de john

## scenario

1. si k non formis, demande du k
2. parsing du fichier
3. calcul de la distance entre john et les éléments du fichier
4. détermination des K cas les plus proches de john
5. retourner la valeur de la classe à prédire des johns
6. demander s'il y a d'autres johns à rentrer  
   6a. si oui, on retourne à l'étape 3
   6b. Si non, on termine

## constantes de configuration
SEPARATOR  
READ_MODE

## fonctions
parseCsvLine(csvLine:str):list  
parseCsvFile(filename:str):Dataset  
euclideanKNN(dataSet:list[Datum], index_col:int)  

## classes

### Datum
constructor(csvLine:list)  
euclideanDistance(compared:Datum, index_col:int)  
euclideanKNN(dataSet:list[Datum], index_col:int)  

### Dataset

data:list[Datum]  
fields:list[str]  
nbFields:int  

constructor(fields:list[str], data:list[Datum])  



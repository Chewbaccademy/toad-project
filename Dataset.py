
class Dataset:
    def __init__(self, fields, data):
        """
        Constructor for Dataset  
        @param {list[string]} fields name
        @param {list[Datum]} data
        """
        self._fields = fields
        self._data = data
        self._nbfields = len(fields)
        self._index = 0
        self._nbitem = len(data)

        # Setup types list
        self._types = []
        for a in self._data[0].attrs:
            self._types.append(float if a.isdigit() else str)
        # Calcul the limits of the interger in the dataset
        self.min_max = self.calculLimits()

    def getTypes(self):
        return self._types
    
    def getData(self):
        return self._data
    
    def getNbFields(self):
        return self._nbfields

    def calculLimits(self):
        """
        Return a list of tuple. The list is composed with as many tuple as there is fields. 
        If a field is a typed as string, its value is None, else it will be represented as a (min, max) tuple
        min is the shortest value and max is the biggest.
        """
        res = []
        for t in range(self._nbfields):
            if self._types[t] == str:
                res.append(None)
            else:
                max = float("-Inf") 
                min = float("Inf") 
                for datum in self._data:
                    if datum[t] != None:
                        value = float(datum[t])
                        if value < min : 
                            min = value
                        if value > max :
                            max = value
                res.append((min, max))
        
        return res
    
    def getLimits(self):
        return self.min_max
            
            
    def __getitem__(self, item):
        """
        Get the data at current index
        @item {int} item index of the data to return
        """
        return self._data[item]

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < self._nbitem:
            r = self._data[self._index]
            self._index += 1
            return r

        else:
            raise StopIteration
            

    

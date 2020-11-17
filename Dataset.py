
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
            
            

    

import json

from source.layer import Layers


class Map :

    def __init__(self, filename:str) -> None : 
        
        with open(filename, 'r', encoding='utf8') as f_map : 
            self.raw = json.load(f_map)

        for key, value in dict(self.raw).items() :
            self.__setattr__(key, value)
        
        self.layers = Layers(self).layers_list

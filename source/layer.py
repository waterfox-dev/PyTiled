
class Layers :

    def __init__(self, parent) :

        self.layers_list = []

        for element in parent.raw["layers"] : 
            element = dict(element)
            dic = {}
            for key, value in element.items() :
                dic[key] = value
            self.layers_list.append(dic)

            
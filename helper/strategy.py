''' @author: klimyflorez '''
import numpy as np

class GetHorizontal:
    def __init__(self, series):        
        self.series = series #se obtiene la matriz del array numpy
        self.isMutant = False
        self.isEnd = False
        self.mutantScore = 0
        self.humanScore = 0
        self.get()

    ''' Función para validar si la letra existe 4 veces seguido en la fila '''
    def validate(self, serie: list, letter_to_validate: str):
        aux = 0
        for letter in serie:            
            if aux >= 4:
                return True
            else:
                if letter == letter_to_validate:
                    aux += 1
                elif letter is not letter_to_validate and aux == 0:                    
                    pass #no se realiza ninguna acción, se sigue ejecutando el for
                else:
                    return False

    def get(self):
        #se enumera la matriz del array numpy
        for i, item in enumerate(self.series):
            # unique: se almacena las letras unicas por cada fila del array
            # counts: se almacena el número de letra por cada fila en el array
            unique, counts = np.unique(item, return_counts=True)            
            # zip: agrupa los elementos iterables              
            for letter, count in zip(unique, counts):                
                if count >= 4:
                    result = self.validate(item, letter)
                    if result:
                        self.mutantScore += 1
                    else:
                        self.humanScore += 1
                else:
                    self.humanScore += 1

class GetVertical:
    def __init__(self, series):
        ''' self.series: se recorre la matriz del array numpy agrupados en elementos iterables, 
            se convierte a una lista y luego se crea el array numpy con el fin de convertir 
            las lineas verticales a líneas horizontales  '''
        self.series = np.array([list(tup) for tup in zip(*series)])
        self.isMutant = False
        self.isEnd = False
        self.mutantScore = 0
        self.humanScore = 0
        self.get()

    def validate(self, serie: list, letter_to_validate: str):
        aux = 0
        for letter in serie:
            if aux >= 4:
                return True
            else:
                if letter == letter_to_validate:
                    aux += 1
                    if aux >= 4:
                        return True
                elif letter != letter_to_validate and aux == 0:
                    pass
                else:
                    return False

    def get(self):
        # print(self.series)
        for i, item in enumerate(self.series):
            unique, counts = np.unique(item, return_counts=True)
            for letter, count in zip(unique, counts):
                if count >= 4:
                    result = self.validate(item, letter)
                    if result:
                        self.mutantScore += 1
                    else:
                        self.humanScore += 1
                else:
                    self.humanScore += 1


class GetDiagonal:
    def __init__(self, series):
        self.series = series #se obtiene la matriz del array numpy
        self.isMutant = True
        self.isEnd = True
        self.mutantScore = 0
        self.humanScore = 0
        self.get()

    def validate(self, serie: list, letter_to_validate: str):
        aux = 0
        for letter in serie:
            if aux >= 4:
                return True
            else:
                if letter == letter_to_validate:
                    aux += 1
                elif letter is not letter_to_validate and aux == 0:
                    pass
                else:
                    return False
    
    def getResult(self, item):
        unique, counts = np.unique(item, return_counts=True)
        for letter, count in zip(unique, counts):
            if count >= 4:
                result = self.validate(item, letter)
                if result:
                    self.mutantScore += 1
                else:
                    self.humanScore += 1


    def get(self):
        #se obtiene el número de columnas        
        columns = list(range(0, len(self.series[0])))        
        for column in columns:
            itemsPlus = self.series.diagonal(column)
            itemMinus = self.series.diagonal(-column)

            if column:
                if len(itemsPlus) >= 4:
                    self.getResult(itemsPlus)
                    self.humanScore += 1
                if len(itemMinus) >= 4:
                    self.getResult(itemMinus)
            else:
                if len(itemsPlus) >= 4:
                    self.getResult(itemsPlus)

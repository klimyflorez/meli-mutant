import numpy as np
from helper.strategy import GetHorizontal, GetVertical, GetDiagonal

class IsMutant:
    def __init__(self, data: dict) -> None:
        self.data = data
        self.options = ['horizontal', 'vertical', 'diagonal']
        self.letters = ['A','T','C','G']
        self.score = {}
        self.isMutant = False
        self.count_mutant_dna = 0
        self.count_human_dna = 0
        self.size = 0
        self.error = {}
        self.isEnd = False
        self.get = self.getSeries()

    def verify(self):
        for item in self.data:
            for letter in list(item):
                if letter not in self.letters:
                    self.isEnd = True
                    self.error = {
                        'error': True,
                        'message': f"Unknown letter: ({letter}) "
                    }
            

    def getSeries(self) -> object:
        verify = self.verify()
        parsed = [list(i) for i in self.data]
        series = np.array(parsed)
        res = self.getCoincidencia(series)
        return res

    def getCoincidencia(self, series) -> dict:
        self.size = series.size
        index = 0
        countMutantAux = 0
        while self.isEnd == False:
            if not self.isMutant and not self.isEnd:
                result = self.validateIsMutant(self.options[index],series)
                self.score[self.options[index]] = {
                    'mutant_dna': result.mutantScore,
                    'human_dna': result.humanScore,
                }
                self.count_mutant_dna += result.mutantScore * 4
                self.count_human_dna += result.humanScore
                if result.mutantScore:
                    countMutantAux += result.mutantScore
                if result.isEnd == True:
                    self.isEnd = True
                    break
                index += 1
        if countMutantAux > 1:
            self.isMutant = True

        return series

    def validateIsMutant(self, option, series):
        options = {
            'horizontal': GetHorizontal,
            'vertical': GetVertical,
            'diagonal': GetDiagonal,
        } 
        
        return options[option](series)


    
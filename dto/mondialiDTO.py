class NotHomeWinner:
    def __init__(self, nazione):
        self._nazione=nazione
        
    @property
    def nazione(self):
        return self._nazione
    
    @nazione.setter
    def nazione(self, nazione):
        self._nazione=nazione
        
    def __str__(self):
        return f"{self.nazione}"

class AllHugeNationbyWC:
    def __init__(self, anno, nazione,numero_convocazioni):
        self._anno=anno
        self._nazione=nazione
        self._numero_convocazioni=numero_convocazioni
    
    @property
    def anno(self):
        return self._anno
    
    @anno.setter
    def anno(self, anno):
        self._anno=anno
        
    @property
    def nazione(self):
        return self._nazione
    
    @nazione.setter
    def nazione(self, nazione):
        self._nazione=nazione  
        
    @property
    def numero_convocazioni(self):
        return self._numero_convocazioni
    
    @numero_convocazioni.setter
    def numero_convocazioni(self, numero_convocazioni):
        self._numero_convocazioni=numero_convocazioni 
        
    def __str__(self):
        return f"{self.anno} {self.nazione} {self.numero_convocazioni}"
    
class PlayersWithThreeWCOrTwoNation:
    def __init__(self, nome):
        self._nome=nome
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome=nome
            
    def __str__(self):
        return f"{self.nome}"
class Token: 
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self,classe,lexema,tipo):
        self.classe = classe
        self.lexema = lexema
        self.tipo = tipo
    
    def getToken():
        return self
    
    def getClasse(self):
        return self.classe
    
    def getLexema(self):
        return self.lexema
    
    def getTipo(self):
        return self.tipo
       
    def setClasse(self, classe):
        self.classe = classe
    
    def setLexema(self, lexema):
        self.lexema = lexema
    
    def setTipo(self, tipo):
        self.tipo = tipo
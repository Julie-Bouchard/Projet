class StatistiqueDescriptives:
    #self represente un vecteur
    def __init__(self):
        self.moyenne=0
        self.variance=0
        self.ecart_type=0
        self.covariance=0
        
    def moyenne(self):    
        n= len(self)
        for i in range (0,n):
            self.moyenne+=self[i,0]
        self.moyenne=self.moyenne / n
        
    def variance(self):
        n=len(self)
        for i in range (0,n):
            self.variance+=((self[i][0]-self.moyenne)**2)
        self.variance=self.variance / n
        
    def ecart_type(self):
        n=len(self)
        self.ecart_type=(self.variance)**(1/2)
    
    def covariance(self, V):
        n=len(self)
        for i in range (0, n):
            self.covariance+=((self[i][0]-self.moyenne)*(V[i][0]-V.moyenne))
        self.covariance = self.covariance / n

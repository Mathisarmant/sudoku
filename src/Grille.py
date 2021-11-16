class grille :
    
    def __init__(self, long, larg):
        self.longueur=long
        self.largeur=larg
        
    def perimetre (self):
        return 2*(self.longueur + self.largeur)
    
    def aire(self):
        return self.longueur * self.largeur
    


    def rectanglePA(p,a):
        from math import sqrt
        
        L=(p+sqrt(p**2-16*a))/4
        l=(p-sqrt(p**2-16*a))/4
        
        return Rectangle(L,l)
    
    def __repr__(self):
        return f"Rectangle({self.longueur},{self.largeur})"
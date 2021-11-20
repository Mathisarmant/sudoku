from case import Case
from stack import Stack

class Grid:
    
    def __init__(self, puzzle = 81*'.'):
        """
            Constructeur par défaut
            Arguments :
                - puzzle : chaine de 81 caractères
            Tests :
            >>> Grid().puzzle == 81*'.', Grid(81*'2').puzzle == 81*'2'
            (True, True)
            >>> Grid().full, Grid(81*'2').full
            (False, True)
        """
        self.puzzle = puzzle
        self.full = self.puzzle.count('.') == 0
        self.initCases()
        self.puzzleNow = self.casesToString()
        self.stack = Stack()
        
    def loadFromFile(num):
        """
            Charger un puzzle dans le fichier grids.sud
            Argument :
                - num : numéro du puzzle à charger
            Tests :
            >>> Grid.loadFromFile(0).puzzle[:10]
            '4.....8.5.'
        """
        f = open("../data/grids.sud", 'r')
        buff = f.readlines()
        f.close()
        return Grid(buff[num][:-1])
    
    def initCases(self):
        """
            Initialise une liste de 81 cases avec leur valeur suivant le puzzle
            Cette méthode est à appelée lors de l'instanciation de l'objet
            Tests:
            >>> S = Grid()
            >>> S.cases[0].value == None
            True
            >>> S = Grid.loadFromFile(0)
            >>> S.cases[0].value == 4
            True
            >>> S.cases[13].region == 2
            True
        """
        self.cases = []
        for i in range(81):
            if self.puzzle[i] == '.':
                self.cases.append(Case(i))
            else:
                self.cases.append(Case(i, int(self.puzzle[i])))
                
    def casesToString(self):
        """
            Retourne une chaine de caractère représentant le Sudoku
            Permet de faire la comparaison entre l'état initial du puzzle
            et l'état après ajout de valeurs
            
            Cette méthode est appelée lors de l'instanciation de l'objet. Elle crée alors
            un attribut puzzleNow. Elle est également appelée lors d'un changement d'une
            valeur de case.
        
            Tests :
            >>> S = Grid()
            >>> S.puzzleNow == 81*'.'
            True
            >>> S = Grid.loadFromFile(0)
            >>> S.cases[0].value = 5
            >>> S.casesToString()[0] == '5'
            True
        """
        S = ''
        for c in self.cases:
            S += str(c.value) if c.value != None else '.'
        return S
                
    def setValue(self, position, value):
        """
            Méthode permettant de modifier la valeur d'une case à une position donnée.
            Cette méthode doit mettre à jour l'attribut puzzleNow.
            Attention, on ne doit pas pouvoir modifier une valeur qui a été placée initialement.
            
            Tests :
            >>> S = Grid()
            >>> S.setValue(0, 8)
            >>> S.puzzleNow[0] == '8'
            True
            >>> S = Grid.loadFromFile(0)
            >>> S.setValue(0, 7)
            >>> S.puzzleNow[0] == '7'
            False
        """
        if self.puzzle[position] == '.':
            self.stack.push((position, self.cases[position].value, value))
            self.cases[position].setValue(value)
            self.puzzleNow = self.casesToString()
            
            self.cases[position].valid = True # Changement de valeur, on réinitialise sa validité
            self.verif(position)
        
    def undo(self):
        """
            Méthode permettant d'annuler les coups
            Dépile l'élément de la pile historique et fait le coup inverse
            
            Tests :
            >>> S = Grid()
            >>> S.setValue(0, 5)
            >>> S.stack.stack == [(0, None, 5)]
            True
            >>> S.setValue(0, 8)
            >>> S.stack.stack == [(0, None, 5), (0, 5, 8)]
            True
        """
        if not self.stack.empty():
            old = self.stack.pop() # position, oldValue, newValue
            self.setValue(old[0], old[1])
            self.stack.pop()
            
    def verifLine(self, position):
        """
            position est la position de la case qui vient d'être modifiée
            On teste toutes les cases de la ligne.
            
            Tests :
            >>> S = Grid.loadFromFile(0)
            >>> S.setValue(1, 4)
            >>> S.cases[1].valid
            False
            >>> S.setValue(1, 7)
            >>> S.cases[1].valid
            True
        """
        case = self.cases[position]
        
        listCases = [c for c in self.cases if c.line == case.line and c != case]
        
        for c in listCases:
            case.valid = case.valid and (c.value != case.value)
            
    def verifRow(self, position):
        """
            position est la position de la case qui vient d'être modifiée
            On teste toutes les cases de la ligne.
            
            Tests :
            >>> S = Grid.loadFromFile(0)
            >>> S.setValue(9, 4)
            >>> S.cases[9].valid
            False
            >>> S.setValue(9, 7)
            >>> S.cases[9].valid
            True
        """
        case = self.cases[position]
        
        listCases = [c for c in self.cases if c.row == case.row and c != case]
        
        for c in listCases:
            case.valid = case.valid and (c.value != case.value)
            
    def verifRegion(self, position):
        """
            position est la position de la case qui vient d'être modifiée
            On teste toutes les cases de la ligne.
            
            Tests :
            >>> S = Grid.loadFromFile(0)
            >>> S.setValue(20, 3)
            >>> S.cases[20].valid
            False
            >>> S.setValue(20, 1)
            >>> S.cases[20].valid
            True
        """
        case = self.cases[position]
        
        listCases = [c for c in self.cases if c.row == case.region and c != case]
        
        for c in listCases:
            case.valid = case.valid and (c.value != case.value)
            
    def verif(self, position):
        self.verifLine(position)
        self.verifRow(position)
        self.verifRegion(position)
        
    def checkWin(self):
        """
            Vérifie si une grille est gagnante ou pas.
            Une grille est gagnante si elle est remplie et que toutes les cases
            sont valides
        """
        pass
                    
    def __repr__(self):
        """
            Méthode de représentation d'un Sudoku
        """
        S = ''
        for i in range(81):
            if (i+1)%9==0:
                S += f'|{self.puzzleNow[i]}|\n'
            else:
                S += f'|{self.puzzleNow[i]}'
        return S

if __name__ == '__main__':
    import doctest
    doctest.testmod()
        
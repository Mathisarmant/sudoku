class Stack:
    
    def __init__(self):
        """
            Initialisation de la pile
            
            Tests :
            >>> p = Stack()
            >>> p.stack == []
            True
            >>> p.top == None
            True
        """
        pass
        
    def push(self, el):
        """
            Ajouter un élément à la pile
            
            Tests :
            >>> p = Stack()
            >>> p.push(13)
            >>> p.push((12, 1, 9))
            >>> p.stack == [13, (12, 1, 9)]
            True
            >>> p.top == 13
            False
            >>> p.top == (12, 1, 9)
            True
        """
        pass
    
    def empty(self):
        """
            Vérifie si la pile est vide
            
            Tests :
            >>> p = Stack()
            >>> p.empty()
            True
            >>> p.push(12)
            >>> p.empty()
            False
        """
        pass
        
    def pop(self):
        """
            Retirer et renvoyer si possible l'élément en tête de pile
            
            Tests :
            >>> p = Stack()
            >>> p.pop()
            >>> p.push(13)
            >>> p.pop()
            13
            >>> p.push(13)
            >>> p.push((1, 2, 3))
            >>> p.push("NSI")
            >>> p.top == "NSI"
            True
            >>> p.pop()
            'NSI'
            >>> p.top == (1, 2, 3)
            True
            >>> p.pop()
            (1, 2, 3)
            >>> p.pop()
            13
        """
        pass
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()

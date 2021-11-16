class Case:
    
    def __init__(self, pos, value = None):
        """
            Constructeur par défaut
            Arguments :
                - pos   : position de la case (0--80)
                - value : valeur de la case (1--9)
            Tests :
            >>> Case(0).position, Case(80).position, Case(25).position
            (0, 80, 25)
            >>> Case(13).value, Case(13, 3).value
            (None, 3)
            >>> Case(0).row, Case(80).row, Case(25).row
            (0, 8, 7)
            >>> Case(0).line, Case(80).line, Case(25).line
            (0, 8, 2)
            >>> Case(0).region, Case(80).region, Case(25).region
            (1, 9, 3)
        """
        pass
    
    def setValue(self, value):
        """
            Mutateur de l'attribut value
            
            Tests :
            >>> c = Case(13, 2)
            >>> c.setValue(8)
            >>> c.value == 2
            False
            >>> c.value == 8
            True
        """
        pass
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
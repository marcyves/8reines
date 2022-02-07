class Echiquier:
    def __init__(self, n):
        self.tab = list(range(1,n**2+1))
        self.queenCount = 0
        self.lines = list(range(1,9))
        self.columns = list(range(1,9))

    def get(self, x, y):
        return self.tab[y-1 + (x-1)*8]

    def isValid(self, x, y):
        return isinstance(self.get(x, y), int)

    def set(self, x, y, label):
        if self.isValid(x, y):
            self.setLabelByValue(y-1 + (x-1)*8, label)
            return True
        else:
            return False

    def setLabelByValue(self, value, label):
        self.tab[int(value)] = label
    
    def setQueen(self, x, y):
        if self.set(x, y , "D"):
            self.queenCount += 1
            print(x, self.lines)
            self.lines.remove(x)
            self.columns.remove(y)
            return True
        else:
            return False

    def playQueen(self, value):
        value = int(value) - 1
        x = value//8 + 1
        y = value - (x-1)*8 +1

        if self.setQueen(x, y):            
            print('Vous avez joué en {},{}'.format(x,y))
            # Lock line x
            for j in range(1, 9):
                self.set(x, j, '.')
            # Lock column y
            for i in range(1, 9):
                self.set(i, y, '.')
            # Lock diags : / up
            i = x
            j = y
            while(i<8 and j<8):
                i += 1
                j += 1
                self.set(i, j, '.')
            # Lock diags : \ up
            i = x
            j = y
            while(i>1 and j>1):
                i -= 1
                j -= 1
                self.set(i, j, '.')
            # Lock diags : / up
            i = x
            j = y
            while(i<8 and j>1):
                i += 1
                j -= 1
                self.set(i, j, '.')
            # Lock diags : / down
            i = x
            j = y
            while(i>0 and j<8):
                i -= 1
                j += 1
                self.set(i, j, '.')
        else:
            print("Coup invalide")
    
    def scanLines(self):
        linesToPlay = 0
        count = 0
        for i in self.lines:
            for j in range(1,9):
                if self.isValid(i, j):
                    count += 1
                    linesToPlay = j + (i-1)*8
            if count == 1:
                print("Il faut jouer {} dans la ligne {}".format(linesToPlay,i))
                return linesToPlay
            elif count == 0:
                print("La ligne {} est perdue, impossible d'atteindre le but des 8 Reines sur l'échiquier".format(i))
                self.lines.remove(i)
            count = 0
        return 0

    def scanColumns(self):
        columnToPlay = 0
        count = 0
        for j in self.columns:
            for i in range(1,9):
                if self.isValid(i, j):
                    count += 1
                    columnToPlay =  j + (i-1)*8
            if count == 1:
                print("Il faut jouer {} dans la colonne {}".format(columnToPlay, j))
                return columnToPlay
            elif count == 0:
                print("La colonne {} est perdue".format(j))
                self.columns.remove(j)
            count = 0
        return 0

    def solve(self):

        linesToPlay = self.scanLines()
        columnsToPlay = self.scanColumns()
        
        if len(self.lines) == 0 or len(self.columns) == 0:
            return 0
        
        if linesToPlay != 0:
            return linesToPlay

        if columnsToPlay != 0:
            return columnsToPlay

        return -1

    def __str__(self):
        print('Q: {} |  1  2  3  4  5  6  7  8'.format(self.queenCount))
        print('     +------------------------')
        tab = ""
        for i in range(1, 9):
            tab += '  {0:2d}'.format(i) + ' | '
            for j in range(1, 9):
                value = self.get(i,j)
                if isinstance(value, int):
                    tab += '{0:2d}'.format(self.get(i,j)) + ' '
                else:
                    tab += ' '+value+' '
            tab += "\n"
        return tab

print("\nLe problème des 8 dames\n")

t = Echiquier(8)

print(t)

coup = 1
while coup !=0:
    coup = t.solve()
    print("Coup suggéré {}".format(coup))
    if coup == -1:
        coup = int(input("Où est-ce que vous jouez ? (0 pour terminer) ==> "))
    else:
        print("Je joue en {}".format(coup))
    if coup != 0:
        t.playQueen(coup)
        print("lines {}".format(t.lines))
        print("columns {}".format(t.columns))
    print(t)    
print("\nC'est terminé avec {} reines placées".format(t.queenCount))


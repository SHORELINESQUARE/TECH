class Point():
    def num(self, x, y):
        self.X = x
        self.Y = y
    def setx(self,x):
        self.X = x
    def sety(self,y):
        self.Y = y
    def get(self):
        print("(%d,%d)"%(self.X,self.Y))
    def move(self, dx, dy):
        self.X = self.X + dx
        self.Y = self.Y + dy
        print("%d %d"%(self.X,self.Y))
    

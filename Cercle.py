class Cercle:
    
    def __init__(self,x,y):
        self.x = 200 + x*200 + 100
        self.y = y*200+100
        
    def draw(self):
        circle(self.x,self.y,180)

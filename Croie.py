class Croie:
    
    
    def __init__(self,x,y):
        self.x = 200 + x*200 + 100
        self.y = y*200+100
    
    def draw(self):
        line((self.x-90),(self.y-90),(self.x+90),(self.y+90))
        line((self.x-90),(self.y+90),(self.x+90),(self.y-90))

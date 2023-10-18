from Croie import Croie
from Cercle import Cercle
import time
Tab = [[None,None,None],[None,None,None],[None,None,None]]
flipflop = False
playerXScore = 0
playerOScore = 0

def ui():
    background(198,188,188)
    line(200,200,800,200)
    line(200,400,800,400)
    line(400,0,400,600)
    line(600,0,600,600)
    textSize(20)
    text(("Score du joueur X = " + str(playerXScore)), 10, 200)
    text(("Score du joueur O = " + str(playerOScore)), 10, 400)
    textSize(25)
    if flipflop:
        text("Tour du joueur X", 10, 300)
    else:
        text("Tour du joueur O", 10, 300)
    for i in range(3):
        for j in range(3):
            if Tab[i][j] != None:
                Tab[i][j].draw()
                
def debug(x,y):
    global flipflop
    if flipflop:
        Tab[x][y] = Croie(i,j)
        flipflop = False
    else:
        Tab[i][j] = Cercle(i,j)
        flipflop = True
    
        
def mouseClicked():
    delay(500)
    for i in range(3):
        for j in range(3):
            if Tab[i][j] is None:
                if mouseX > 200 + i*200 and mouseX < 400 + i*200 and mouseY > j*200 and mouseY < 200 + j*200:
                    print(str(flipflop))
                    debug(i,j)

def setup():
    size(800,600)
    flipflop = False
    print(str(flipflop))
    
def draw():
    ui()
    

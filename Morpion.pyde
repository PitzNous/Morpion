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
        Tab[x][y] = Croie(x,y)
        flipflop = False
    else:
        Tab[x][y] = Cercle(x,y)
        flipflop = True
        
def reset():
    global Tab
    Tab = [[None,None,None],[None,None,None],[None,None,None]]

        
def check_winner():
    global playerXScore,playerOScore
    for row in Tab:
        if all(cell == Tab[0][0] and isinstance(cell, Croie) for cell in row):
            playerXScore = playerXScore + 1
            reset()
        if all(cell == Tab[0][0] and isinstance(cell, Cercle) for cell in row):
            playerOScore = playerOScore + 1
            reset()

    for col in range(3):
        if all(Tab[row][col] == Tab[0][0] and isinstance(Tab[row][col], Croie) for row in range(3)):
            playerXScore = playerXScore + 1
            reset()
        if all(Tab[row][col] == Tab[0][0] and isinstance(Tab[row][col], Cercle) for row in range(3)):
            playerOScore = playerOScore + 1
            reset()

    if all(Tab[i][i] == Tab[0][0] and isinstance(Tab[i][i], Croie) for i in range(3)) or all(Tab[i][2 - i] == Tab[0][0] and isinstance(Tab[i][2 - i], Croie) for i in range(3)):
        playerXScore = playerXScore + 1
        reset()
    if all(Tab[i][i] == Tab[0][0] and isinstance(Tab[i][i], Cercle) for i in range(3)) or all(Tab[i][2 - i] == Tab[0][0] and isinstance(Tab[i][2 - i], Cercle) for i in range(3)):
        playerOScore = playerOScore + 1
        reset()
    



        
def mouseClicked():
    for i in range(3):
        for j in range(3):
            if Tab[i][j] is None:
                if mouseX > 200 + i*200 and mouseX < 400 + i*200 and mouseY > j*200 and mouseY < 200 + j*200:
                    debug(i,j)
                    check_winner()

def setup():
    size(800,600)
    
def draw():
    ui()
    
    

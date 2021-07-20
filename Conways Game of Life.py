import pygame
pygame.init()
import Button as b

class game:
    def __init__(self):
        self.gamerunning=True
        self.window=gamewindow()
        self.clock=pygame.time.Clock()
        while self.gamerunning:
            self.clock.tick(40)
            self.continuerunning=self.window.drawwindow()
            if self.continuerunning==1:
                self.gamerunning=False

        pygame.quit()

class gamewindow:
    def __init__(self):
        self.pygamewindow=pygame.display.set_mode((1000,750))
        pygame.display.set_caption('Conways game of Life')
        self.clock=pygame.time.Clock()
        self.isstartscreen=True
        self.isgamescreen=False
        self.titlefont=pygame.font.SysFont('comicsansms',85)

        self.gamecolony=cellcolony([5,25,45])

        ### colors

        self.black=(0,0,0)
        self.white=(255,255,255)
        self.red=(255,0,0)

        self.startbutton=b.Button(self.pygamewindow,'Start',500,500,150,50,self.black,self.white,self.black,35)

        self.squarebutton=b.Button(self.pygamewindow,'Square',130,575,85,28,self.black,self.white,self.black,20)
        self.donutbutton = b.Button(self.pygamewindow,'Donut',220,575,85,28,self.black,self.white,self.black,20)
        self.longdonutbutton = b.Button(self.pygamewindow,'Long Donut',325,575,115,28,self.black,self.white,self.black,20)
        self.chickenwingbutton = b.Button(self.pygamewindow,'Chicken Wing',460,575,135,28,self.black,self.white,self.black,20)
        self.bigdonutbutton = b.Button(self.pygamewindow,'Big Donut',595,575,115,28,self.black,self.white,self.black,20)
        self.roadbutton = b.Button(self.pygamewindow,'Road',700,575,85,28,self.black,self.white,self.black,20)
        self.blinkerbutton = b.Button(self.pygamewindow,'Blinker',170,615,85,28,self.black,self.white,self.black,20)
        self.toadbutton = b.Button(self.pygamewindow,'Toad',260,615,85,28,self.black,self.white,self.black,20)
        self.beaconbutton = b.Button(self.pygamewindow,'Beacon',350,615,85,28,self.black,self.white,self.black,20)
        self.clockbutton = b.Button(self.pygamewindow,'Clock',440,615,85,28,self.black,self.white,self.black,20)
        self.tripolebutton = b.Button(self.pygamewindow,'Tripole',530,615,85,28,self.black,self.white,self.black,20)
        self.tumblerbutton = b.Button(self.pygamewindow,'Tumbler',620,615,85,28,self.black,self.white,self.black,20)
        self.gliderbutton = b.Button(self.pygamewindow,'Glider',280,655,85,28,self.black,self.white,self.black,20)
        self.spaceshipbutton = b.Button(self.pygamewindow,'Spaceship',390,655,115,28,self.black,self.white,self.black,20)
        self.octagonbutton = b.Button(self.pygamewindow,'Octagon',710,615,85,28,self.black,self.white,self.black,20)
        self.boatbutton = b.Button(self.pygamewindow,'Boat',790,575,85,28,self.black,self.white,self.black,20)
        
        

    def drawwindow(self):
        self.pygamewindow.fill((255,255,255))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return 1

        if self.isstartscreen:
            self.drawstartscreen()

        if self.isgamescreen:
            self.drawgamescreen()
            
        pygame.display.update()

    def drawstartscreen(self):
        text=self.titlefont.render('Conways Game of life',1,(0,0,0))
        self.pygamewindow.blit(text,(round(500-text.get_width()/2),150))
        sbpressed=self.startbutton.run()
        if sbpressed:
            self.isstartscreen=False
            self.isgamescreen=True

    def drawgamescreen(self):
        pygame.draw.line(self.pygamewindow,self.red,(0,550),(1000,550))
        self.gamecolony.draw(self.pygamewindow)

        font = pygame.font.SysFont('comicsansms',20)
        text = font.render('Static:',1,(0,0,0))
        self.pygamewindow.blit(text,(10,560))
        text = font.render('Oscillators:',1,(0,0,0))
        self.pygamewindow.blit(text,(10,600))
        text = font.render('Gliders and Spaceships:',1,(0,0,0))
        self.pygamewindow.blit(text,(10,640))

        squarebuttonpressed = self.squarebutton.run()
        if squarebuttonpressed:
            self.gamecolony = cellcolony([91,92,111,112])
        donutbuttonpressed = self.donutbutton.run()
        if donutbuttonpressed:
            self.gamecolony = cellcolony([91,110,112,131])
        longdonutbuttonpressed = self.longdonutbutton.run()
        if longdonutbuttonpressed:
            self.gamecolony = cellcolony([91,110,130,112,132,151])
        chickenwingbuttonpressed = self.chickenwingbutton.run()
        if chickenwingbuttonpressed:
            self.gamecolony = cellcolony([70,71,89,92,110,112,131])
        bigdonutbuttonpressed = self.bigdonutbutton.run()
        if bigdonutbuttonpressed:
            self.gamecolony = cellcolony([70,71,89,92,109,112,130,131])
        roadbuttonpressed = self.roadbutton.run()
        if roadbuttonpressed:
            self.gamecolony = cellcolony([53,72,74,91,93,112])
        blinkerbuttonpressed = self.blinkerbutton.run()
        if blinkerbuttonpressed:
            self.gamecolony = cellcolony([90,91,92])
        toadbuttonpressed = self.toadbutton.run()
        if toadbuttonpressed:
            self.gamecolony = cellcolony([90,91,92,71,72,73])
        beaconbuttonpressed = self.beaconbutton.run()
        if beaconbuttonpressed:
            self.gamecolony = cellcolony([47,48,67,68,89,90,109,110])
        clockbuttonpressed = self.clockbutton.run()
        if clockbuttonpressed:
            self.gamecolony = cellcolony([49,69,71,90,88,110])
        tripolebuttonpressed = self.tripolebutton.run()
        if tripolebuttonpressed:
            self.gamecolony = cellcolony([47,48,67,88,90,111,130,131])
        tumblerbuttonpressed = self.tumblerbutton.run()
        if tumblerbuttonpressed:
            self.gamecolony = cellcolony([46,47,51,52,65,66,68,70,72,73,88,90,108,110,147,148,150,151])
        gliderbuttonpressed = self.gliderbutton.run()
        if gliderbuttonpressed:
            self.gamecolony = cellcolony([1,3,22,23,42])
        spaceshipbuttonpressed = self.spaceshipbutton.run()
        if spaceshipbuttonpressed:
            self.gamecolony = cellcolony([42,43,44,45,61,65,85,101,104])
        octagonbuttonpressed = self.octagonbutton.run()
        if octagonbuttonpressed:
            self.gamecolony = cellcolony([28,31,48,51,66,67,69,70,72,73,88,91,108,111,126,127,129,130,132,133,148,151,168,171])
        boatpressed = self.boatbutton.run()
        if boatpressed:
            self.gamecolony = cellcolony([49,50,69,71,90])
            


class cellcolony:
    def __init__(self,alivearray):
        self.updatecounter=0
        self.alivearray=alivearray
        ### colors

        self.black=(0,0,0)
        self.white=(255,255,255)
        self.red=(255,0,0)

        self.appendx=100
        self.appendy=75
        self.appendcol=1
        self.appendrow=1
        self.counter=1

        self.updatebool=False
        
        self.cellarray=[]
        for i in range(200):
            beginAlive=False
            
            for f in self.alivearray:
                if f==self.counter:
                    beginAlive=True
            
            self.cellarray.append(cell(self.appendx,self.appendy,self.appendcol,self.appendrow,beginAlive))
            if self.appendcol==20:
                self.appendcol=1
                self.appendx=100
                self.appendrow+=1
                self.appendy+=40

            else:
                self.appendcol+=1
                self.appendx+=40

            self.counter+=1


    def draw(self,window):
        if self.updatecounter==10:
            self.updatecounter=0
            for e in self.cellarray:
                e.getwillbealive(self.cellarray)
        else:
            self.updatecounter+=1
        
        for e in self.cellarray:
            e.draw(window)


class cell:
    def __init__(self,x,y,column,row,isalive):
        self.x=x
        self.y=y
        self.column=column
        self.row=row
        self.isalive=isalive
        self.willbealive=isalive

        ### colors

        self.black=(0,0,0)
        self.white=(255,255,255)
        self.red=(255,0,0)

    def getalive(self):
        return self.isalive

    def getposition(self):
        return [self.row,self.column]

    def draw(self,window):
        self.isalive=self.willbealive
        
        if self.isalive:
            pygame.draw.rect(window,self.black,(self.x,self.y,40,40),0)

        else:
            pygame.draw.rect(window,self.black,(self.x,self.y,40,40),1)

    def getwillbealive(self,cellarray):
        NeighboursAlive=0

        
        for cell in cellarray:
        
            cellposition=cell.getposition()

            ## TOP
            if cellposition[0]==self.row-1 and cellposition[1]==self.column:
                if cell.getalive()==True:
                    NeighboursAlive+=1
           ## elif self.row==1:
                ##if cellposition[0]==10 and cellposition[1]==self.column:
                    ##if cell.getalive():
                        ##NeighboursAlive+=1

            ## TOP-RIGHT
            if cellposition[0]==self.row-1 and cellposition[1]==self.column+1:
                if cell.getalive()==True:
                    NeighboursAlive+=1
            ##elif self.row==1 and self.column==20:
                ##if cellposition[0]==10 and cellposition[1]==1:
                   ##if cell.getalive()==True:
                        ##NeighboursAlive+=1
            ##elif self.row==1:
                ##if cellposition[0]==10 and cellposition[1]==self.column+1:
                   ##if cell.getalive()==True:
                        ##NeighboursAlive+=1
            ##elif self.column==20:
                ##if cellposition[0]==self.row-1 and cellposition[1]==1:
                   ##if cell.getalive()==True:
                        ##NeighboursAlive+=1

            ## TOP-LEFT
            if cellposition[0]==self.row-1 and cellposition[1]==self.column-1:
                if cell.getalive()==True:
                    NeighboursAlive+=1
            ##elif self.row==1 and self.column==1:
                ##if cellposition[0]==10 and cellposition[1]==20:
                   ##if cell.getalive()==True:
                        ##NeighboursAlive+=1
            ##elif self.row==1:
                ##if cellposition[0]==10 and cellposition[1]==self.column-1:
                   ##if cell.getalive()==True:
                        ##NeighboursAlive+=1
            ##elif self.column==1:
                ##if cellposition[0]==self.row-1 and cellposition[1]==1:
                   ##if cell.getalive()==True:
                        ##NeighboursAlive+=1

            ## LEFT
            if cellposition[0]==self.row and cellposition[1]==self.column-1:
                if cell.getalive():
                    NeighboursAlive+=1
            ##elif self.column==1:
                ##if cellposition[0]==self.row and cellposition[1]==20:
                    ##if cell.getalive():
                        ##NeighboursAlive+=1

            ## BOTTOM-LEFT
            if cellposition[0]==self.row+1 and cellposition[1]==self.column-1:
                if cell.getalive()==True:
                    NeighboursAlive+=1
            ##elif self.row==10 and self.column==1:
                ##if cellposition[0]==1 and cellposition[1]==20:
                    ##if cell.getalive()==True:
                        ##NeighboursAlive+=1 
            ##elif self.row==10:
                ##if cellposition[0]==1 and cellposition[1]==self.column-1:
                   ##if cell.getalive()==True:
                        ##NeighboursAlive+=1
            ##elif self.column==1:
                ##if cellposition[0]==self.row-1 and cellposition[1]==20:
                   ##if cell.getalive()==True:
                        ##NeighboursAlive+=1

            ## BOTTOM
            if cellposition[0]==self.row+1 and cellposition[1]==self.column:
                if cell.getalive():
                    NeighboursAlive+=1
            ##elif self.row==10:
                ##if cellposition[0]==1 and cellposition[1]==self.column:
                    ##if cell.getalive():
                        ##NeighboursAlive+=1

            ## BOTTOM-RIGHT
            if cellposition[0]==self.row+1 and cellposition[1]==self.column+1:
                if cell.getalive()==True:
                    NeighboursAlive+=1
            ##elif self.row==10 and self.column==20:
                ##if cellposition[0]==1 and cellposition[1]==1:
                   ##if cell.getalive()==True:
                        ##NeighboursAlive+=1
            ##elif self.row==10:
                ##if cellposition[0]==1 and cellposition[1]==self.column+1:
                   ##if cell.getalive()==True:
                       ## NeighboursAlive+=1
            ##elif self.column==20:
                ##if cellposition[0]==self.row-1 and cellposition[1]==1:
                   ##if cell.getalive()==True:
                        ##NeighboursAlive+=1

            ## RIGHT
            if cellposition[0]==self.row and cellposition[1]==self.column+1:
                if cell.getalive():
                    NeighboursAlive+=1
            ##elif self.column==20:
                ##if cellposition[0]==self.row and cellposition[1]==1:
                    ##if cell.getalive():
                        ##NeighboursAlive+=1

            
        if self.isalive==False and NeighboursAlive==3:
            self.willbealive=True

        if NeighboursAlive<2:
            self.willbealive=False

        if self.isalive:
            if NeighboursAlive==2 or NeighboursAlive==3:
                self.willbealive=True

        if NeighboursAlive>3:
            self.willbealive=False
            
    

if __name__=='__main__':
    newgame=game()

import pygame

class Button:
    def __init__(self,window,message,x,y,width,height,nothovertextcol,hovertextcol,color,size):
        self.window=window
        self.message=message
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.nothovertextcol=nothovertextcol                                           #color of text inside button when not hovering over it
        self.hovertextcol=hovertextcol                                                 #color of text inside button when hovering over it
        self.color=color                                                               #color of frame, unfilled
        self.size=size                                                                 #size of text in button
        self.font1=pygame.font.SysFont('comicsansms',self.size)
        self.x=self.x-self.width/2
        self.y=self.y-self.height/2                                                    #coordinates entered will be middle point of button

    def run(self):
        mouse=pygame.mouse.get_pos()
        if self.x<mouse[0]<self.x+self.width and self.y<mouse[1]<self.y+self.height:   #if cursor is on button
            pygame.draw.rect(self.window,self.color,(self.x,self.y,self.width,self.height))
            text=self.font1.render(self.message,1,self.hovertextcol)
            self.window.blit(text,(round(self.x + (self.width/2 - text.get_width()/2)),round( self.y + (self.height/2 - text.get_height()/2))))

            click=pygame.mouse.get_pressed()
            if click[0]==1:
                loop=True
                while loop:
                    e=False
                    for event in pygame.event.get():
                        if event.type==pygame.MOUSEBUTTONUP:
                            e=True
                    if e:
                        return True

            else:
                return False

        else:
            pygame.draw.rect(self.window,self.color,(self.x,self.y,self.width,self.height),1)
            text=self.font1.render(self.message,1,self.nothovertextcol)
            self.window.blit(text,(round(self.x + (self.width/2 - text.get_width()/2)),round( self.y + (self.height/2 - text.get_height()/2))))

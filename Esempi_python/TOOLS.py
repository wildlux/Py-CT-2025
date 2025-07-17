import pygame
pygame.init()

x,y = 500
screen = pygame.display.set_mode((x ,y))
screen.fill("white")
pygame.display.set_caption("il mio primo gioco su pygame" )

#pygame.draw.line  ( screen ,"black"  ,(0,0), (300,300),5  )
#pygame.draw.lines ( screen ,"orange" , True, [(100,100),(200,100)] , 4)
#pygame.draw.rect ( screen ,"red" , (50,50,100,100),7)
#pygame.draw.circle ( screen ,"green" , (200,150,),50,7)
#pygame.draw.ellipse(screen , "yellow" ,(100,100,100,50),4)
#pygame.draw.polygon(screen , "blue" , ((250,75),(300,25), (350,75)),0)

pygame.draw.rect ( screen ,"yellow" , (100,200,80,40),7)
#font1 = pygame.font.Font(screen, 24)
#surf_text = fnt.render("Hello world!", True, "yellow")

done = True
while done:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         done = False

   pygame.display.flip()

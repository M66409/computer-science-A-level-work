import pygame

pygame.init()
print(pygame.font.get_fonts())
screen=pygame.display.set_mode((500,400))
clock=pygame.time.Clock()
running=True
dt=0

player_pos=pygame.Vector2(screen.get_width()/2,screen.get_height()/2)
text=""
copy=""
while running:
    print(text)
    for event in pygame.event.get():
      if (event.type==pygame.KEYDOWN):
        if event.key==pygame.K_BACKSPACE:
          if len(text)>0:
            text=text[:-1]
        elif event.key==pygame.K_RETURN:
          if text=="heal()":
            copy="do you want to heal with a potion?"
          text=""
        else:
          text+=event.unicode
        if event.type==pygame.QUIT:
            running=False
          
    screen.fill("blue")
    #image=pygame.image.load("something.jpg").convert()
    #screen.blit(image,(200,150))
    pygame.draw.circle(screen,"red",player_pos,50)
    font=pygame.font.Font(None,32)
    text_surface=font.render(text,True,"black")
    s=pygame.font.Font(None,32)
    f=s.render(copy,True,"black")
    screen.blit(f,(250,200))
    screen.blit(text_surface,(00,350))

    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y-=300*dt
    if keys[pygame.K_s]:
        player_pos.y+=300*dt
    if keys[pygame.K_a]:
        player_pos.x-=300*dt
    if keys[pygame.K_d]:
        player_pos.x+=300*dt
    pygame.display.flip()

    dt=clock.tick(60)/1000
pygame.quit()

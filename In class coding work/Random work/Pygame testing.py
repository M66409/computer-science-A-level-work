import pygame

pygame.init()
screen=pygame.display.set_mode((500,400))
clock=pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    choice=pygame.key.start_text_input()
    pygame.TEXTINPUT
    #print(pygame.TEXTEDITING)

    screen.fill("white")
    font=pygame.font.SysFont("arial",14)
    text=font.render("What class do you want to play? Knight, Merchant, Healer, or the base class",True,(0,0,0))
    screen.blit(text,(0,350))

    pygame.display.flip()

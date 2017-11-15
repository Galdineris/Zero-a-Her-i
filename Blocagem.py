#26/10
import pygame
import random
import sys

def draw_tela():
    screen.fill((0,255,0))
    
    pygame.draw.rect(screen,white,hercules,3)
    
    for i in range(len(hidra)): pygame.draw.rect(screen,white,hidra[i],3)

    for i in range(len(galho)): pygame.draw.rect(screen,white,galho[i],2)
    
    pygame.display.update()

def cortar():
    for j in range(len(hidra)):
        for i in range(20):
            hidra[j].y += 5
            draw_tela()
            if hidra[j].y > 650:
                hidra[j].y -= 600
    for j in range(len(galho)):
        for i in range(20):
            galho[j].y += 5
            draw_tela()
            if galho[j].y > 650:
                galho[j].y -= 600
    print("tecla")


pygame.init()

screen = pygame.display.set_mode((600,700))

pygame.display.set_caption("Hercules")

screen.fill((0,255,0))

white = (255,255,255)

posicao = [250,200]

galho = [pygame.Rect(400,550,100,50), pygame.Rect(100,450,100,50),pygame.Rect(400,350,100,50),pygame.Rect(100,250,100,50),pygame.Rect(400,150,100,50),pygame.Rect(100,50,100,50)]

hidra = [pygame.Rect(200,550,200,100),pygame.Rect(200,450,200,100),pygame.Rect(200,350,200,100),pygame.Rect(200,250,200,100),pygame.Rect(200,150,200,100),pygame.Rect(200,50,200,100)]

hercules = pygame.Rect(140,550,50,100)

galhos = [[0,1,1,0,0],[0,0,1,1,0]]
hero = [0,0]

draw_tela()

pygame.display.update()

while True:
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:

            #random Galhos
            for j in range(2):
                for i in range(len(galhos)-1, 0):
                    galhos[j][i] = galhos[j][i-1]
                galhos[j][0] = random.getrandbits(1)
            print(galhos)

            #desenhar galhos
            for j in range(2):
                for i in range(len(galhos)):
                    pass
                
            

            #Sair com ESC
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            #Setas
            if event.key == pygame.K_LEFT:
                hercules = pygame.Rect(140,550,50,100)
                cortar()
                hero = [1,0]
            if event.key == pygame.K_RIGHT:
                hercules = pygame.Rect(410,550,50,100)
                cortar()
                hero = [0,1]

        draw_tela()





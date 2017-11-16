#26/10
import pygame
import time
import random
import sys

inicio = time.time()############

def draw_tela():   #EU SIRVO PARA REDESENHAR A TELA (AKA SOU OS "FRAMES" DO JOGO)
    screen.fill((0,255,0))
    
    for i in range(len(hidra)): pygame.draw.rect(screen,white,hidra[i],3)

    for i in range(len(cabecas)): pygame.draw.rect(screen,white,cabecas[i],2)

    pygame.draw.rect(screen,white,hercules,3)

    scoretext = fonte.render("Pontos {0}".format(score),10, (0,0,0),white)
    screen.blit(scoretext, (300, 10))

    tempotext = fonte.render("Tempo 00:{0}".format(60 - segundos),10, (0,0,0),white)
    screen.blit(tempotext, (100, 10))
    
    pygame.display.update()

def cortar(lado,posicao):  #SOU RESPONSÁVEL POR MOVER OS OBJETOS E SOU CHAMADO TODO COMANDO (-----------------TALVEZ OS PONTOS SEJAM BONS COLOCAR AQUI???----------------)
    
    #estouro de tela HIDRA (loop visual)
    for j in range(len(hidra)):
        for i in range(25):
            hidra[j].y += 4
            draw_tela()
            if hidra[j].y > 650:
                hidra[j].y -= 600

    #estouro de tela posicao (loop visual e GERAÇÃO DAS CABEÇAS ALEATÓRIAS)
    for j in range(len(cabecas)):
        for i in range(25):
            cabecas[j].y += 4
            draw_tela()
            #estouro de tela e geração de posicao
            if cabecas[j].y > 650:
                cabecas[j].y -= 600
                posicao[j] = random.randint(0,1)
                cabecas[j].x = 100 + 300*posicao[j]




pygame.init()


segundos = 0


score = 0

screen = pygame.display.set_mode((600,700)) #TAMANHO DA TELA (SE FOR ME ALTERAR, LEMBRAR QUE TODOS OS VALORES FORAM BASEADOS EM MIM)

pygame.display.set_caption("De Zero a Herói") #NOME DA JANELA DO JOGO (IDEAL COLOCAR NOME DO JOGO)

screen.fill((0,255,0))  #BACKGROUND, PROCURE POR MIM NO CRTL+H QUANDO FOR ALTERAR O MSM

white = (255,255,255)   #COR DAS FORMAS, CTRL+H EM MIM

cabecas = [pygame.Rect(400,550,100,50)  , pygame.Rect(400,450,100,50),    pygame.Rect(400,350,100,50),    pygame.Rect(400,250,100,50),   pygame.Rect(400,150,100,50),   pygame.Rect(400,50,100,50)] #desenho cabeças (galhos)

hidra = [pygame.Rect(200,550,200,100) , pygame.Rect(200,450,200,100),   pygame.Rect(200,350,200,100),   pygame.Rect(200,250,200,100),  pygame.Rect(200,150,200,100),  pygame.Rect(200,50,200,100)] # desenho pescoço

hercules = pygame.Rect(140,550,50,100) # desenho herói

posicao = [random.randint(0,1) for i in range(6)] #lado que as cabeças (galhos) vão aparecer

fonte = pygame.font.SysFont("Comic Sans MS",30)
relogio = pygame.font.SysFont("Comic Sans MS",30)






for i in range(len(posicao)): #Crio a tela inicial
    if posicao[i] == 0:
        cabecas[i].x = 100

cabecas[0].x = 1000 #Gambiarra para a 1ª cabeça não aperecer na tela ao iniciar

lado = 0

draw_tela()

agora = time.time()#################

pygame.display.update()

while True:

    ##########
    agora = time.time() - inicio
    minutos = int(agora/60)
    segundos = int(agora%60)
    
    if segundos >= 20:
        print("tempo esgotado")
        lado = 666
    ########
    draw_tela()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #sair ao clickar no x no canto da janela
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN: #evento de pressionar botão, testes especificos de cada botão

            if event.key == pygame.K_ESCAPE: #Sair com ESC
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_LEFT: #Controle Setas
                hercules = pygame.Rect(140,550,50,100)
                cortar(lado,posicao)
                lado = 0
                score+=1
                
            if event.key == pygame.K_RIGHT:
                hercules = pygame.Rect(410,550,50,100)
                cortar(lado,posicao)
                lado = 1
                score+=1
                

            for i in range(len(cabecas)): #TESTE DE "COLISÃO" ---ENDGAME---
                if cabecas[i].y == 550:
                    if posicao[i] == lado:
                        print("VIROU COMIDA DA CABEÇA DO MEU MONSTRO")
                        lado = 666 #FLAG DE DERROTA            

            
            
    draw_tela()
    
    #QUEBRA DO LOOP JOGO
    if lado == 666:
        screen.fill(white)
        texto = fonte.render("FIM DE JOGO",10, (0,0,0),white)
        screen.blit(texto, (300, 550))
        pygame.display.update()
        time.sleep(2)
        break

#################################    DAQUI PARA BAIXO FECHA O PROGRAMA #######################################
print("fim de jogo")
pygame.quit()
sys.exit()



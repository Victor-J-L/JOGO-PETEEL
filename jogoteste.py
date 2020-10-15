#COLISÃO COM IMAGENS 

import pygame
import random
def main():
    #as definições dos objetos (variaveis)
    pygame.init()
    tela = pygame.display.set_mode([600, 600])
    pygame.display.set_caption("Iniciando o Pygame")
    relogio = pygame.time.Clock() #isso fica dentro do main, consigo capturar info de atualização da tela, o tempo.
    
    #CORES

    cor_branca = (255,255,255) #definindo cor
    cor_verde = (152, 231, 114)
    cor_azul = (108, 194, 236)
    cor_vermelha = (227, 57, 9)
    cor_rosa = (253,147,226)
   
    #OBJ/IMG

    imagem = pygame.image.load("testando.jpg") #poe nome da img
    (x,y) = (150,150) #posição da imagem
    ret = pygame.Rect(250,300,20,500)
    vx = 0 #atribuimos variavel velocidade 
    vy = 0
    sair = False
    while sair != True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            
            if event.type == pygame.KEYDOWN: #se o evento for do tipo tecla pressionada (keydown) (entao verifica se alguma tecla ta pressionada)
                if event.key == pygame.K_LEFT: #se a tecla pressionada (event.key) receber o pygame.K_LEFT (seta da esquerda) então mova a -10 o retangulo)
                    vx -= 5 #então quando pressionar a imagem vai só ir até vc clicar pra parar em outra tecla que vx é 0
                if event.key == pygame.K_RIGHT:
                    vx += 5
                if event.key == pygame.K_DOWN:
                    vy += 5
                if event.key == pygame.K_UP:
                    vy -= 5
            if event.type == pygame.KEYUP: #se soltar tecla
                if event.key == pygame.K_LEFT:
                    vx = 0
                if event.key == pygame.K_RIGHT: #nesse caso quando solta botão ele para
                    vx = 0
                if event.key == pygame.K_DOWN:
                    vy = 0
                if event.key == pygame.K_UP:
                    vy = 0
              
        tela.fill(cor_branca) #sempre cuidar com a ordem das coisas que poe na tela
        tela.blit(imagem, (x,y)) #poe posição da tua imagem e faz aparecer
        
        #(x,y) = pygame.mouse.get_pos() #variavel receb posição do mouse
        pygame.draw.rect(tela, cor_vermelha, ret)
        x += vx #nao sei pq ele fez isso
        y += vy
        relogio.tick(30)
        pygame.display.update() 
  
    pygame.quit()
main() 
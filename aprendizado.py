#1

import pygame
x = pygame.init()
print(x)

#display

import pygame
def main():
    pygame.init()
    pygame.display.set_mode([300, 300])
main()

#tudo que quer que aconteça nessa janela vai ter que ser através de eventos

import pygame
def main():
    pygame.init()
    pygame.display.set_mode([300, 300])
    pygame.display.set_caption("Iniciando com Pygame") #nome da janela
    #pygame.quit() quando chega nesse momento do código a janela fecha
    sair = False
    while sair != True:
        for event in pygame.event,get():
            if event.type == pygame.QUIT:
                sair = True
        pygame.display.update() #atualização na tela  tempo todo
    pygame.quit()
main() 

#trabalhar com frames

import pygame
def main():
    #as definições dos objetos (variaveis)
    pygame.init()
    tela = pygame.display.set_mode([300, 300])
    pygame.display.set_caption("Iniciando o Pygame")
    relogio = pygame.time.Clock() #isso fica dentro do main, consigo capturar info de atualização da tela, o tempo.
    cor_branca = (255,255,255) #definindo cor
    sair = False
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
        relogio.tick(27) #atualizando de 27 quadros por segundo
        tela.fill(cor_branca) #trabalhando com o fundo/preenchimentl, valor hexadecimal vai dar essa cor
        pygame.display.update() #atualização na tela  tempo todo
    pygame.quit()
main() 
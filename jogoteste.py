import pygame
def main():
    #as definições dos objetos (variaveis)
    pygame.init()
    tela = pygame.display.set_mode([300, 300])
    pygame.display.set_caption("Iniciando o Pygame")
    relogio = pygame.time.Clock() #isso fica dentro do main, consigo capturar info de atualização da tela, o tempo.
    cor_branca = (255,255,255) #definindo cor
    cor_verde = (152, 231, 114)
    cor_azul = (108, 194, 236)
    cor_vermelha = (227, 57, 9)

    sup = pygame.Surface((200, 200)) #definindo sueprficie
    sup.fill(cor_azul) #superfície sup vai ser rpeenchida com essa cor
    
    sup2 = pygame.Surface((100,100))
    sup2.fill(cor_verde)

    ret = pygame.Rect(10, 10, 45, 45)

    sair = False
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.MOUSEBUTTONDOWN: #criando evento quando clica com mouse
                 ret = ret.move(10, 10) #a cada clique ele se move 10 pixeis nessa direção de x e y (diagonal ifnerior)
            if event.type == pygame.MOUSEMOTION:
                ret = ret.move(-10, -10)
       
        relogio.tick(27) #atualizando de 27 quadros por segundo
        tela.fill(cor_branca) #trabalhando com o fundo/preenchimentl, valor hexadecimal vai dar essa cor
        tela.blit(sup, [50, 50]) #chamando superfície pela variavel e depois pela posição no cartesiano
        tela.blit(sup2, [70,70])
        pygame.draw.rect(tela, cor_vermelha, ret) #para fazer o retangulo la ret na tela
        pygame.display.update() #atualização na tela  tempo todo
  
    pygame.quit()
main() 
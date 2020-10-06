#Curso PYGAME
import pygame
def main():
    pygame.init()
    tela = pygame.display.set_mode([300, 300])
    pygame.display.set_caption("Iniciando o pygame")
    relogio = pygame.time.Clock()
    cor_branca = (255,255,255)
    cor_azul = (16,118,148)
    cor_verde = (74,117,43)

    sup = pygame.Surface((200,200))
    sup.fill(cor_verde)
    sup2 = pygame.Surface((100,100))
    sup2.fill(cor_azul)
    sair = False

    while sair != True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                sair = True
        relogio.tick(30)
        tela.fill(cor_branca)
        tela.blit(sup,[50,50])  
        tela.blit(sup2,[100,100]) 
        pygame.display.update()
    pygame.quit() 


main()

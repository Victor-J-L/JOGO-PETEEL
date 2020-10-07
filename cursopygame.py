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
    cor_amarela = (255,248,0)

    sup = pygame.Surface((200,200))
    sup.fill(cor_verde)
    sup2 = pygame.Surface((100,100))
    sup2.fill(cor_azul)
    ret= pygame.Rect(10, 10, 45, 45)
    sair = False

    while sair != True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_pos(150,150)
            #if event.type == pygame.MOUSEMOTION:
                #ret = ret.move(g-10,-10)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ret.move_ip(-10,-0)
                if event.key == pygame.K_RIGHT:
                    ret.move_ip(10,-0)
                if event.key == pygame.K_DOWN:
                    ret.move_ip(0,10)
                if event.key == pygame.K_UP:
                    ret.move_ip(0,-10)
                if event.key == pygame.K_SPACE:
                    ret.move_ip(10,10)
                if event.key == pygame.K_BACKSPACE:
                    ret.move_ip(10,-10)
        relogio.tick(150)
        tela.fill(cor_branca)
        tela.blit(sup,[50,50])  
        tela.blit(sup2,[100,100])
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width/2
        ret.top -= ret.height/2
        pygame.draw.rect(tela, cor_amarela, ret) 
        pygame.display.update()
    pygame.quit() 


main()

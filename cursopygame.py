#Curso PYGAME
import pygame
def main():
    pygame.init()
    tela = pygame.display.set_mode([300, 300])
    pygame.display.set_caption("Iniciando o pygame")
    relogio = pygame.time.Clock()
   
   #CORES
    cor_branca = (255,255,255)
    cor_azul = (16,118,148)
    cor_verde = (74,117,43)
    cor_amarela = (255,248,0)
    cor_roxa = (106, 52, 114)

   #SUPERFÍCIES
    sup = pygame.Surface((200,200))
    sup.fill(cor_verde)
    sup2 = pygame.Surface((100,100))
    sup2.fill(cor_azul)

   #OBJETOS 
    ret= pygame.Rect(10, 10, 45, 45)
    ret2= pygame.Rect(100,80,130,60)

   #FONTE
    pygame.font.init()

    font_padrao = pygame.font.get_default_font()
    font_lose = pygame.font.SysFont(font_padrao, 45)
    font_ganhou = pygame.font.SysFont(font_padrao, 30)

   #ÁUDIOS 
    audio_explosao = pygame.mixer.Sound('explosao.ogg')

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

        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width/2
        ret.top -= ret.height/2
        if ret.colliderect(ret2):
            text = font_lose.render('COLIDIU', 1, (255, 255, 255))
            tela.blit(text, (150,150))
            audio_explosao.play()
            audio_explosao.set_volume(0.01)
            (ret.left, ret.top) = (xant, yant)
        pygame.draw.rect(tela, cor_amarela, ret)
        pygame.draw.rect(tela, cor_roxa, ret2) 
        pygame.display.update()
    pygame.quit() 


main()

#exemplo de jogo

import pygame 

def main():
    pygame.init()
    tela = pygame.display.set_mode([500,650])
    pygame.display.set_caption("Jogo Iniciante")
    relogio = pygame.time.Clock()
    cor_branca = (255,255,255)
    cor_verde = (152, 231, 114)
    cor_azul = (108, 194, 236)
    cor_vermelha = (227, 57, 9)
    cor_rosa = (253,147,226)
    cor_preta = (0,0,0)
    sup = pygame.Surface ((600,2450))
    sup.fill(cor_preta)

    ret = pygame.Rect(10,10, 30, 30)
    ret2 = pygame.Rect (10, 70, 555, 6)
    ret3 = pygame.Rect(10,120,350,6)
    ret4 = pygame.Rect(405,120,195,6)
    ret5 = pygame.Rect(45, 170, 555,6)

    sair = False

    pygame.font.init()

    font_padrao = pygame.font.get_default_font() 
    fonte_perdeu = pygame.font.SysFont(font_padrao,45)
    fonte_ganhou = pygame.font.SysFont(font_padrao,30)

    audio_explosao = pygame.mixer.Sound('explosion.wav')

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
           
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_pos(10,10)
                ret2.left = 10
                main() #só chamar a main que vai criar os objetos de novo

        relogio.tick(30)
        tela.fill(cor_branca)
        tela.blit(sup, [0,0]) 
    
        (xant, yant) = (ret.left, ret.top) 
        (ret.left, ret.top) = pygame.mouse.get_pos() 
        ret.left -= ret.width/2 
        ret.top -= ret.height/2 

        if ret.colliderect(ret2) or ret.colliderect(ret3) or ret.colliderect(ret4): 
            text = fonte_perdeu.render('Você perdeu!', 1, (255,255,255)) 
            tela.blit(text, (150,150)) 
            pygame.mouse.set_pos(10,10) #isso vai fazer com que quando perca/encoste na plataforma ele volte a posição tal
            audio_explosao.play() 
            audio_explosao.set_volume(0.5) 
            (ret.left, ret.top) = (xant, yant)


        if ret.top > 400:
            text = fonte_ganhou.render('VOCÊ GANHOU', 1, (255,255,255)) 
            tela.blit(text,(200, 200))
            text = fonte_perdeu.render('clique para recomeçar', 1, cor_vermelha) 
            tela.blit(text,(150,250))
            ret2.left, ret3.left, ret4.left = 602, 602, 602
        pygame.draw.rect(tela, cor_vermelha, ret)
        pygame.draw.rect(tela, cor_branca, ret2)
        pygame.draw.rect(tela, cor_branca, ret3)
        pygame.draw.rect(tela, cor_branca, ret4)
        pygame.draw.rect(tela, cor_branca, ret5)
        pygame.display.update() 
  
    pygame.quit()

main() 
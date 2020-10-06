import pygame 

def main():
    pygame.init()
    tela = pygame.display.set_mode([600,450])
    pygame.display.set_caption("Jogo Iniciante")
    relogio = pygame.time.Clock()
    cor_branca = (255,255,255)
    cor_verde = (152, 231, 114)
    cor_azul = (108, 194, 236)
    cor_vermelha = (227, 57, 9)
    cor_rosa = (253,147,226)
    sup = pygame.Surface ((600,2450))
    sup.fill(cor_azul)

    ret = pygame.Rect(10,10, 30, 30)
    ret2 = pygame.Rect (10, 40, 555, 6)

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
                pygame.mouse.set_pos(150,150)

        relogio.tick(30)
        tela.fill(cor_branca)
        tela.blit(sup, [0,0]) #0,0 pra nao deslocar ela pq ela tem a mesma dimensao da tela entao fica emcima certinho
    
        (xant, yant) = (ret.left, ret.top) #x anterior e y anterior guarda posição
        (ret.left, ret.top) = pygame.mouse.get_pos() #esse evtno captura posição do mouse e parte esq e direita fica associada ao mouse
        ret.left -= ret.width/2 #esquerda mouse vai ficar sempre no centro
        ret.top -= ret.height/2 

        if ret.colliderect(ret2): #se ret 1 colodir com ret 2 
            (ret.left, ret.top) = (xant, yant)
            text = fonte_perdeu.render('COLIDIU', 1, (255,255,255)) #render faz aparecer na tela 
            audio_explosao.play() #executa o audio com colisão
            audio_explosao.set_volume(0.5) #define volume, maior eh 1 e menor eh 0
            tela.blit(text, (150,150)) #usa blit pra jogar obj na tela entao vamos jogar o texto e poe posição


        pygame.draw.rect(tela, cor_vermelha, ret)
        pygame.draw.rect(tela, cor_rosa, ret2)
        pygame.display.update() #atualização na tela  tempo todo
  
    pygame.quit()

main() 
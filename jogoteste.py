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
    cor_rosa = (253,147,226)

    sup = pygame.Surface((200, 200)) #definindo sueprficie
    sup.fill(cor_azul) #superfície sup vai ser rpeenchida com essa cor
    
    sup2 = pygame.Surface((100,100))
    sup2.fill(cor_verde)

    ret = pygame.Rect(10, 10, 45, 45)
    ret2 = pygame.Rect (50, 50, 80, 50)

    pygame.font.init() #iniciar fonte

    font_padrao = pygame.font.get_default_font() #define variavel de texto com fonte padrão
    fonte_perdeu = pygame.font.SysFont(font_padrao,45)
    fonte_ganhou = pygame.font.SysFont(font_padrao,30)

    sair = False
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            
            if event.type == pygame.MOUSEBUTTONDOWN: #criando evento quando clica com mouse
                pygame.mouse.set_pos(150,150) #passar uma posição então usa o set em vez de get e poe posição 
                #dai o mouse quando clica pra pra essa posição e o quadrado como ta acompanhando vai junto
            """if event.type == pygame.MOUSEMOTION:
                ret = ret.move(-10, -10) #conforme movimenta mouse na tela o ret se mexe, pra isso cada tecla tem um comando ali soh ver no site
            """

            if event.type == pygame.KEYDOWN: #se o evento for do tipo tecla pressionada (keydown) (entao verifica se alguma tecla ta pressionada)
                if event.key == pygame.K_LEFT: #se a tecla pressionada (event.key) receber o pygame.K_LEFT (seta da esquerda) então mova a -10 o retangulo)
                    ret.move_ip (-10,0) #vai fazer funcionar a tecla
                if event.key == pygame.K_RIGHT:
                    ret.move_ip (10,0)
                if event.key == pygame.K_UP:
                    ret.move_ip (0,-10)
                if event.key == pygame.K_DOWN:
                    ret.move_ip (0,10)
                if event.key == pygame.K_SPACE:
                    ret.move_ip(10,10)


        relogio.tick(27) #atualizando de 27 quadros por segundo
        tela.fill(cor_branca) #trabalhando com o fundo/preenchimentl, valor hexadecimal vai dar essa cor
        tela.blit(sup, [50, 50]) #chamando superfície pela variavel e depois pela posição no cartesiano
        tela.blit(sup2, [70,70])
        (xant, yant) = (ret.left, ret.top) #x anterior e y anterior guarda posição
        (ret.left, ret.top) = pygame.mouse.get_pos() #esse evtno captura posição do mouse e parte esq e direita fica associada ao mouse
        ret.left -= ret.width/2 #esquerda mouse vai ficar sempre no centro
        ret.top -= ret.height/2 
        if ret.colliderect(ret2): #se ret 1 colodir com ret 2 
            (ret.left, ret.top) = (xant, yant)
            text = fonte_perdeu.render('COLIDIU', 1, (255,255,255)) #render faz aparecer na tela 
            tela.blit(text, (150,150)) #usa blit pra jogar obj na tela entao vamos jogar o texto e poe posição
        pygame.draw.rect(tela, cor_vermelha, ret) #para fazer o retangulo la ret na tela
        pygame.draw.rect(tela, cor_rosa, ret)
        pygame.display.update() #atualização na tela  tempo todo
  
    pygame.quit()
main()
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

#criação de sueprfícies

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
    
    sup = pygame.Surface((200, 200)) #definindo sueprficie
    sup.fill(cor_azul) #superfície sup vai ser rpeenchida com essa cor
    
    sup2 = pygame.Surface((100,100))
    sup2.fill(cor_verde)

    sair = False
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
        relogio.tick(27) #atualizando de 27 quadros por segundo
        tela.fill(cor_branca) #trabalhando com o fundo/preenchimentl, valor hexadecimal vai dar essa cor
        tela.blit(sup, [50, 50]) #chamando superfície pela variavel e depois pela posição no cartesiano
        tela.blit(sup2, [70,70])
        pygame.display.update() #atualização na tela  tempo todo
    pygame.quit()
main() 

#criando eventos de clique e outros objetos

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
            """
            if event.type == pygame.MOUSEBUTTONDOWN: #criando evento quando clica com mouse
                 ret = ret.move(10, 10) #a cada clique ele se move 10 pixeis nessa direção de x e y (diagonal ifnerior)
            if event.type == pygame.MOUSEMOTION:
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
        (ret.left, ret.top) = pygame.mouse.get_pos() #esse evtno captura posição do mouse e parte esq e direita fica associada ao mouse
        ret.left -= ret.width/2 #esquerda vai ficar sempre no centro
        ret.top -= ret.height/2 
        pygame.draw.rect(tela, cor_vermelha, ret) #para fazer o retangulo la ret na tela
        pygame.display.update() #atualização na tela  tempo todo
  
    pygame.quit()
main() 


#movimentando objeto com o mouse e adicionando o clique tambem e colisões

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

        pygame.draw.rect(tela, cor_vermelha, ret) #para fazer o retangulo la ret na tela
        pygame.draw.rect(tela, cor_rosa, ret)
        pygame.display.update() #atualização na tela  tempo todo
  
    pygame.quit()
main() 


#colocar texto na tela

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
            text = fonte_perdeu.render('COLIDIU', 1, (255,255,255))) #render faz aparecer na tela 
            tela.blit(text, (150,150)) #usa blit pra jogar obj na tela entao vamos jogar o texto e poe posição
        
        pygame.draw.rect(tela, cor_vermelha, ret) #para fazer o retangulo la ret na tela
        pygame.draw.rect(tela, cor_rosa, ret)
        pygame.display.update() #atualização na tela  tempo todo
  
    pygame.quit()
main() 

#colocar audio

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

    audio_explosao = pygame.mixer.Sound('explosion.wav') #adiciona sons e poe arquivo dentro dos ()


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
            text = fonte_perdeu.render('COLIDIU', 1, (255,255,255))) #render faz aparecer na tela 
            audio_explosao.play() #executa o audio com colisão
            audio_explosao.set_volume(0.5) #define volume, maior eh 1 e menor eh 0
            tela.blit(text, (150,150)) #usa blit pra jogar obj na tela entao vamos jogar o texto e poe posição


        pygame.draw.rect(tela, cor_vermelha, ret) #para fazer o retangulo la ret na tela
        pygame.draw.rect(tela, cor_rosa, ret)
        pygame.display.update() #atualização na tela  tempo todo
  
    pygame.quit()
main() 

#exemplo de jogo

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

#inflando

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
            text = fonte_perdeu.render('COLIDIU', 1, (255,255,255))) #render faz aparecer na tela 
            tela.blit(text, (150,150)) #usa blit pra jogar obj na tela entao vamos jogar o texto e poe posição
        
        pygame.draw.rect(tela, cor_vermelha, ret) #para fazer o retangulo la ret na tela
        pygame.draw.rect(tela, cor_rosa, ret)
        pygame.display.update() #atualização na tela  tempo todo
  
    pygame.quit()
main() 

#inflando

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

    audio_explosao = pygame.mixer.Sound('explosion.wav') #adiciona sons e poe arquivo dentro dos ()


    sair = False
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ret.collidirect (ret2):
                    ret2.height = 0
                    ret2. width = 0
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


        relogio.tick(27) 
        tela.fill(cor_branca) 
        tela.blit(sup, [50, 50]) 
        tela.blit(sup2, [70,70])
        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos() 
        ret.left -= ret.width/2 
        ret.top -= ret.height/2 

        '''if ret.colliderect(ret2): 
            ret2.inflate_ip(3,3) #vai inflar
            (ret.left, ret.top) = (xant, yant)
            #text = fonte_perdeu.render('COLIDIU', 1, (255,255,255))) 
            #audio_explosao.play() 
            #audio_explosao.set_volume(0.5) 
            #tela.blit(text, (150,150)) '''


        pygame.draw.rect(tela, cor_vermelha, ret) 
        pygame.draw.rect(tela, cor_rosa, ret)
        pygame.display.update() 
  
    pygame.quit()
main() 

#random

import pygame
import random
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

    sup = pygame.Surface((600, 600)) #definindo sueprficie
    sup.fill(cor_azul) #superfície sup vai ser rpeenchida com essa cor
    
    sup2 = pygame.Surface((100,100))
    sup2.fill(cor_verde)

    ret = pygame.Rect(10, 10, 45, 45)
    ret2 = pygame.Rect (50, 50, 80, 50)

    pygame.font.init() #iniciar fonte

    font_padrao = pygame.font.get_default_font() #define variavel de texto com fonte padrão
    fonte_perdeu = pygame.font.SysFont(font_padrao,45)
    fonte_ganhou = pygame.font.SysFont(font_padrao,30)
    texto = pygame.font.SysFont("Arial", 30, True, False)

    audio_explosao = pygame.mixer.Sound('explosion.wav') #adiciona sons e poe arquivo dentro dos ()
    listaret = [] #cada vez que cria ret joga dentro da lista com uma naoseioq que ele guarda as info 
    #e depois pode fazzer teste dde colisão com a lista

    for x in range (15): #vai repetir instrução 15 vezes
        h = random.randrange (20,60)
        w = random.randrange(15,45)
        x = random.randrange(280)
        y = random.randrange(280)
        listaret.append(pygame.Rect(x, y, w, h)) #coloca info dentro da lista

    sair = False
    while sair != True:

        for rets in listaret: #rets eh cada item da lista
            pygame.draw.rect(sup, cor_verde, rets) #vai ser desenhado na sup com a cor e qual objeto que vai desenhar

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ret.collidirect (ret2):
                    ret2.height = 0
                    ret2. width = 0
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


        relogio.tick(27) 
        tela.fill(cor_branca) 
        tela.blit(sup, [0, 0]) 
        tela.blit(sup2, [70,70])
        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos() 
        ret.left -= ret.width/2 
        ret.top -= ret.height/2 

        '''if ret.colliderect(ret2): 
            ret2.inflate_ip(3,3) #vai inflar
            (ret.left, ret.top) = (xant, yant)
            #text = fonte_perdeu.render('COLIDIU', 1, (255,255,255))) 
            #audio_explosao.play() 
            #audio_explosao.set_volume(0.5) 
            #tela.blit(text, (150,150)) '''

        segundos = pygame.time.get_ticks()/1000
        segundos = str(segundos) #convertemos pra string pra ir pra texto e poder usar
        contador = texto.render(segundo, 0, cor_branca)
        sup.blit(contador, (300,10))
        #print(segundos)#mostra milisegundos na tela e por isso dividimos por 1000
        pygame.draw.rect(tela, cor_vermelha, ret) 
        pygame.draw.rect(tela, cor_rosa, ret)
        pygame.display.update() 
  
    pygame.quit()
main() 

#trabalhando com imagens

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
    
    sair = False
    while sair != True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            
            #if event.type == pygame.MOUSEBUTTONDOWN:
              
        tela.fill(cor_branca) #sempre cuidar com a ordem das coisas que poe na tela
        tela.blit(imagem, (x,y)) #poe posição da tua imagem e faz aparecer
        
        (x,y) = pygame.mouse.get_pos() #variavel receb posição do mouse
        pygame.draw.rect(tela, cor_vermelha, ret)

        relogio.tick(30)
        pygame.display.update() 
  
    pygame.quit()
main() 

#COLISÃO COM IMAGENS E VELOCIDADE

import pygame
import random
def main():
    #as definições dos objetos (variaveis)
    pygame.init()
    tela = pygame.display.set_mode([300, 300])
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
    sprite = pygame.sprite.Sprite()
    sprite.image = imagem #o sprite recebe a imagem
    sprite.rect = imagem.get_rect() #cria uma area retangular em volta da imagem que compara a colisão da area com outro obj
    #tipo retangulo invisivel
    sprite.rect.top = 50 
    sprite.rect.left = 50

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
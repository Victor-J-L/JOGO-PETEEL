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
        contador = texto.render(segundos, 0, cor_branca)
        sup.blit(contador, (300,10))
        #print(segundos)#mostra milisegundos na tela e por isso dividimos por 1000
        pygame.draw.rect(tela, cor_vermelha, ret) 
        pygame.draw.rect(tela, cor_rosa, ret)
        pygame.display.update() 
  
    pygame.quit()
main() 
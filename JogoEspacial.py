#Jogo Espacial 
import pygame
import random

class Ret(object):
    def __init__(self, numeroinicial):
        self.lista = []
        for x in range(numeroinicial):
            leftrandom = random.randrange(2, 560)
            toprandom = random.randrange(-580, -10)
            width = random.randrange(10, 30)
            height = random.randrange(15, 30)
            self.lista.append(pygame.Rect(leftrandom, toprandom, width, height))

    def mover(self):
        for retangulo in self.lista:
            retangulo.move_ip(0, 2)
    
    def cor(self, superficie):
        for retangulo in self.lista:
            pygame.draw.rect(superficie, (165, 214, 254), retangulo)
    
    def recriar(self):
         for x in range(len(self.lista)):
            if self.lista[x].top > 481:
                leftrandom = random.randrange(2, 560)
                toprandom = random.randrange(-580, -10)
                width = random.randrange(10, 30)
                height = random.randrange(15, 30)
                self.lista[x] = (pygame.Rect(leftrandom, toprandom, width, height))

class Player(pygame.sprite.Sprite):
    def __init__(self, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = (100,200)
    
    def mover(self, vx, vy):
        self.rect.move_ip(vx,vy)

    def update (self, sup):
        sup.blit(self.imagem, self.rect)

def main ():
    import pygame
    pygame.init()
    
    #Variaveis
    tela = pygame.display.set_mode((480,300))
    sair = False
    relogio = pygame.time.Clock()
    relogio.tick(50)
    tela.fill((200, 200, 200))
    vx, vy = 0,0
    velocidade = 8
    leftpress, rightpress, uppress, downpress = False, False, False, False

    #Imagens
    img_nave = pygame.image.load("nave.png").convert_alpha()
    jogador = Player(img_nave)
    fundo = pygame.image.load("fundo.png").convert_alpha()

    #Objetos
    ret= Ret(30)


    while sair != True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                sair = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leftpress = True
                    vx = -velocidade
                if event.key == pygame.K_RIGHT:
                    rightpress = True
                    vx = velocidade
                if event.key == pygame.K_DOWN:
                    downpress = True
                    vy = velocidade
                if event.key == pygame.K_UP:
                    uppress = True
                    vy = -velocidade
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    leftpress = False
                    if rightpress: vx = velocidade
                    else: vx = 0
                if event.key == pygame.K_RIGHT:
                    rightpress = False
                    if leftpress: vx = -velocidade
                    else: vx = 0
                    vx = 0
                if event.key == pygame.K_DOWN:
                    downpress = False
                    if uppress: vy = -velocidade
                    else: vy = 0
                if event.key == pygame.K_UP:
                    uppress = False
                    if downpress: vy = velocidade
                    else: vy = 0
                

                
        relogio.tick(50)
        tela.blit(fundo, (0, 0))
        ret.mover()
        ret.cor(tela)
        ret.recriar()
        jogador.update(tela)
        jogador.mover(vx,vy)
        

        pygame.display.update()
main()






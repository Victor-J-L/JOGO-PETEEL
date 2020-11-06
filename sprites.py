import pygame
import random
#from settings import *
#from random import choice, randrange
vec = pygame.math.Vector2

class Personagem1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/personagem/personagem1frente.png")
        self.rect = self.image.get_rect()
        self.rect.top = 475
        self.rect.left = 575
        self.rect.left = 200
        self.rect.right = 210

class Personagem2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/personagem/personagem2frente.png")
        self.rect = self.image.get_rect()
        self.rect.top = 475
        self.rect.left = 575
        self.rect.left = 200
        self.rect.right = 405

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/personagem/personagem1frente_min.png")
        self.rect = self.image.get_rect()
        self.rect.center= (400,530)
        self.rect.top = 800
        self.rect.left = 228
        self.rect.right = 228
        self.pos = vec(400,530)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -0,5
        if keys[pygame.K_RIGHT]:
            self.acc.x = 0,5

        # apply friction
        self.acc += self.vel * (-0.12)
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > 500:
            self.pos.x = 0
            self.rect.left = self.pos.x
        if self.pos.x < -10:
            self.pos.x = 500

        self.rect.center = self.pos

                  
class Selecao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/personagem/selecao.png")
        self.rect = self.image.get_rect()
        self.rect.top = 470
        self.rect.right = 800

class Plataformas(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Primeira Fase/plataforma1.png")
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

class PlataformaFinal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Primeira Fase/plataformafinal.png")
        self.rect = self.image.get_rect()
        self.rect.left = 5
        self.rect.top = -2400

class Paginainicial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Página inicial/paginainicial2.png")
        self.rect = self.image.get_rect()
        self.rect.top = -26
        self.rect.left = -16

class Botaoplay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Página inicial/play.png")
        self.rect = self.image.get_rect()
        self.rect.top = 342
        self.rect.bottom = 391
        self.rect.left = 199
        self.rect.right = 314

class Bolinha1(pygame.sprite.Sprite): #ensino
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Primeira Fase/ensino.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.uniform(100,400)
        self.rect.y = random.uniform(-400,-100)
        #self.pos = (self.rect.x, self.rect.y)
        self.pos = vec(228, 720)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

class Bolinha2(pygame.sprite.Sprite): #pesquisa
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Primeira Fase/pesquisa.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.uniform(100,400)
        self.rect.y = random.uniform(-600,-1000)
        #self.pos = (self.rect.x, self.rect.y)
        self.pos = vec(228, 720)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

class Bolinha3(pygame.sprite.Sprite): #extensão
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Primeira Fase/extensão.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.uniform(100,400)
        self.rect.y = random.uniform(-1200,-1500)
        #self.pos = (self.rect.x, self.rect.y)
        self.pos = vec(228, 720)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

#screen.blit(player.image, (x,y))

class Iconefinal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Primeira Fase/iconefinal.png")
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y =  -2505

cor_azul = (181,244,253)

class Chao(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Primeira Fase/chao.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class FundoInicial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Primeira Fase/fundo123desfocado.png")
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = 0

class BotaoGameOver(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Game Over/botaogameover.png")
        self.rect = self.image.get_rect()
        self.rect.top = 330 
        self.rect.left = 800

class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Game Over/gameover.png")
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = 800
class Transicao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Primeira Fase/transição.png")
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = 800

class Botaot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Primeira Fase/playtransição.png")
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = 800
#grupos 

plataformas = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
chao_sprite = pygame.sprite.Group()
bolinhas = pygame.sprite.Group()
iconegrupo = pygame.sprite.Group()
gameovergrupo = pygame.sprite.Group()
fundoinicialgrupo = pygame.sprite.Group()
personagemgrupo = pygame.sprite.Group()
transicaogrupo = pygame.sprite.Group()
#CORES
cor_azul = (181,244,253)

#Variaveis
pag_inicial= Paginainicial()
all_sprites.add(pag_inicial)
botaoplay= Botaoplay()
all_sprites.add(botaoplay)
personagem= Personagem()
personagemgrupo.add(personagem)
personagem1= Personagem1()
all_sprites.add(personagem1)
personagem2= Personagem2()
all_sprites.add(personagem2)
selecao= Selecao()
all_sprites.add(selecao)
transição = Transicao()
transicaogrupo.add(transição)

botaot = Botaot()
transicaogrupo.add(botaot)

ensino= Bolinha1()
#all_sprites.add(ensino)
bolinhas.add(ensino)
pesquisa = Bolinha2()
#all_sprites.add(pesquisa)
bolinhas.add(pesquisa)
extensao = Bolinha3()
#all_sprites.add(extensao)
bolinhas.add(extensao)


iconefinal= Iconefinal()
iconegrupo.add(iconefinal)


#Lista de Plataformas
p0 = Chao(-15, 544)
plataformas.add(p0)

p1 = Plataformas(250, 255)
plataformas.add(p1)

p2 = Plataformas(10, 395)
plataformas.add(p2)

p3 = Plataformas(10, 125)
plataformas.add(p3)

p4 = Plataformas(235, -10)
plataformas.add(p4)

pfinal = PlataformaFinal()
plataformas.add(pfinal)

Plataforma_lista = [p0, p1, p2, p3, p4]

#Fundo Inicial
fundoinicial=FundoInicial()
fundoinicialgrupo.add(fundoinicial)

#GameOver
gameover = GameOver()
gameovergrupo.add(gameover)
botaogameover = BotaoGameOver()
gameovergrupo.add(botaogameover)

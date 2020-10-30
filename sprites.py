import pygame
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
        self.rect.center= (400, 805)
        self.rect.top = 800
        self.rect.left = 228
        self.rect.right = 228
        self.pos = vec(400, 805)
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

class Bolinha(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Primeira Fase/bolinha.png")
        self.rect = self.image.get_rect()
        self.rect.top = 120
        self.rect.bottom = 200
        self.rect.left = 250
        self.rect.right = 300

class Iconefinal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Primeira Fase/iconefinal.png")
        self.rect = self.image.get_rect()
        self.rect.top = 120
        self.rect.bottom = 200
        self.rect.left = 280
        self.rect.right = 300

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

#grupos 

plataformas = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
chao_sprite = pygame.sprite.Group()


#CORES
cor_azul = (181,244,253)

#Variaveis
pag_inicial= Paginainicial()
all_sprites.add(pag_inicial)
botaoplay= Botaoplay()
all_sprites.add(botaoplay)
personagem= Personagem()
all_sprites.add(personagem)
personagem1= Personagem1()
all_sprites.add(personagem1)
personagem2= Personagem2()
all_sprites.add(personagem2)
selecao= Selecao()
all_sprites.add(selecao)
iconefinal= Iconefinal()
#all_sprites.add(iconefinal)
bolinha= Bolinha()
#all_sprites.add(bolinha)

#Lista de Plataformas

Plataforma_lista = [ (800, 400), (-15, 544), (250, 250), (10, 400), (10, 100)]
p00 = Plataformas(800, 400)
plataformas.add(p00)

p0 = Chao(-15, 544)
plataformas.add(p0)

p1 = Plataformas(250, 250)
plataformas.add(p1)

p2 = Plataformas(10, 400)
plataformas.add(p2)

p3 = Plataformas(10, 100)
plataformas.add(p3)

# o chão

ochao = Chao(400, 805)

#Fundo Inicial
fundoinicial=FundoInicial()
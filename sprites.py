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
        self.p11 = False
        self.p22 = False
        self.p10 = True

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
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

class PlataformaFinal(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
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
        self.rect.left = 350
        self.rect.right = 370

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

class Iconefinal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Primeira Fase/iconefinal.png")
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y =  -2555

class Icone2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Primeira Fase/iconefinal.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y =  -2505

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

class Transicao2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Segunda Fase/transiçãof2.png")
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

class Valorbrio(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Segunda Fase/brio.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = random.uniform(-400,-100)
        self.pos = vec(228, 720)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

class Valorcapaci(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Segunda Fase/capacitação.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = random.uniform(-400,-100)
        self.pos = vec(228, 720)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

class Valorhumil(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Segunda Fase/humildade.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = random.uniform(-400,-100)
        self.pos = vec(228, 720)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

class Valorcomprom(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Segunda Fase/comprometimento.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = random.uniform(-400,-100)
        self.pos = vec(228, 720)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

class Valoruniao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Segunda Fase/UNIÃO.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = random.uniform(-400,-100)
        self.pos = vec(228, 720)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

class Capacete(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Terceira Fase/cpaceteespacial.png")
        self.rect = self.image.get_rect()
        self.rect.center= (407,511.5)
        self.pos = vec(407,511.5)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

class Inimigos3(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.pos = vec(x,y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

class Bolinha4(pygame.sprite.Sprite): 
    def __init__(self, image, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = 2000
        self.rect.y = y
        #self.pos = vec(228, 720)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

class Inimigos4(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.pos = vec(x,y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

class Personagemfinal(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y


class Personagensfinais(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.jaaconteceu = False

class FalaExpetiano(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.jaaconteceu = False

class Botaoexpetiano(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Quinta Fase/botaoexpetianos.png")
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = 800

#Variaveis
cor_azul = (181,244,253)
#grupos 

plataformas = pygame.sprite.Group()
platfinal = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
chao_sprite = pygame.sprite.Group()
bolinhas = pygame.sprite.Group()
iconegrupo = pygame.sprite.Group()
gameovergrupo = pygame.sprite.Group()
fundoinicialgrupo = pygame.sprite.Group()
personagemgrupo = pygame.sprite.Group()
transicaogrupo = pygame.sprite.Group()
valoresgrupo = pygame.sprite.Group()
iconef2grupo = pygame.sprite.Group()
transicao2grupo = pygame.sprite.Group()
iconef3grupo = pygame.sprite.Group()
transicao3grupo = pygame.sprite.Group()
inimigos3grupo = pygame.sprite.Group()
transicao41grupo = pygame.sprite.Group()
transicao42grupo = pygame.sprite.Group()
iconef4grupo = pygame.sprite.Group()
iconef5grupo = pygame.sprite.Group()
bolinhas4grupo = pygame.sprite.Group()
inimigos4grupo = pygame.sprite.Group()
transicaofinal = pygame.sprite.Group()
expetianomarialauragroup=pygame.sprite.Group()
expetianojoaogroup=pygame.sprite.Group()
expetianoarthurgroup=pygame.sprite.Group()
expetianoeduardagroup=pygame.sprite.Group()
falaexpetiano=pygame.sprite.Group()
botaoexpetianosgroup = pygame.sprite.Group()


#CORES
cor_azul = (181,244,253)

#Variaveis
pag_inicial= Paginainicial()
all_sprites.add(pag_inicial)
botaoplay= Botaoplay()
all_sprites.add(botaoplay)
personagem = Personagem()
personagemgrupo.add(personagem)
personagem1= Personagem1()
all_sprites.add(personagem1)
personagem2= Personagem2()
all_sprites.add(personagem2)
selecao= Selecao()
all_sprites.add(selecao)
transição1 = Transicao()
transicaogrupo.add(transição1)

botaot = Botaot()
transicaogrupo.add(botaot)

sobre = Botaoplay()
sobre.image = pygame.image.load("Imagens/Página Inicial/sobre.png")
sobre.rect.top = 342
sobre.rect.bottom = 400
sobre.rect.left = 150
sobre.rect.right = 250
all_sprites.add(sobre)


#bolinhas primeira fase

ensino= Bolinha1()
bolinhas.add(ensino)
pesquisa = Bolinha2()
bolinhas.add(pesquisa)
extensao = Bolinha3()
bolinhas.add(extensao)

iconefinal= Iconefinal()
iconegrupo.add(iconefinal)

#segunda fase

humildade = Valorhumil()
valoresgrupo.add(humildade)
uniao = Valoruniao()
valoresgrupo.add(uniao)
comprometimento = Valorcomprom()
valoresgrupo.add(comprometimento)
capacitacao = Valorcapaci()
valoresgrupo.add(capacitacao)
brio = Valorbrio()
valoresgrupo.add(brio)

iconef2 = Icone2()
iconef2grupo.add(iconef2)

transição2 = Transicao2()
transicao2grupo.add(transição2)
botaot2 = Botaot()
transicao2grupo.add(botaot2)

#terceira fase

transição3 = Transicao()
transição3.image = pygame.image.load("Imagens/Terceira Fase/transição3.png")
transicao3grupo.add(transição3)
iconef3 = Icone2()
iconef3grupo.add(iconef3)
botaot3 = Botaot()
transicao3grupo.add(botaot3)

interromper = Inimigos3(5, 2000, "Imagens/Terceira Fase/interromper.png") #dai quando clica no botao muda o y pro lugar certo deles"
falarmal = Inimigos3(450, 2000, "Imagens/Terceira Fase/falarmal.png")
falardemais = Inimigos3(5, 2000, "Imagens/Terceira Fase/falardemais.png")
desrespeitar = Inimigos3(450, 2000, "Imagens/Terceira Fase/desrespeitar.png")
mentefechada  = Inimigos3(5, 2000, "Imagens/Terceira Fase/mentefechada.png")
inimigos3grupo.add(interromper, falarmal, falardemais, desrespeitar, mentefechada)

#quarta fase

transição41 = Transicao()
transição42 = Transicao()
transição41.image = pygame.image.load("Imagens/Quarta Fase/transição41.png")
transição42.image = pygame.image.load("Imagens/Quarta Fase/transição42.png")
transicao41grupo.add(transição41)
transicao42grupo.add(transição42)
abrir = Botaot()
abrir.image = pygame.image.load("Imagens/Quarta Fase/abrir.png")
transicao41grupo.add(abrir)
iconef4 = Icone2()
iconef4grupo.add(iconef4)
botaot4 = Botaot()
botaot4.image = pygame.image.load("Imagens/Quarta Fase/agora.png")
transicao42grupo.add(botaot4)

coo = Bolinha4("Imagens/Quarta Fase/obstáculos/COO.png",random.uniform(400,200))
sec = Bolinha4("Imagens/Quarta Fase/obstáculos/SEC.png",random.uniform(-400,-200))
tes = Bolinha4("Imagens/Quarta Fase/obstáculos/TES.png",random.uniform(-600,-400))
pep = Bolinha4("Imagens/Quarta Fase/obstáculos/PEP.png",random.uniform(-800,-600))
mkt = Bolinha4("Imagens/Quarta Fase/obstáculos/MKT.png",random.uniform(-1000,-800))
evt = Bolinha4("Imagens/Quarta Fase/obstáculos/EVT.png",random.uniform(-1200,-1000))
inter = Bolinha4("Imagens/Quarta Fase/obstáculos/INTERPET.png",random.uniform(-1400,-1200))
qld = Bolinha4("Imagens/Quarta Fase/obstáculos/qld.png",random.uniform(-1600,-1400))

bolinhas4grupo.add(coo, tes, pep, sec, mkt, evt, inter, qld)

respostas = Inimigos4(5, 2000, "Imagens/Quarta Fase/RESPOSTAS.png") #dai quando clica no botao muda o y pro lugar certo deles"
falta = Inimigos4(450, 2000, "Imagens/Quarta Fase/FALTA.png")
irdes = Inimigos4(5, 2000, "Imagens/Quarta Fase/irdespreparado.png")
mentir = Inimigos4(450, 2000, "Imagens/Quarta Fase/mentir.png")
preguiça  = Inimigos4(5, 2000, "Imagens/Quarta Fase/TERPREGUIÇA.png")
inimigos4grupo.add(respostas, falta, irdes, mentir, preguiça)

#Quinta Fase

iconef5 = Icone2()
iconef5grupo.add(iconef5)
transiçãofinal = Transicao()
transiçãofinal.image = pygame.image.load("Imagens/Quinta Fase/transiçãofinal-01.png")
transicaofinal.add(transiçãofinal)
personagemfinal = Personagemfinal(800, 800, "Imagens/Quinta Fase/personagemfinal.png")
transicaofinal.add(personagemfinal)
falamarialaura= FalaExpetiano(800, 87.679,"Imagens/Quinta Fase/expetiano_marialaura.png" )
falaexpetiano.add(falamarialaura)
falaeduarda= FalaExpetiano(800, 87.679,"Imagens/Quinta Fase/expetiano_eduarda.png" )
falaexpetiano.add(falaeduarda)
falaarthur=FalaExpetiano(800, 87.679,"Imagens/Quinta Fase/expetiano_arthur.png" )
falaexpetiano.add(falaarthur)
falajoao=FalaExpetiano(800, 87.679,"Imagens/Quinta Fase/expetiano_joao.png" )
falaexpetiano.add(falajoao)
botaoexpetianos = Botaoexpetiano()
botaoexpetianosgroup.add(botaoexpetianos)
personagemarthur = Personagensfinais(800,-450,"Imagens/Quinta Fase/Expetianoarthur.png")
expetianoarthurgroup.add(personagemarthur)
personagemjoao = Personagensfinais(800,-950,"Imagens/Quinta Fase/Expetianojoao.png")
expetianojoaogroup.add(personagemjoao)
personagemmarialaura = Personagensfinais(800,-1450,"Imagens/Quinta Fase/Expetianomarialaura.png")
expetianomarialauragroup.add(personagemmarialaura)
personagemeduarda = Personagensfinais(800,-1950,"Imagens/Quinta Fase/Expetianoeduarda.png")
expetianoeduardagroup.add(personagemeduarda)

#Lista de Plataformas
p0 = Chao(-15, 544)
plataformas.add(p0)

p1 = Plataformas(250, 255, "Imagens/Primeira Fase/plataforma1.png")
plataformas.add(p1)

p2 = Plataformas(10, 395, "Imagens/Primeira Fase/plataforma1.png")
plataformas.add(p2)

p3 = Plataformas(10, 120, "Imagens/Primeira Fase/plataforma1.png")
plataformas.add(p3)

p4 = Plataformas(235, -30, "Imagens/Primeira Fase/plataforma1.png")
plataformas.add(p4)

pfinal1 = PlataformaFinal(5, -2450, "Imagens/Primeira Fase/plataformafinal.png")
platfinal.add(pfinal1)

pfinal2 = PlataformaFinal(800, -2550, "Imagens/Segunda Fase/plataformafinal2.png")
platfinal.add(pfinal2)

pfinal3 = PlataformaFinal(800, -2450, "Imagens/Terceira Fase/plataformafinal3.png")
platfinal.add(pfinal3) 

pfinal4 = PlataformaFinal(800, -2450, "Imagens/Quarta Fase/plataformafinal4.png")
platfinal.add(pfinal4)

pfinal5 = PlataformaFinal(800, -2450, "Imagens/Quinta Fase/plataformafinal5.png")
platfinal.add(pfinal5)

capacete = Capacete()
"""all_sprites.add(capacete)"""



Plataforma_lista = [p0, p1, p2, p3, p4]

#Fundo Inicial
fundoinicial=FundoInicial()
fundoinicialgrupo.add(fundoinicial)

#GameOver
gameover = GameOver()
gameovergrupo.add(gameover)
botaogameover = BotaoGameOver()
gameovergrupo.add(botaogameover)

#self.rect.center= (407,511.5)
#self.pos = vec(407,511.5)
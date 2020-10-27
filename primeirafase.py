import pygame 
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
        self.rect.center= (400,100)
        self.rect.top = 800
        self.rect.left = 228
        self.rect.right = 228
        self.pos = vec(800,800)
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
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagens/Primeira Fase/plataforma.png")
        self.rect = self.image.get_rect()
        self.rect.top = 200
        self.rect.left = 200

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


def main():

    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode([500,650])
    pygame.display.set_caption("Jogo PETEEL")
    relogio = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    fundo = pygame.image.load("Imagens/Primeira Fase/fundo123desfocado.png")

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
    plataforma1 = Plataformas()
    #all_sprites.add(plataforma1)
    iconefinal= Iconefinal()
    #all_sprites.add(iconefinal)
    bolinha= Bolinha()
    #all_sprites.add(bolinha)

    sair = False
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
        
        #Parametros
        relogio.tick(30)
        tela.fill(cor_azul)
        (xmouse, ymouse) = pygame.mouse.get_pos()

        #Código Página inicial
        if xmouse >= personagem1.rect.left and xmouse <= personagem1.rect.right and ymouse <= personagem1.rect.bottom and ymouse >= personagem1.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                personagem.image = pygame.image.load("Imagens/personagem/personagem1frente_min.png") #personagem1frente
                personagem.rect = personagem.image.get_rect()
                personagem.rect.center = (800,800)
                selecao.rect.right = 217

        if xmouse >= personagem2.rect.left and xmouse <= personagem2.rect.right and ymouse <= personagem2.rect.bottom and ymouse >= personagem2.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                personagem.image = pygame.image.load("Imagens/personagem/personagem2frente_min.png") #personagem1frente
                personagem.rect = personagem.image.get_rect()
                personagem.rect.center=(800,800)
                selecao.rect.right = 412
            
        if xmouse >= botaoplay.rect.left and xmouse <= botaoplay.rect.right and ymouse <= 351 and ymouse >= 295:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pag_inicial.rect.left = 800
                botaoplay.rect.left = 800
                personagem1.rect.left = 800
                personagem2.rect.left = 800
                personagem.rect.center = (228,200)
                personagem.pos = vec(228,200)
                selecao.rect.right = 800
                fundo = pygame.image.load("Imagens/Primeira Fase/fundo1_1.png")

       #Código Movimento do personagem
        personagem.acc = vec(0, 0.35)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            personagem.acc.x = -0.5

        if keys[pygame.K_RIGHT]:
            personagem.acc.x = 0.5
        
        personagem.acc.x += personagem.vel.x * (-0.12)
        personagem.vel += personagem.acc
        personagem.pos += personagem.vel + 0.5 * personagem.acc

        if personagem.pos.x > 500:
            personagem.pos.x = 0
        if personagem.pos.x < 0:
            personagem.pos.x = 500

        personagem.rect.center = personagem.pos

        
        #Desenhar
        tela.blit(fundo, (0,0))
        all_sprites.draw(tela)

        #Updates
        all_sprites.update        
        pygame.display.update() 

    pygame.quit() 
main()
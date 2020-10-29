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
        self.pos = vec(100,2000)
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


def main():

    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode([500,650])
    pygame.display.set_caption("Jogo PETEEL")
    relogio = pygame.time.Clock()
    fundo = pygame.image.load("Imagens/Primeira Fase/fundo123desfocado.png")

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

    p00 = Plataformas(100, 2005)
    plataformas.add(p00)

    p0 = Chao(-15, 544)
    plataformas.add(p0)

    p1 = Plataformas(250, 250)
    plataformas.add(p1)

    p2 = Plataformas(10, 400)
    plataformas.add(p2)

    p3 = Plataformas(10, 100)
    plataformas.add(p3)
    

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
                personagem.rect.midbottom = (800,800)
                selecao.rect.right = 217

        if xmouse >= personagem2.rect.left and xmouse <= personagem2.rect.right and ymouse <= personagem2.rect.bottom and ymouse >= personagem2.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                personagem.image = pygame.image.load("Imagens/personagem/personagem2frente_min.png") #personagem1frente
                personagem.rect = personagem.image.get_rect()
                personagem.rect.midbottom=(800,800)
                selecao.rect.right = 412
            
        if xmouse >= botaoplay.rect.left and xmouse <= botaoplay.rect.right and ymouse <= 351 and ymouse >= 295:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pag_inicial.rect.left = 800
                botaoplay.rect.left = 800
                personagem1.rect.left = 800
                personagem2.rect.left = 800
                personagem.rect.midbottom = (228,200)
                selecao.rect.right = 800
                fundo = pygame.image.load("Imagens/Primeira Fase/fundo1_1.png")
                personagem.pos = vec(400,530)

       #Código Movimento do personagem
        personagem.acc = vec(0, 1)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            personagem.acc.x = -0.9

        if keys[pygame.K_RIGHT]:
            personagem.acc.x = 0.9

        personagem.acc.x += personagem.vel.x * (-0.12)
        personagem.vel += personagem.acc
        personagem.pos += personagem.vel + 0.5 * personagem.acc


        if personagem.pos.x > 500:
            personagem.pos.x = 0
        if personagem.pos.x < 0:
            personagem.pos.x = 500

        personagem.rect.midbottom = personagem.pos

        #colisao

        if personagem.vel.y > 0.5:
            colisao_plataforma = pygame.sprite.spritecollide(personagem, plataformas, False)
            if colisao_plataforma:
                personagem.pos.y = colisao_plataforma[0].rect.top
                personagem.vel.y = 0

        #pulo
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        personagem.rect.x += 1
                        colisao_plataforma = pygame.sprite.spritecollide(personagem, plataformas, False)
                        personagem.rect.x -= 1
                        if  colisao_plataforma:
                            personagem.vel.y = -18
                        personagem.rect.x += 1

                        
                        
        
        #Desenhar
        tela.blit(fundo, (0,0))
        chao_sprite.draw(tela)
        plataformas.draw(tela)
        all_sprites.draw(tela)

        #Updates
        all_sprites.update        
        pygame.display.update() 

    pygame.quit() 
main()
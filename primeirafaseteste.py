import pygame 
import random
from sprites import *
from os import path
import random
#from configuração import *
vec = pygame.math.Vector2


def main():

    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode([500,650])
    pygame.display.set_caption("Jogo PETEEL")
    relogio = pygame.time.Clock()
    fundo = pygame.image.load("Imagens/Primeira Fase/fundo123desfocado.png")
    

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
                fundoinicial.rect.left = 800 
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

        if personagem.vel.y > 0.9:
            colisao_plataforma = pygame.sprite.spritecollide(personagem, plataformas, False)
            if colisao_plataforma:
                personagem.pos.y = colisao_plataforma[0].rect.top
                personagem.vel.y = 0

        colisao_bolinhas = pygame.sprite.spritecollide(personagem, bolinhas, True)
        


        #pulo
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    personagem.rect.x += 1
                    colisao_plataforma = pygame.sprite.spritecollide(personagem, plataformas, False)
                    personagem.rect.x -= 1
                    if  colisao_plataforma:
                        personagem.vel.y = -18
                    
        
         # Scrolling
        if personagem.rect.top <= 250:
            personagem.pos.y += abs(personagem.vel.y)
            ensino.pos.y += abs(ensino.vel.y)
            pesquisa.pos.y += abs(pesquisa.vel.y)
            extensao.pos.y += abs(extensao.vel.y)
            for plat in plataformas:
                plat.rect.y += abs(personagem.vel.y)
                if plat.rect.top >= 850:
                    plat.kill()

        # spawn new platforms to keep same average number
        while len(plataformas) < 6:
            p = Plataformas(random.randrange(5, 300),
                         random.randrange(-92, -88))
            plataformas.add(p)
            
        #Desenhar
        tela.blit(fundo, (0,0))
        plataformas.draw(tela)
        all_sprites.draw(tela)
        tela.blit(fundoinicial.image, fundoinicial.rect)
        all_sprites.draw(tela)
    

        #Updates
        all_sprites.update        
        pygame.display.update() 

    pygame.quit() 
main()
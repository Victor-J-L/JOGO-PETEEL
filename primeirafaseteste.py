import pygame 
import random
from sprites import *
from os import path

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
                selecao.rect.right = 800
                fundo = pygame.image.load("Imagens/Primeira Fase/fundo1_1.png")
                fundoinicial.rect.left = 800 

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

        if personagem.vel.y > 0.9:
            colisao_platfinal = pygame.sprite.spritecollide(personagem, platfinal, False)
            if colisao_platfinal:
                personagem.pos.y = colisao_platfinal[0].rect.top
                personagem.vel.y = 0

        colisao_bolinhas = pygame.sprite.spritecollide(personagem, bolinhas, True)
        colisao_valores = pygame.sprite.spritecollide(personagem, valoresgrupo, True)
        colisao_icone1 = pygame.sprite.spritecollide(personagem, iconegrupo, False)
        if colisao_icone1:
            transição1.rect.left = 0
            botaot.rect.left = 325
            botaot.rect.top = 585

        colisao_icone2 = pygame.sprite.spritecollide(personagem, iconef2grupo, False)
        if colisao_icone2:
            transição2.rect.left = 0


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
            for bol in bolinhas:
                bol.rect.y += abs(personagem.vel.y)
            for val in valoresgrupo:
                val.rect.y += abs(personagem.vel.y)
            for ic2 in iconef2grupo:
                ic2.rect.y += abs(personagem.vel.y) 
            for ic in iconegrupo:
                ic.rect.y += abs(personagem.vel.y)
            for platfin in platfinal:
                platfin.rect.y += abs(personagem.vel.y)
            for plat in plataformas:
                plat.rect.y += abs(personagem.vel.y)
                if plat.rect.top >= 650:
                    plat.kill()

        # spawn new platforms to keep same average number
        if pfinal1.rect.top <-100:
            while len(plataformas) < 6:
                p = Plataformas(random.randrange(5, 300),
                            random.randrange(-90, -88))
                plataformas.add(p)

        #Fase 2

        if xmouse >= botaot.rect.left and xmouse <= botaot.rect.right and ymouse <= botaot.rect.bottom and ymouse >= botaot.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                personagem.pos = vec(400,530)
                transição1.rect.left= 800
                botaot.rect.right = 800
                iconefinal.rect.x = 800
                pfinal1.rect.top = -2400
                fundo = pygame.image.load("Imagens/Segunda Fase/fundo2.png")
                Plataformas.image = pygame.image.load("Imagens/Segunda Fase/plataforma2.png")
                for plat in plataformas: 
                    plat.kill()   
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
                

                brio.rect.x = random.uniform(100,400)
                brio.rect.y = random.uniform(-400,-100)

                capacitacao.rect.x = random.uniform(100, 400)
                capacitacao.rect.y = random.uniform(-600, -1000)

                humildade.rect.x = random.uniform(100,400)
                humildade.rect.y = random.uniform(-1200,-1500)

                uniao.rect.x = random.uniform(100,400)
                uniao.rect.y = random.uniform(-1700, -2000)

                comprometimento.rect.x = random.uniform(100,400)
                comprometimento.rect.y = random.uniform(-2200, -2500)

                iconef2.rect.x = 50
                iconef2.rect.y = -2505





        #Game Over

        if personagem.rect.top > 650:
            personagem.pos = vec(400,530)
            gameover.rect.left = 0
            botaogameover.rect.left = 199.62
            fundoinicial.rect.left = 0
            for plat in plataformas: 
                plat.kill()   
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
            ensino= Bolinha1()
            bolinhas.add(ensino)
            pesquisa = Bolinha2()
            bolinhas.add(pesquisa)
            extensao = Bolinha3()
            bolinhas.add(extensao)
            iconefinal.rect.y = -2505
            pfinal1.rect.top = -2400

        if xmouse >= botaogameover.rect.left and xmouse <= botaogameover.rect.right and ymouse <= botaogameover.rect.bottom and ymouse >= botaogameover.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pag_inicial.rect.left= -16
                botaoplay.rect.right = 314
                personagem1.rect.right = 210
                personagem2.rect.right = 405
                gameover.rect.left = 800
                botaogameover.rect.left = 800

            
            

        #Desenhar
        tela.blit(fundo, (0,0))
        plataformas.draw(tela)
        bolinhas.draw(tela)
        iconegrupo.draw(tela)
        platfinal.draw(tela)
        personagemgrupo.draw(tela)
        fundoinicialgrupo.draw(tela)
        all_sprites.draw(tela)
        tela.blit(fundoinicial.image, fundoinicial.rect)
        all_sprites.draw(tela)
        gameovergrupo.draw(tela)
        transicaogrupo.draw(tela)
        valoresgrupo.draw(tela)
        iconef2grupo.draw(tela)
        transicao2grupo.draw(tela)
    

        #Updates
        all_sprites.update        
        pygame.display.update() 



    pygame.quit() 
main()
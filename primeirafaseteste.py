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

        #CODIGO MOVIMENTO INIMIGOS DA FASE 3

        interromper.acc = vec(1, 0)
        #interromper.acc.x += interromper.vel.x * (-0.12)
        interromper.vel = vec(3,0)
        interromper.pos += interromper.vel + 0.5 * interromper.acc
        interromper.rect.midbottom = interromper.pos

        falarmal.acc = vec(-1, 0)
        #falarmal.acc.x += falarmal.vel.x * (-0.12)
        falarmal.vel = vec(-3,0)
        falarmal.pos += falarmal.vel - 0.5 * falarmal.acc
        falarmal.rect.midbottom = falarmal.pos

        gritar.acc = vec(1, 0)
        #gritar.acc.x += gritar.vel.x * (-0.12)
        gritar.vel = vec(3,0)
        gritar.pos += gritar.vel + 0.5 * gritar.acc
        gritar.rect.midbottom = gritar.pos

        desrespeitar.acc = vec(-1, 0)
        #desrespeitar.acc.x += desrespeitar.vel.x * (-0.12)
        desrespeitar.vel = vec(-3,0)
        desrespeitar.pos += desrespeitar.vel - 0.5 * desrespeitar.acc
        desrespeitar.rect.midbottom = desrespeitar.pos

        mentefechada.acc = vec(1, 0)
        #mentefechada.acc.x += mentefechada.vel.x * (-0.12)
        mentefechada.vel = vec(3,0)
        mentefechada.pos += mentefechada.vel + 0.5 * mentefechada.acc
        mentefechada.rect.midbottom = mentefechada.pos

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
            botaot2.rect.left = 325
            botaot2.rect.top = 585

        colisao_icone3 = pygame.sprite.spritecollide(personagem, iconef3grupo, False)
        if colisao_icone3:
            transição3.rect.left = 0
            botaot3.rect.left = 325
            botaot3.rect.top = 585

        colisao_inimigos3 = pygame.sprite.spritecollide(personagem, inimigos3grupo, False)
        if colisao_inimigos3:
            personagem.pos = vec(400,530)
            gameover.rect.left = 0
            botaogameover.rect.left = 182.985 
            fundoinicial.rect.left = 0
            for ini in inimigos3grupo:
                ini.kill()
            for plat in plataformas: 
                plat.kill()   


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
            for ic3 in iconef3grupo:
                ic3.rect.y += abs(personagem.vel.y) 
            for ini in inimigos3grupo:
                ini.pos.y += abs(personagem.vel.y)
            for ic in iconegrupo:
                ic.rect.y += abs(personagem.vel.y)
            for platfin in platfinal:
                platfin.rect.y += abs(personagem.vel.y)
            for plat in plataformas:
                plat.rect.y += abs(personagem.vel.y)
                if plat.rect.top >= 650:
                    plat.kill()

        # Spawn novas plat fase 1
        if pfinal1.rect.top <-100:
            while len(plataformas) < 6:
                if iconefinal.rect.x >= 0 and iconefinal.rect.x <= 500: 
                    p = Plataformas(random.randrange(5, 300),
                                random.randrange(-90, -88), "Imagens/Primeira Fase/plataforma1.png")
                    plataformas.add(p)
        if pfinal2.rect.top <-100 and pfinal2.rect.left <= 10:
            while len(plataformas) < 6:
                if iconef2.rect.x >= 0 and iconef2.rect.x <= 500: 
                    p = Plataformas(random.randrange(5, 300),
                                    random.randrange(-90, -88), "Imagens/Segunda Fase/plataforma2.png")
                    plataformas.add(p)
        if pfinal3.rect.top <-100 and pfinal3.rect.left <= 10:
            while len(plataformas) < 6:
                if iconef3.rect.x >= 0 and iconef3.rect.x <= 500: 
                    p = Plataformas(random.randrange(5, 300),
                                    random.randrange(-90, -88), "Imagens/Terceira Fase/plataforma3.png")
                    plataformas.add(p)
        

        #Fase 2

        if xmouse >= botaot.rect.left and xmouse <= botaot.rect.right and ymouse <= botaot.rect.bottom and ymouse >= botaot.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                personagem.pos = vec(400,530)
                transição1.rect.left= 800
                botaot.rect.right = 800
                iconefinal.rect.x = 800
                pfinal1.rect.left = 800
                pfinal2.rect.left = 5
                pfinal2.rect.top = -2400
                fundo = pygame.image.load("Imagens/Segunda Fase/fundo2.png")
                Plataformas.image = pygame.image.load("Imagens/Segunda Fase/plataforma2.png")
                for plat in plataformas: 
                    plat.kill()
                for bol in bolinhas : 
                    bol.kill()   
                p0 = Chao(-15, 544)
                plataformas.add(p0)
                p1 = Plataformas(250, 255, "Imagens/Segunda Fase/plataforma2.png")
                plataformas.add(p1)
                p2 = Plataformas(10, 395, "Imagens/Segunda Fase/plataforma2.png")
                plataformas.add(p2)
                p3 = Plataformas(10, 125, "Imagens/Segunda Fase/plataforma2.png")
                plataformas.add(p3)
                p4 = Plataformas(235, -10, "Imagens/Segunda Fase/plataforma2.png")
                plataformas.add(p4)

                p = Plataformas(random.randrange(5, 300),
                            random.randrange(-90, -88), "Imagens/Segunda Fase/plataforma2.png")
                

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

        # fase 3

        if xmouse >= botaot2.rect.left and xmouse <= botaot2.rect.right and ymouse <= botaot2.rect.bottom and ymouse >= botaot2.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                personagem.image = pygame.image.load("Imagens/personagem/personagem1minespaço.png")
                personagem.pos = vec(400,530)
                transição2.rect.left= 800
                botaot2.rect.right = 800
                iconef2.rect.x = 800
                iconef3.rect.x = 50
                iconef3.rect.y = -2505
                pfinal2.rect.left = 800
                pfinal3.rect.left = 5
                pfinal3.rect.top = -2400
                
                interromper.pos.y = -200
                falarmal.pos.y = -500
                gritar.pos.y = -850
                desrespeitar.pos.y = -1150
                mentefechada.pos.y = -1400
                
                fundo = pygame.image.load("Imagens/Terceira Fase/fundo3.png")
                for plat in plataformas: 
                    plat.kill()
                for val in valoresgrupo : 
                    val.kill()      
                p0 = Chao(-15, 544)
                plataformas.add(p0)
                p1 = Plataformas(250, 255, "Imagens/Terceira Fase/plataforma3.png")
                plataformas.add(p1)
                p2 = Plataformas(10, 395, "Imagens/Terceira Fase/plataforma3.png")
                plataformas.add(p2)
                p3 = Plataformas(10, 125, "Imagens/Terceira Fase/plataforma3.png")
                plataformas.add(p3)
                p4 = Plataformas(235, -10, "Imagens/Terceira Fase/plataforma3.png")
                plataformas.add(p4)

                #codigo inimigo voltando
                if interromper.pos.x > 500: #esse vai da esquerda pra direita
                    interromper.pos.x = 0
                if falarmal.pos.x < 0: #esse esquerda direita
                    falarmal.pos.x = 500
                if gritar.pos.x > 500: 
                    gritar.pos.x = 0
                if desrespeitar.pos.x < 0: 
                    desrespeitar.pos.x = 500
                if mentefechada.pos.x > 500: 
                    mentefechada.pos.x = 0

                personagem.rect.midbottom = personagem.pos

                if iconef3.rect.x >= 0 and iconef3.rect.x <= 500: 
                    capacete.acc = vec(0, 1)
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT]:
                        capacete.acc.x = -0.9

                    if keys[pygame.K_RIGHT]:
                        capacete.acc.x = 0.9

                    capacete.acc.x += capacete.vel.x * (-0.12)
                    capacete.vel += capacete.acc
                    capacete.pos += capacete.vel + 0.5 * capacete.acc


                    if capacete.pos.x > 500:
                        capacete.pos.x = 0
                    if capacete.pos.x < 0:
                        capacete.pos.x = 500

                    capacete.rect.midbottom = capacete.pos


        #Game Over

        if personagem.rect.top > 650:
            personagem.pos = vec(400,530)
            gameover.rect.left = 0
            botaogameover.rect.left = 182.985 
            fundoinicial.rect.left = 0
            for plat in plataformas: 
                plat.kill()   
            p0 = Chao(-15, 544)
            plataformas.add(p0)
            p1 = Plataformas(250, 255, "Imagens/Primeira Fase/plataforma1.png")
            plataformas.add(p1)
            p2 = Plataformas(10, 395, "Imagens/Primeira Fase/plataforma1.png")
            plataformas.add(p2)
            p3 = Plataformas(10, 125, "Imagens/Primeira Fase/plataforma1.png")
            plataformas.add(p3)
            p4 = Plataformas(235, -10, "Imagens/Primeira Fase/plataforma1.png")
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
        iconef3grupo.draw(tela)
        transicao3grupo.draw(tela)
        inimigos3grupo.draw(tela)
    

        #Updates
        all_sprites.update        
        pygame.display.update() 



    pygame.quit() 
main()
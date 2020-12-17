import pygame 
import random
from sprites import *
from os import path
from pygame import mixer

vec = pygame.math.Vector2


def main():

    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode([500,650])
    pygame.display.set_caption("PET UP")
    relogio = pygame.time.Clock()
    fundo = pygame.image.load("Imagens/Primeira Fase/fundo123desfocado.png")
    mixer.music.load("Som/Músicas/day 33.mp3")
    mixer.music.play(1)
    

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

        if xmouse >= personagem1.rect.left and xmouse <= personagem1.rect.right 
        and ymouse <= personagem1.rect.bottom and ymouse >= personagem1.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                personagem.image = pygame.image.load("Imagens/personagem/personagem1frente_min.png") #personagem1frente
                personagem.rect = personagem.image.get_rect()
                personagem.rect.midbottom = (800,800)
                selecao.rect.right = 217
                personagem.p11 = True
                personagem.p22 = False
                personagem.p10 = False

        if xmouse >= personagem2.rect.left and xmouse <= personagem2.rect.right and ymouse <= personagem2.rect.bottom and ymouse >= personagem2.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                personagem.image = pygame.image.load("Imagens/personagem/personagem2frente_min.png") #personagem1frente
                personagem.rect = personagem.image.get_rect()
                personagem.rect.midbottom=(800,800)
                selecao.rect.right = 412
                personagem.p11 = False
                personagem.p22 = True
                personagem.p10 = False
            
        if xmouse >= botaoplay.rect.left and xmouse <= botaoplay.rect.right and ymouse <= 351 and ymouse >= 295:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pag_inicial.rect.left = 800
                botaoplay.rect.left = 800
                sobre.rect.right = 1000
                personagem1.rect.left = 800
                personagem2.rect.left = 800
                selecao.rect.right = 800
                fundo = pygame.image.load("Imagens/Primeira Fase/fundo1_112.png")
                fundoinicial.rect.left = 800 
                pygame.mixer.music.stop()
                mixer.music.load("Som/Músicas/day 32.mp3")
                mixer.music.play(1)

        if xmouse >= sobre.rect.left and xmouse <= sobre.rect.right and ymouse <= sobre.rect.bottom and ymouse >= sobre.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                sobrejogo.rect.left = 0
                seta.rect.top = 500
                seta.rect.bottom = 650
                seta.rect.left = 1000
                seta.rect.right = 150

        if xmouse >= seta.rect.left and xmouse <= seta.rect.right and ymouse <= seta.rect.bottom and ymouse >= seta.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                sobrejogo.rect.left = 1000
                tutorial.rect.left = 0
                seta.rect.bottom = 660
                seta.rect.left = 1000
                seta.rect.right = 1000
                setatut.rect.top = 500
                setatut.rect.bottom = 650
                setatut.rect.left = 1000
                setatut.rect.right = 210
        
        if xmouse >= setatut.rect.left and xmouse <= setatut.rect.right and ymouse <= setatut.rect.bottom and ymouse >= setatut.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                tutorial.rect.left = 1000
                pontuações.rect.left = 0
                setatut.rect.bottom = 660
                setatut.rect.left = 1000
                setatut.rect.right = 1000
                setapont.rect.top = 500
                setapont.rect.bottom = 650
                setapont.rect.left = 1000
                setapont.rect.right = 270

        if xmouse >= setapont.rect.left and xmouse <= setapont.rect.right and ymouse <= setapont.rect.bottom and ymouse >= setapont.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pontuações.rect.left = 1000
                fases1.rect.left = 0
                setapont.rect.bottom = 660
                setapont.rect.left = 1000
                setapont.rect.right = 1000
                setaf1.rect.top = 500
                setaf1.rect.bottom = 650
                setaf1.rect.left = 1000
                setaf1.rect.right = 340

        if xmouse >= setaf1.rect.left and xmouse <= setaf1.rect.right and ymouse <= setaf1.rect.bottom and ymouse >= setaf1.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                fases1.rect.left = 1000
                fases4.rect.left = 0
                setaf1.rect.bottom = 660
                setaf1.rect.left = 1000
                setaf1.rect.right = 1000
                setaf4.rect.top = 500
                setaf4.rect.bottom = 650
                setaf4.rect.left = 1000
                setaf4.rect.right = 400
        
        if xmouse >= setaf4.rect.left and xmouse <= setaf4.rect.right and ymouse <= setaf4.rect.bottom and ymouse >= setaf4.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                fases4.rect.left = 1000
                agradecimento.rect.left = 0
                setaf4.rect.bottom = 660
                setaf4.rect.left = 1000
                setaf4.rect.right = 1000
                botaoexit.rect.top = 500
                botaoexit.rect.bottom = 650
                botaoexit.rect.left = 1000
                botaoexit.rect.right = 500


        if xmouse >= botaoexit.rect.left and xmouse <= botaoexit.rect.right and ymouse <= botaoexit.rect.bottom and ymouse >= botaoexit.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                agradecimento.rect.left = 1000
                botaoexit.rect.right = 1000



        

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
        interromper.vel = vec(3,0)
        interromper.pos += interromper.vel + 0.5 * interromper.acc
        interromper.rect.midbottom = interromper.pos
        if interromper.pos.x > 500:
            interromper.pos.x = 0

        falarmal.acc = vec(-1, 0)

        falarmal.vel = vec(-3,0)
        falarmal.pos += falarmal.vel - 0.5 * falarmal.acc
        falarmal.rect.midbottom = falarmal.pos
        if falarmal.pos.x < 0:
            falarmal.pos.x = 500

        falardemais.acc = vec(1, 0)
        falardemais.vel = vec(3,0)
        falardemais.pos += falardemais.vel + 0.5 * falardemais.acc
        falardemais.rect.midbottom = falardemais.pos
        if falardemais.pos.x > 500:
            falardemais.pos.x = 0

        desrespeitar.acc = vec(-1, 0)
        desrespeitar.vel = vec(-3,0)
        desrespeitar.pos += desrespeitar.vel - 0.5 * desrespeitar.acc
        desrespeitar.rect.midbottom = desrespeitar.pos
        if desrespeitar.pos.x < 0:
            desrespeitar.pos.x = 500

        mentefechada.acc = vec(1, 0)
        mentefechada.vel = vec(3,0)
        mentefechada.pos += mentefechada.vel + 0.5 * mentefechada.acc
        mentefechada.rect.midbottom = mentefechada.pos
        if mentefechada.pos.x > 500:
            mentefechada.pos.x = 0

        #CODIGO INIMIGOS MOVIMENTO FASE 4 

        respostas.acc = vec(1, 0)
        respostas.vel = vec(3,0)
        respostas.pos += respostas.vel + 0.5 * respostas.acc
        respostas.rect.midbottom = respostas.pos
        if respostas.pos.x > 500:
            respostas.pos.x = 0

        falta.acc = vec(-1, 0)
        falta.vel = vec(-3,0)
        falta.pos += falta.vel - 0.5 * falta.acc
        falta.rect.midbottom = falta.pos
        if falta.pos.x < 0:
            falta.pos.x = 500

        irdes.acc = vec(1, 0)
        irdes.vel = vec(3,0)
        irdes.pos += irdes.vel + 0.5 * irdes.acc
        irdes.rect.midbottom = irdes.pos
        if irdes.pos.x > 500:
            irdes.pos.x = 0

        mentir.acc = vec(-1, 0)
        mentir.vel = vec(-3,0)
        mentir.pos += mentir.vel - 0.5 * mentir.acc
        mentir.rect.midbottom = mentir.pos
        if mentir.pos.x < 0:
            mentir.pos.x = 500

        preguiça.acc = vec(1, 0)
        preguiça.vel = vec(3,0)
        preguiça.pos += preguiça.vel + 0.5 * preguiça.acc
        preguiça.rect.midbottom = preguiça.pos
        if preguiça.pos.x > 500:
            preguiça.pos.x = 0

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
        if colisao_bolinhas:
            pontuação.p = pontuação.p + 50
        colisao_valores = pygame.sprite.spritecollide(personagem, valoresgrupo, True)
        if colisao_valores:
            pontuação.p = pontuação.p + 50
        colisao_bolinhas4 = pygame.sprite.spritecollide(personagem, bolinhas4grupo, True)
        if colisao_bolinhas4:
            pontuação.p = pontuação.p + 50

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
            for ini in inimigos3grupo:
                ini.pos.y = 2000

        colisao_icone4 = pygame.sprite.spritecollide(personagem, iconef4grupo, False)
        if colisao_icone4:
            transição41.rect.left = -1
            abrir.rect.left = 385
            abrir.rect.top = 285
            for bol in bolinhas4grupo:
                bol.kill()
            for ini in inimigos4grupo:
                ini.pos.y = 2000

        if xmouse >= abrir.rect.left and xmouse <= abrir.rect.right and ymouse <= abrir.rect.bottom and ymouse >= abrir.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                transição42.rect.left = -1
                transição41.rect.left = 800
                abrir.rect.left = -800
                botaot4.rect.left = 335
                botaot4.rect.top = 585
                iconef4.rect.x = 800
            if som.jaaconteceu == False:
                pygame.mixer.music.stop()
                mixer.music.load("Som/Músicas/Rise of spirit.ogg")
                mixer.music.play(1)



        colisao_inimigos3 = pygame.sprite.spritecollide(personagem, inimigos3grupo, False)
        colisao_inimigos4 = pygame.sprite.spritecollide(personagem, inimigos4grupo, False) 

        colisao_icone5 = pygame.sprite.spritecollide(personagem, iconef5grupo, False)
        if colisao_icone5:
            transiçãofinal.rect.left = -1
            personagemfinal.rect.x = 210
            personagemfinal.rect.y = 425
            if personagem.p11 == True:
                    personagemfinal.image = pygame.image.load("Imagens/Quinta Fase/personagemfinal.png")
            if personagem.p10 == True:
                    personagemfinal.image = pygame.image.load("Imagens/Quinta Fase/personagemfinal.png")
            if personagem.p22 == True:
                    personagemfinal.image = pygame.image.load("Imagens/Quinta Fase/personagem2final.png")
            fimdejogo.rect.left = 0
            botaofinal.rect.left = 199
            pontuacaogameover.l = 267
            pontuacaogameover.o = 180
            creditos.rect.left = 10

        #pulo
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    personagem.rect.x += 1
                    colisao_plataforma = pygame.sprite.spritecollide(personagem, plataformas, False)
                    personagem.rect.x -= 1
                    if  colisao_plataforma:
                        if personagem.pos.y == colisao_plataforma[0].rect.top:
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
            for ic4 in iconef4grupo:
                ic4.rect.y += abs(personagem.vel.y)
            for ic5 in iconef5grupo:
                ic5.rect.y += abs(personagem.vel.y)
            for bol in bolinhas4grupo: #bolinhas 4
                bol.rect.y += abs(personagem.vel.y)
            for ini in inimigos3grupo:
                ini.pos.y += abs(personagem.vel.y)
            for ini in inimigos4grupo:
                ini.pos.y += abs(personagem.vel.y)
            for ic in iconegrupo:
                ic.rect.y += abs(personagem.vel.y)
            for platfin in platfinal:
                platfin.rect.y += abs(personagem.vel.y)
            for per in expetianojoaogroup:
                per.rect.y += abs(personagem.vel.y)
            for per in expetianoarthurgroup:
                per.rect.y += abs(personagem.vel.y)
            for per in expetianomarialauragroup:
                per.rect.y += abs(personagem.vel.y)
            for per in expetianoeduardagroup :
                per.rect.y += abs(personagem.vel.y)
            for plat in plataformas:
                plat.rect.y += abs(personagem.vel.y)
                if plat.rect.top >= 650:
                    plat.kill()
                    pontuação.p = pontuação.p + 10

        # Spawn novas plat fase 1
        if pfinal1.rect.top <-155:
            while len(plataformas) < 5:
                if iconefinal.rect.x >= 0 and iconefinal.rect.x <= 500: 
                    p = Plataformas(random.randrange(5, 300),-105, "Imagens/Primeira Fase/plataforma1.png")
                    plataformas.add(p)
        if pfinal2.rect.top <-155 and pfinal2.rect.left <= 10:
            while len(plataformas) < 5:
                if iconef2.rect.x >= 0 and iconef2.rect.x <= 500: 
                    p = Plataformas(random.randrange(5, 300),-105, "Imagens/Segunda Fase/plataforma2.png")
                    plataformas.add(p)
        if pfinal3.rect.top <-155 and pfinal3.rect.left <= 10:
            while len(plataformas) < 5:
                if iconef3.rect.x >= 0 and iconef3.rect.x <= 500: 
                    p = Plataformas(random.randrange(5, 300),-105, "Imagens/Terceira Fase/plataforma3.png")
                    plataformas.add(p)

        if pfinal4.rect.top <-155 and pfinal4.rect.left <= 10:
            while len(plataformas) < 5:
                if iconef4.rect.x >= 0 and iconef4.rect.x <= 500: 
                    p = Plataformas(random.randrange(5, 300),-105, "Imagens/Quarta Fase/plataforma4.png")
                    plataformas.add(p)
        
    
        #Fase 2

        if xmouse >= botaot.rect.left and xmouse <= botaot.rect.right and ymouse <= botaot.rect.bottom and ymouse >= botaot.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                personagem.pos = vec(400,530)
                pontuação.p = pontuação.p + 150
                transição1.rect.left= 800
                botaot.rect.right = 800
                iconefinal.rect.x = 800
                pfinal1.rect.left = 800
                pfinal2.rect.left = 5
                pfinal2.rect.top = -2450
                fundo = pygame.image.load("Imagens/Segunda Fase/fundo2.png")
                Plataformas.image = pygame.image.load("Imagens/Segunda Fase/plataforma2.png")
                for plat in plataformas: 
                    plat.kill()
                for bol in bolinhas : 
                    bol.kill()   
                p0 = Chao(-15, 500)
                plataformas.add(p0)
                p1 = Plataformas(10, 350, "Imagens/Segunda Fase/plataforma2.png")
                plataformas.add(p1)
                p2 = Plataformas(250, 200, "Imagens/Segunda Fase/plataforma2.png")
                plataformas.add(p2)
                p3 = Plataformas(10, 50, "Imagens/Segunda Fase/plataforma2.png")
                plataformas.add(p3)  
                if som.jaaconteceu == False:
                    pygame.mixer.music.stop()
                    mixer.music.load("Som/Músicas/day 43.mp3")
                    mixer.music.play(1)

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
                iconef2.rect.y = -2555

        # fase 3

        if xmouse >= botaot2.rect.left and xmouse <= botaot2.rect.right and ymouse <= botaot2.rect.bottom and ymouse >= botaot2.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if personagem.p11 == True:
                    personagem.image = pygame.image.load("Imagens/personagem/personagem1minespaço.png")
                if personagem.p10 == True:
                    personagem.image = pygame.image.load("Imagens/personagem/personagem1minespaço.png")
                if personagem.p22 == True:
                    personagem.image = pygame.image.load("Imagens/personagem/personagem2minespaço.png")
                personagem.pos = vec(400,530)
                pontuação.p = pontuação.p + 150
                transição2.rect.left= 800
                botaot2.rect.right = 800
                iconef2.rect.x = 800
                iconef3.rect.x = 50
                iconef3.rect.y = -2555
                pfinal2.rect.left = 800
                pfinal3.rect.left = 5
                pfinal3.rect.top = -2450
                if som.jaaconteceu == False:
                    pygame.mixer.music.stop()
                    mixer.music.load("Som/Músicas/Full of memories.ogg")
                    mixer.music.play(1)
                
                
                interromper.pos.y = -10
                falarmal.pos.y = -500
                falardemais.pos.y = -1000
                desrespeitar.pos.y = -1500
                mentefechada.pos.y = -2000
                
                fundo = pygame.image.load("Imagens/Terceira Fase/fundo3.png")
                for plat in plataformas: 
                    plat.kill()
                for val in valoresgrupo : 
                    val.kill()      
                p0 = Chao(-15, 500)
                plataformas.add(p0)
                p1 = Plataformas(10, 350, "Imagens/Terceira Fase/plataforma3.png")
                plataformas.add(p1)
                p2 = Plataformas(250, 200, "Imagens/Terceira Fase/plataforma3.png")
                plataformas.add(p2)
                p3 = Plataformas(10, 50, "Imagens/Terceira Fase/plataforma3.png")
                plataformas.add(p3)  
                

        #fase 4 

        if xmouse >= botaot3.rect.left and xmouse <= botaot3.rect.right and ymouse <= botaot3.rect.bottom and ymouse >= botaot3.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if personagem.p11 == True:
                    personagem.image = pygame.image.load("Imagens/personagem/personagem1frente_min.png")
                if personagem.p10 == True:
                    personagem.image = pygame.image.load("Imagens/personagem/personagem1frente_min.png")
                if personagem.p22 == True:
                    personagem.image = pygame.image.load("Imagens/personagem/personagem2frente_min.png")
                fundo = pygame.image.load("Imagens/Quarta Fase/fundo 4.png")
                personagem.pos = vec(400,530)
                pontuação.p = pontuação.p + 150
                transição3.rect.left= 800
                botaot3.rect.right = 800
                pfinal3.rect.left = 800
                iconef3.rect.x = 800 #até aqui jogamos pra longe
                if som.jaaconteceu == False:
                    pygame.mixer.music.stop()
                    mixer.music.load("Som/Músicas/day 34.mp3")
                    mixer.music.play(1)


                iconef4.rect.x = 50
                iconef4.rect.y = -2555
                pfinal4.rect.left = 5
                pfinal4.rect.top = -2450

                respostas.pos.y = -10
                falta.pos.y = -500
                irdes.pos.y = -1000
                mentir.pos.y = -1500
                preguiça.pos.y = -2000

                coo = Bolinha4("Imagens/Quarta Fase/obstáculos/COO.png",random.uniform(400,200))
                sec = Bolinha4("Imagens/Quarta Fase/obstáculos/SEC.png",random.uniform(-400,-200))
                tes = Bolinha4("Imagens/Quarta Fase/obstáculos/TES.png",random.uniform(-600,-400))
                pep = Bolinha4("Imagens/Quarta Fase/obstáculos/PEP.png",random.uniform(-800,-600))
                mkt = Bolinha4("Imagens/Quarta Fase/obstáculos/MKT.png",random.uniform(-1000,-800))
                evt = Bolinha4("Imagens/Quarta Fase/obstáculos/EVT.png",random.uniform(-1200,-1000))
                inter = Bolinha4("Imagens/Quarta Fase/obstáculos/INTERPET.png",random.uniform(-1400,-1200))
                qld = Bolinha4("Imagens/Quarta Fase/obstáculos/qld.png",random.uniform(-1600,-1400))
                bolinhas4grupo.add(coo, tes, pep, sec, mkt, evt, inter, qld)

                coo.rect.x = random.uniform(50,400)
                sec.rect.x = random.uniform(50,400)
                tes.rect.x = random.uniform(50,400)
                qld.rect.x = random.uniform(50,400)
                pep.rect.x = random.uniform(50,400)
                mkt.rect.x = random.uniform(50,400)
                evt.rect.x = random.uniform(50,400)
                inter.rect.x = random.uniform(50,400)

                coo.rect.y = random.uniform(400,200)
                sec.rect.y = random.uniform(200,0)
                tes.rect.y = random.uniform(-100,-300)
                pep.rect.y = random.uniform(-400,-600)
                mkt.rect.y = random.uniform(-800,-1000)
                evt.rect.y = random.uniform(-1200,-1400)
                inter.rect.y = random.uniform(-1600,-1800)
                qld.rect.y = random.uniform(-2000,-2200)
                for plat in plataformas: 
                    plat.kill()     
                p0 = Chao(-15, 500)
                plataformas.add(p0)
                p1 = Plataformas(10, 350, "Imagens/Quarta Fase/plataforma4.png")
                plataformas.add(p1)
                p2 = Plataformas(250, 200, "Imagens/Quarta Fase/plataforma4.png")
                plataformas.add(p2)
                p3 = Plataformas(10, 50, "Imagens/Quarta Fase/plataforma4.png")
                plataformas.add(p3)  


        #Fase 5 
        if xmouse >= botaot4.rect.left and xmouse <= botaot4.rect.right and ymouse <= botaot4.rect.bottom and ymouse >= botaot4.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                fundo = pygame.image.load("Imagens/Quinta Fase/fundo5.png")
                personagem.pos = vec(400,530)
                transição42.rect.left= 800
                botaot4.rect.right = 800
                pfinal4.rect.left = 800
                iconef4.rect.x = 800 
                pontuação.p = pontuação.p + 150

                iconef5.rect.x = 50
                iconef5.rect.y = -2555
                pfinal5.rect.left = 5
                pfinal5.rect.top = -2450

                for plat in plataformas: 
                    plat.kill()     
                p0 = Chao(-15, 500)
                plataformas.add(p0)
                p1 = Plataformas(random.randrange(5, 300), 350, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(p1)
                p2 = Plataformas(random.randrange(5, 300), 200, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(p2)
                p3 = Plataformas(random.randrange(5, 300), 50, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(p3)  
                p4 = Plataformas(random.randrange(5, 300), -100, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(p4)
                p6 = Plataformas(random.randrange(5, 300), -250, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(p6)
                plataformaarthur=Plataformas(50, -400, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(plataformaarthur)
                p8 = Plataformas(random.randrange(5, 300), -550, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(p8)
                p10 = Plataformas(random.randrange(5, 300), -700, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(p10)
                plataformaeduarda=Plataformas(300, -850, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(plataformaeduarda)
                p12 = Plataformas(random.randrange(5, 300), -1000, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(p12)
                p14 = Plataformas(random.randrange(5, 300), -1150, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(p14)
                plataformamarialaura=Plataformas(50, -1300, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(plataformamarialaura)
                p16 = Plataformas(random.randrange(5, 300), -1450, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(p16)
                p18 = Plataformas(random.randrange(5, 300), -1600, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(p18)
                plataformajoao=Plataformas(300, -1750, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(plataformajoao)
                p20 = Plataformas(random.randrange(5, 300), -1900, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(p20)
                p22 = Plataformas(random.randrange(5, 300), -2050, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(p22)
                p24 = Plataformas(random.randrange(5, 300), -2200, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(p24)
                p26 = Plataformas(random.randrange(5, 300), -2350, "Imagens/Quinta Fase/plataforma5.png")
                plataformas.add(p26)

                personagemarthur.rect.left=120
                personagemarthur.rect.top=-470

                personagemmarialaura.rect.left=420
                personagemmarialaura.rect.top=-920

                personagemjoao.rect.left=120
                personagemjoao.rect.top=-1370

                personagemeduarda.rect.left=420
                personagemeduarda.rect.top=-1820

        #Colisão Expetianos
        colisao_marialaura = pygame.sprite.spritecollide(personagem, expetianomarialauragroup, False)
        if colisao_marialaura:
            if personagemmarialaura.jaaconteceu == False:
                fundo = pygame.image.load("Imagens/Quinta Fase/fundo5desfocado.png")
                falamarialaura.rect.left=  70.504 
                botaoexpetianos.rect.top = 95
                botaoexpetianos.rect.left = 80
                pontuação.p = pontuação.p + 100
                personagemmarialaura.jaaconteceu = True
        
        colisao_eduarda = pygame.sprite.spritecollide(personagem, expetianoeduardagroup, False)
        if colisao_eduarda:
            if personagemeduarda.jaaconteceu == False:
                fundo = pygame.image.load("Imagens/Quinta Fase/fundo5desfocado.png")
                falaeduarda.rect.left=70.504 
                botaoexpetianos.rect.top = 95
                botaoexpetianos.rect.left = 80
                pontuação.p = pontuação.p + 100
                personagemeduarda.jaaconteceu = True
        
        colisao_arthur = pygame.sprite.spritecollide(personagem, expetianoarthurgroup, False)
        if colisao_arthur:
            if personagemarthur.jaaconteceu == False:
                fundo = pygame.image.load("Imagens/Quinta Fase/fundo5desfocado.png")
                falaarthur.rect.left= 70.504 
                botaoexpetianos.rect.top = 95
                botaoexpetianos.rect.left = 80
                pontuação.p = pontuação.p + 100
                personagemarthur.jaaconteceu = True
        
        colisao_joao = pygame.sprite.spritecollide(personagem, expetianojoaogroup, False)
        if colisao_joao:
            if personagemjoao.jaaconteceu == False:
                fundo = pygame.image.load("Imagens/Quinta Fase/fundo5desfocado.png")
                falajoao.rect.left=70.504 
                botaoexpetianos.rect.top = 95
                botaoexpetianos.rect.left = 80
                pontuação.p = pontuação.p + 100 
                personagemjoao.jaaconteceu = True

        if xmouse >= botaoexpetianos.rect.left and xmouse <= botaoexpetianos.rect.right and ymouse <= botaoexpetianos.rect.bottom and ymouse >= botaoexpetianos.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN: 
                fundo = pygame.image.load("Imagens/Quinta Fase/fundo5.png")
                falaarthur.rect.left= 1600
                falaeduarda.rect.left= -800
                falamarialaura.rect.left= -800
                botaoexpetianos.rect.left = 800
                falajoao.rect.left = -800

        
        if xmouse >= botaofinal.rect.left and xmouse <= botaofinal.rect.right and ymouse <= botaofinal.rect.bottom and ymouse >= botaofinal.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                fundoinicial.image = pygame.image.load("Imagens/Primeira Fase/fundo123desfocado.png")
                creditos.rect.left = 800
                personagem.pos = vec(400,530)
                pag_inicial.rect.left= 0
                botaoplay.rect.right = 314
                personagem1.rect.right = 210
                personagem2.rect.right = 405
                fimdejogo.rect.left = 800
                botaofinal.rect.left = 800
                pontuação.p = 0
                pontuacaogameover.rect.left = 800
                pontuacaogameover.l = 800
                fundoinicial.rect.left = 0
                pfinal1.rect.left = 5
                pfinal1.rect.top = -2450
                iconefinal.rect.x = 50
                iconefinal.rect.y = -2555
                som1.jaaconteceu = False
                som.jaaconteceu = False
                for plat in plataformas: 
                    plat.kill()
                p0 = Chao(-15, 500)
                plataformas.add(p0)
                p1 = Plataformas(10, 350, "Imagens/Primeira Fase/plataforma1.png")
                plataformas.add(p1)
                p2 = Plataformas(250, 200, "Imagens/Primeira Fase/plataforma1.png")
                plataformas.add(p2)
                p3 = Plataformas(10, 50, "Imagens/Primeira Fase/plataforma1.png")
                plataformas.add(p3)
                ensino= Bolinha1()
                bolinhas.add(ensino)
                pesquisa = Bolinha2()
                bolinhas.add(pesquisa)
                extensao = Bolinha3()
                bolinhas.add(extensao)
                pfinal5.rect.left = 800
                pfinal5.rect.top = -2450
                iconef5.rect.x = 800
                iconef5.rect.y = -2555
                personagemarthur.rect.left=800
                personagemarthur.rect.top=-800
                personagemmarialaura.rect.left=800
                personagemjoao.rect.left=800
                personagemeduarda.rect.left=800
                falaarthur.rect.left= 1600
                falaeduarda.rect.left= 800
                falamarialaura.rect.left= 800
                botaoexpetianos.rect.left = 800
                falajoao.rect.left = 800
                transiçãofinal.rect.left = 800
                personagemfinal.rect.x = 800
                falaarthur.jaaconteceu = False
                falamarialaura.jaaconteceu = False
                falaeduarda.jaaconteceu = False
                falajoao.jaaconteceu = False

                pygame.mixer.music.stop()
                mixer.music.load("Som/Músicas/day 33.mp3")
                mixer.music.play(1)


        #Game Over

        if personagem.rect.top > 650 or colisao_inimigos3 or colisao_inimigos4:
            pygame.mixer.music.stop()
            mixer.music.load("Som/Músicas/day 10.mp3")
            mixer.music.play(1)
            pontuacaogameover.rect.left = 250
            pontuacaogameover.l = 265
            pontuacaogameover.o = 260
            personagem.pos = vec(400,530)
            gameover.rect.left = 0
            botaogameover.rect.left = 182.985 
            fundoinicial.rect.left = 0
            pfinal1.rect.left = 5
            pfinal1.rect.top = -2450
            iconefinal.rect.x = 50
            iconefinal.rect.y = -2555
            creditos.rect.left = 10
            som1.jaaconteceu = False
            som.jaaconteceu = False
            for plat in plataformas: 
                plat.kill() 

            if iconefinal.rect.x >= 0 and iconefinal.rect.x <= 500: 
                for bol in bolinhas : 
                    bol.kill()
                fundoinicial.image = pygame.image.load("Imagens/Primeira Fase/fundo123desfocado.png")

            if iconef2.rect.x >= 0 and iconef2.rect.x <= 500:
                for val in valoresgrupo : 
                    val.kill()   
                fundoinicial.image = pygame.image.load("Imagens/Segunda Fase/Fundo2desfocado.png")
                pfinal2.rect.left = 800
                pfinal2.rect.top = -2450
                iconef2.rect.x = 800
                iconef2.rect.y = -2555
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

            if iconef3.rect.x >= 0 and iconef3.rect.x <= 500:
                pfinal3.rect.left = 800
                pfinal3.rect.top = -2450
                iconef3.rect.x = 800
                iconef3.rect.y = -2555
                fundoinicial.image = pygame.image.load("Imagens/Terceira Fase/Fundo3desfocado.png")
                for ini in inimigos3grupo:
                    ini.pos.y = 2000
                if personagem.p11 == True:
                    personagem.image = pygame.image.load("Imagens/personagem/personagem1frente_min.png")
                if personagem.p10 == True:
                    personagem.image = pygame.image.load("Imagens/personagem/personagem1frente_min.png")
                if personagem.p22 == True:
                    personagem.image = pygame.image.load("Imagens/personagem/personagem2frente_min.png")

                

            if iconef4.rect.x >= 0 and iconef4.rect.x <= 500:
                fundoinicial.image = pygame.image.load("Imagens/Quarta Fase/Fundo4desfocado.png")
                pfinal4.rect.left = 800
                pfinal4.rect.top = -2450
                iconef4.rect.x = 800
                iconef4.rect.y = -2555
                fundoinicial.image = pygame.image.load("Imagens/Quarta Fase/Fundo4desfocado.png")
                for ini in inimigos4grupo:
                    ini.pos.y = 2000
                for bol in bolinhas4grupo:
                    bol.kill()

            if iconef5.rect.x >= 0 and iconef5.rect.x <= 500: 
                fundoinicial.image = pygame.image.load("Imagens/Quinta Fase/fundo5desfocado.png")
                pfinal5.rect.left = 800
                pfinal5.rect.top = -2450
                iconef5.rect.x = 800
                iconef5.rect.y = -2555
                personagemarthur.rect.left=800
                personagemarthur.rect.top=-800
                personagemmarialaura.rect.left=800
                personagemjoao.rect.left=800
                personagemeduarda.rect.left=800
                falaarthur.rect.left= 1600
                falaeduarda.rect.left= -800
                falamarialaura.rect.left= -800
                botaoexpetianos.rect.left = 800
                falajoao.rect.left = -800
                falaarthur.jaaconteceu = False
                falamarialaura.jaaconteceu = False
                falaeduarda.jaaconteceu = False
                falajoao.jaaconteceu = False

            p0 = Chao(-15, 500)
            plataformas.add(p0)
            p1 = Plataformas(10, 350, "Imagens/Primeira Fase/plataforma1.png")
            plataformas.add(p1)
            p2 = Plataformas(250, 200, "Imagens/Primeira Fase/plataforma1.png")
            plataformas.add(p2)
            p3 = Plataformas(10, 50, "Imagens/Primeira Fase/plataforma1.png")
            plataformas.add(p3) 
            ensino= Bolinha1()
            bolinhas.add(ensino)
            pesquisa = Bolinha2()
            bolinhas.add(pesquisa)
            extensao = Bolinha3()
            bolinhas.add(extensao)

        if xmouse >= botaogameover.rect.left and xmouse <= botaogameover.rect.right and ymouse <= botaogameover.rect.bottom and ymouse >= botaogameover.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pag_inicial.rect.left= 0
                botaoplay.rect.right = 314
                personagem1.rect.right = 210
                personagem2.rect.right = 405
                gameover.rect.left = 800
                botaogameover.rect.left = 800
                pontuação.p = 0
                pontuacaogameover.rect.left = 800
                pontuacaogameover.l = 800
                pygame.mixer.music.stop()
                mixer.music.load("Som/Músicas/day 33.mp3")
                mixer.music.play(1)
                creditos.rect.left = 800

        if som.jaaconteceu == False:
            if xmouse >= som1.rect.left and xmouse <= som1.rect.right and ymouse <= som1.rect.bottom and ymouse >= som1.rect.top:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.stop() 
                    som1.jaaconteceu = True
                    som.jaaconteceu = True

        if som1.jaaconteceu == True:
            if xmouse >= som.rect.left and xmouse <= som.rect.right and ymouse <= som.rect.bottom and ymouse >= som.rect.top:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    som1.jaaconteceu = False
                    som.jaaconteceu = False
                    
                    if iconefinal.rect.x >= 0 and iconefinal.rect.x <= 500: 
                        mixer.music.load("Som/Músicas/day 32.mp3")
                        mixer.music.play(1)

                    if iconef2.rect.x >= 0 and iconef2.rect.x <= 500:
                        mixer.music.load("Som/Músicas/day 43.mp3")
                        mixer.music.play(1)

                    if iconef3.rect.x >= 0 and iconef3.rect.x <= 500:
                        mixer.music.load("Som/Músicas/Full of memories.ogg")
                        mixer.music.play(1)

                    if iconef4.rect.x >= 0 and iconef4.rect.x <= 500:
                        mixer.music.load("Som/Músicas/day 34.mp3")
                        mixer.music.play(1)
                    
                    if iconef5.rect.x >= 0 and iconef5.rect.x <= 500: 
                        mixer.music.load("Som/Músicas/Rise of spirit.ogg")
                        mixer.music.play(1)

        if xmouse >= config.rect.left and xmouse <= config.rect.right and ymouse <= config.rect.bottom and ymouse >= config.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                balon.rect.left = 308
                sim.rect.left = 330
                nao.rect.left = 398
        
        if xmouse >= sim.rect.left and xmouse <= sim.rect.right and ymouse <= sim.rect.bottom and ymouse >= sim.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                balon.rect.left = 800
                sim.rect.left = 800
                nao.rect.left = 800
                pygame.mixer.music.stop()
                mixer.music.load("Som/Músicas/day 33.mp3")
                mixer.music.play(1)
                personagem.pos = vec(400,530)
                fundoinicial.rect.left = 0
                pfinal1.rect.left = 5
                pfinal1.rect.top = -2450
                iconefinal.rect.x = 50
                iconefinal.rect.y = -2555
                for plat in plataformas: 
                    plat.kill() 

                if iconefinal.rect.x >= 0 and iconefinal.rect.x <= 500: 
                    for bol in bolinhas : 
                        bol.kill()
                    fundoinicial.image = pygame.image.load("Imagens/Primeira Fase/fundo123desfocado.png")

                if iconef2.rect.x >= 0 and iconef2.rect.x <= 500:
                    for val in valoresgrupo : 
                        val.kill()   
                    fundoinicial.image = pygame.image.load("Imagens/Segunda Fase/Fundo2desfocado.png")
                    pfinal2.rect.left = 800
                    pfinal2.rect.top = -2450
                    iconef2.rect.x = 800
                    iconef2.rect.y = -2555
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

                if iconef3.rect.x >= 0 and iconef3.rect.x <= 500:
                    pfinal3.rect.left = 800
                    pfinal3.rect.top = -2450
                    iconef3.rect.x = 800
                    iconef3.rect.y = -2555
                    fundoinicial.image = pygame.image.load("Imagens/Terceira Fase/Fundo3desfocado.png")
                    for ini in inimigos3grupo:
                        ini.pos.y = 2000
                    if personagem.p11 == True:
                        personagem.image = pygame.image.load("Imagens/personagem/personagem1frente_min.png")
                    if personagem.p10 == True:
                        personagem.image = pygame.image.load("Imagens/personagem/personagem1frente_min.png")
                    if personagem.p22 == True:
                        personagem.image = pygame.image.load("Imagens/personagem/personagem2frente_min.png")

                    

                if iconef4.rect.x >= 0 and iconef4.rect.x <= 500:
                    fundoinicial.image = pygame.image.load("Imagens/Quarta Fase/Fundo4desfocado.png")
                    pfinal4.rect.left = 800
                    pfinal4.rect.top = -2450
                    iconef4.rect.x = 800
                    iconef4.rect.y = -2555
                    fundoinicial.image = pygame.image.load("Imagens/Quarta Fase/Fundo4desfocado.png")
                    for ini in inimigos4grupo:
                        ini.pos.y = 2000
                    for bol in bolinhas4grupo:
                        bol.kill()

                if iconef5.rect.x >= 0 and iconef5.rect.x <= 500: 
                    fundoinicial.image = pygame.image.load("Imagens/Quinta Fase/fundo5desfocado.png")
                    pfinal5.rect.left = 800
                    pfinal5.rect.top = -2450
                    iconef5.rect.x = 800
                    iconef5.rect.y = -2555
                    personagemarthur.rect.left=800
                    personagemarthur.rect.top=-800
                    personagemmarialaura.rect.left=800
                    personagemjoao.rect.left=800
                    personagemeduarda.rect.left=800
                    falaarthur.rect.left= 1600
                    falaeduarda.rect.left= -800
                    falamarialaura.rect.left= -800
                    botaoexpetianos.rect.left = 800
                    falajoao.rect.left = -800
                    falaarthur.jaaconteceu = False
                    falamarialaura.jaaconteceu = False
                    falaeduarda.jaaconteceu = False
                    falajoao.jaaconteceu = False

                p0 = Chao(-15, 500)
                plataformas.add(p0)
                p1 = Plataformas(10, 350, "Imagens/Primeira Fase/plataforma1.png")
                plataformas.add(p1)
                p2 = Plataformas(250, 200, "Imagens/Primeira Fase/plataforma1.png")
                plataformas.add(p2)
                p3 = Plataformas(10, 50, "Imagens/Primeira Fase/plataforma1.png")
                plataformas.add(p3) 
                ensino= Bolinha1()
                bolinhas.add(ensino)
                pesquisa = Bolinha2()
                bolinhas.add(pesquisa)
                extensao = Bolinha3()
                bolinhas.add(extensao)
                pag_inicial.rect.left= 0
                botaoplay.rect.right = 314
                personagem1.rect.right = 210
                personagem2.rect.right = 405
                pontuação.p = 0
                pontuacaogameover.rect.left = 800
                pontuacaogameover.l = 800
                som1.jaaconteceu = False
                som.jaaconteceu = False

        if xmouse >= nao.rect.left and xmouse <= nao.rect.right and ymouse <= nao.rect.bottom and ymouse >= nao.rect.top:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    balon.rect.left = 800
                    sim.rect.left = 800
                    nao.rect.left = 800
                    
                    

                
                
        pontuação1= str(pontuação.p)
        render_pontuação = fonte_pontuação.render(pontuação1,1, (0,0,0))
        render_pontuação1 = fonte_pontuação.render("Pontuação: ",1, (0,0,0))
        render_pontuação2 = fonte_pontuação.render(pontuação1,1, (0,0,0))
        render_pontuação3 = fonte_pontuação.render("pts",1, (0,0,0))
            

        #Desenhar
        tela.blit(fundo, (0,0))
        plataformas.draw(tela)
        bolinhas.draw(tela)
        iconegrupo.draw(tela)
        platfinal.draw(tela)
        personagemgrupo.draw(tela)
        pontuacaogroup.draw(tela)
        tela.blit(render_pontuação,(450.15,17.5))
        tela.blit(render_pontuação1,(350.15,17.5))
        tela.blit(fundoinicial.image, fundoinicial.rect)
        all_sprites.draw(tela)
        valoresgrupo.draw(tela)
        iconef2grupo.draw(tela)
        iconef3grupo.draw(tela)
        inimigos3grupo.draw(tela)
        iconef4grupo.draw(tela)
        iconef5grupo.draw(tela)
        bolinhas4grupo.draw(tela)
        inimigos4grupo.draw(tela)
        expetianomarialauragroup.draw(tela)
        expetianojoaogroup.draw(tela)
        expetianoarthurgroup.draw(tela)
        expetianoeduardagroup.draw(tela)
        falaexpetiano.draw(tela)
        botaoexpetianosgroup.draw(tela)
        setc.draw(tela)
        transicaogrupo.draw(tela)
        transicao2grupo.draw(tela)
        transicao3grupo.draw(tela)
        transicao41grupo.draw(tela)
        transicao42grupo.draw(tela)
        transicaofinal.draw(tela)
        fundoinicialgrupo.draw(tela)
        gameovergrupo.draw(tela)
        tela.blit(render_pontuação2,(pontuacaogameover.l,pontuacaogameover.o))
        tela.blit(render_pontuação3,(pontuacaogameover.l + 45,pontuacaogameover.o))
        all_sprites.draw(tela)
        agradecimentosgrupo.draw(tela)
        botoesinicio.draw(tela)
    

        #Updates
        all_sprites.update        
        pygame.display.update() 



    pygame.quit() 
main()
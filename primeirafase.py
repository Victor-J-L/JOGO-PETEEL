import pygame 

def main():
    pygame.init()
    tela = pygame.display.set_mode([500,650])
    pygame.display.set_caption("Jogo PETEEL")
    relogio = pygame.time.Clock()

    #CORES
    cor_azul = (181,244,253)
    cor_branca = (255,255,255)
    cor_preta = (0,0,0)
    cor_marrom = (126,89,1)
    cor_amarela = (251,222,19)

    #OBJETOS
    nome = pygame.Rect((20,20,460,196))
    quadrado = pygame.Rect((50,231,400,196))
    personagem1 = pygame.Rect((100, 442, 100, 188))
    personagem2 = pygame.Rect((300, 442, 100, 188))
    botao = pygame.Rect((200, 362, 100, 50))

    #IMAGENS
    pag_inicial = pygame.image.load("Imagens/Página inicial/paginainicial2.png")
    sp_paginicial = pygame.sprite.Sprite()
    sp_paginicial.pag_inicial = pag_inicial
    sp_paginicial.rect = pag_inicial.get_rect()
    sp_paginicial.rect.top = -26
    sp_paginicial.rect.left = -16

    botaoplay = pygame.image.load("Imagens/Página inicial/play.png")
    sp_play = pygame.sprite.Sprite()
    sp_play.botaoplay = botaoplay
    sp_play.rect = botaoplay.get_rect()
    sp_play.rect.top = 342
    sp_play.rect.bottom = 391
    sp_play.rect.left = 199
    sp_play.rect.right = 314

    fundo = pygame.image.load("Imagens/Primeira Fase/fundo123desfocado.png")

    #PERSONAGEM 1

    p1frente = pygame.image.load("Imagens/personagem/personagem1frente.png") #personagem1frente
    sp_p1frente = pygame.sprite.Sprite()
    sp_p1frente.p1frente = p1frente 
    sp_p1frente.rect = p1frente.get_rect()
    sp_p1frente.rect.top = 400
    sp_p1frente.rect.bottom = 575
    sp_p1frente.rect.left = 200
    sp_p1frente.rect.right = 210

    #PERSONAGEM 2

    p2frente = pygame.image.load("Imagens/personagem/personagem2frente.png") #personagem2frente
    sp_p2frente = pygame.sprite.Sprite()
    sp_p2frente.p1frente = p2frente 
    sp_p2frente.rect = p2frente.get_rect()
    sp_p2frente.rect.top = 400
    sp_p2frente.rect.bottom = 575
    sp_p2frente.rect.left = 200
    sp_p2frente.rect.right = 405

    personagem = pygame.image.load("Imagens/personagem/personagem1frente.png")
    sp_personagem = pygame.sprite.Sprite()
    sp_personagem.personagem = personagem 
    sp_personagem.rect = personagem.get_rect()
    sp_personagem.rect.top = 800
    sp_personagem.rect.left = 200

    #Plataforma Primeira Fase
    plataforma1 = pygame.image.load("Imagens/Primeira Fase/plataforma.png") #personagem2frente
    sp_plataforma1 = pygame.sprite.Sprite()
    sp_plataforma1.plataforma1 = plataforma1 
    sp_plataforma1.rect = plataforma1.get_rect()
    sp_plataforma1.rect.top = 200
    sp_plataforma1.rect.left = 200

    #Bolinha Primeira Fase
    bolinha = pygame.image.load("Imagens/Primeira Fase/bolinha.png") #personagem2frente
    sp_bolinha = pygame.sprite.Sprite()
    sp_bolinha.bolinha = bolinha 
    sp_bolinha.rect = bolinha.get_rect()
    sp_bolinha.rect.top = 120
    sp_bolinha.rect.bottom = 200
    sp_bolinha.rect.left = 250
    sp_bolinha.rect.right = 300

    #Íncone final primeira fase
    inconefinal1 = pygame.image.load("Imagens/Primeira Fase/iconefinal.png") #personagem2frente
    sp_inconefinal1 = pygame.sprite.Sprite()
    sp_inconefinal1.inconefinal1 = inconefinal1 
    sp_inconefinal1.rect = inconefinal1.get_rect()
    sp_inconefinal1.rect.top = 120
    sp_inconefinal1.rect.bottom = 200
    sp_inconefinal1.rect.left = 280
    sp_inconefinal1.rect.right = 300

    sair = False
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
        

        relogio.tick(30)
        tela.fill(cor_azul)
        (xmouse, ymouse) = pygame.mouse.get_pos()

        if xmouse >= sp_p1frente.rect.left and xmouse <= sp_p1frente.rect.right and ymouse <= sp_p1frente.rect.bottom and ymouse >= sp_p1frente.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                personagem = pygame.image.load("Imagens/personagem/personagem1frente_min.png") #personagem1frente
                sp_personagem = pygame.sprite.Sprite()
                sp_personagem.personagem = personagem 
                sp_personagem.rect = personagem.get_rect()
                sp_personagem.rect.top = 480
                sp_personagem.rect.left = 800

        if xmouse >= sp_p2frente.rect.left and xmouse <= sp_p2frente.rect.right and ymouse <= sp_p2frente.rect.bottom and ymouse >= sp_p2frente.rect.top:
            if event.type == pygame.MOUSEBUTTONDOWN:
                personagem = pygame.image.load("Imagens/personagem/personagem2frente_min.png") #personagem1frente
                sp_personagem = pygame.sprite.Sprite()
                sp_personagem.personagem = personagem 
                sp_personagem.rect = personagem.get_rect()
                sp_personagem.rect.top = 480
                sp_personagem.rect.left = 800
    
        if xmouse >= sp_play.rect.left and xmouse <= sp_play.rect.right and ymouse <= 351 and ymouse >= 295:
            if event.type == pygame.MOUSEBUTTONDOWN:
                sp_paginicial.rect.left = 800
                sp_play.rect.left = 800
                sp_p1frente.rect.left = 800
                sp_p2frente.rect.left = 800
                sp_personagem.rect.top = 480
                sp_personagem.rect.left = 228
                fundo = pygame.image.load("Imagens/Primeira Fase/fundo1_1.png")
                pygame.display.update()
                pygame.display.flip()
                tela.blit(sp_personagem.personagem, sp_personagem.rect)

        


        tela.blit(fundo, (0,0))
        #tela.blit(sp_bolinha.bolinha, sp_bolinha.rect)
        #tela.blit(sp_plataforma1.plataforma1, sp_plataforma1.rect)
        #tela.blit(sp_inconefinal1.inconefinal1, sp_inconefinal1.rect)
        tela.blit(sp_paginicial.pag_inicial, sp_paginicial.rect)
        tela.blit(sp_play.botaoplay, sp_play.rect)
        tela.blit(sp_p1frente.p1frente, sp_p1frente.rect)
        tela.blit(sp_p2frente.p1frente, sp_p2frente.rect)
        tela.blit(sp_personagem.personagem, sp_personagem.rect)
        
        
        pygame.display.update() 
    pygame.quit() 
main() 
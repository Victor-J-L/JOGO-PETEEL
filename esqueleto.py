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
    pag_inicial = pygame.image.load("Imagens/Página inicial/paginainicial.png")
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
    sp_play.rect.right = 301

    fundo = pygame.image.load("Imagens/Primeira Fase/fundo12desfocado.png")

    p1frente = pygame.image.load("Imagens/personagem/personagem1frente.png") #personagem1frente
    sp_p1frente = pygame.sprite.Sprite()
    sp_p1frente.p1frente = p1frente 
    sp_p1frente.rect = p1frente.get_rect()
    sp_p1frente.rect.top = 400
    sp_p1frente.rect.bottom = 575
    sp_p1frente.rect.left = 200
    sp_p1frente.rect.right = 210

    sair = False
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
        

        relogio.tick(30)
        tela.fill(cor_azul)
        (xmouse, ymouse) = pygame.mouse.get_pos()
         
        if xmouse >= sp_play.rect.left and xmouse <= sp_play.rect.right and ymouse <= 351 and ymouse >= 295:
            if event.type == pygame.MOUSEBUTTONDOWN:
                sp_paginicial.rect.left = 800
                sp_play.rect.left = 800
                fundo = pygame.image.load("Imagens/Primeira Fase/fundo1_1.png")

        tela.blit(fundo, (0,0))
        tela.blit(sp_paginicial.pag_inicial, sp_paginicial.rect)
        tela.blit(sp_play.botaoplay, sp_play.rect)
        tela.blit(sp_p1frente.p1frente, sp_p1frente.rect)
        
        
        pygame.display.update() 
    pygame.quit() 
main() 
import pygame 

def main():
    pygame.init()
    tela = pygame.display.set_mode([500,650])
    pygame.display.set_caption("Página Inicial")
    relogio = pygame.time.Clock()
    cor_azul = (181,244,253)
    cor_branca = (255,255,255)
    cor_preta = (0,0,0)
    cor_marrom = (126,89,1)
    cor_amarela = (251,222,19)

    nome = pygame.Rect((20,20,460,196))
    quadrado = pygame.Rect((50,231,400,196))
    personagem1 = pygame.Rect((100, 442, 100, 188))
    personagem2 = pygame.Rect((300, 442, 100, 188))
    botao = pygame.Rect((200, 362, 100, 50))

    sair = False
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

        relogio.tick(30)
        tela.fill(cor_azul)
        
         
        pygame.draw.rect(tela, cor_marrom, quadrado)
        pygame.draw.rect(tela, cor_amarela, nome)
        pygame.draw.rect(tela, cor_branca, personagem1)
        pygame.draw.rect(tela, cor_branca, personagem2)
        pygame.draw.rect(tela, cor_preta, botao)

        pygame.display.update()
    pygame.quit()
main() 
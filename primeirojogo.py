#Curso PYGAME
import pygame
def main():
    pygame.init()
    tela = pygame.display.set_mode([600, 450])
    pygame.display.set_caption("Iniciando o pygame")
    relogio = pygame.time.Clock()
   
   #CORES
    cor_branca = (255,255,255)
    cor_azul = (16,118,148)
    cor_verde = (74,117,43)
    cor_amarela = (255,248,0)
    cor_roxa = (106, 52, 114)

   #SUPERFÍCIES
    sup = pygame.Surface((600,450))
    sup.fill(cor_verde)
    

   #OBJETOS 
    fim = pygame.Rect(500, 390, 100, 60)
    ret= pygame.Rect(10, 10, 30, 30)
    ret2= pygame.Rect(0,40,560, 6)
    ret3= pygame.Rect(40,90,560, 6)
    ret4= pygame.Rect(0,140,360, 6)
    ret4= pygame.Rect(0,140,360, 6)
    ret4_1= pygame.Rect(410,140,190, 6)
    ret5= pygame.Rect(0,190,120, 6)
    ret5_1= pygame.Rect(170,190,430, 6)
    ret6= pygame.Rect(0,240,480, 6)
    ret6_1= pygame.Rect(530,240,70, 6)
    ret7= pygame.Rect(0,290,70, 6)
    ret7_1= pygame.Rect(120,290,480, 6)
    ret8= pygame.Rect(0,340,550, 6)
    ret9= pygame.Rect(50,390,550, 6)

   #FONTE
    pygame.font.init()

    font_padrao = pygame.font.get_default_font()
    font_perdeu = pygame.font.SysFont(font_padrao, 45)
    font_ganhou = pygame.font.SysFont(font_padrao, 45)
    font_recomecar = pygame.font.SysFont(font_padrao, 30)

   #ÁUDIOS 
    audio_explosao = pygame.mixer.Sound('explosao.ogg')

    sair = False

    while sair != True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_pos(20,20)
                main()


        relogio.tick(150)
        tela.fill(cor_branca)
        tela.blit(sup,[0,0])
          
        

        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width/2
        ret.top -= ret.height/2
        if ret.colliderect(ret2):
            text = font_perdeu.render('Você Perdeu', 1, (255, 255, 255))
            tela.blit(text, (215,200))
            text = font_recomecar.render('Clique para recomeçar', 1, (0, 0, 0))
            tela.blit(text, (210,250))
            audio_explosao.play()
            audio_explosao.set_volume(0.01)
            (ret.left, ret.top) = (xant, yant)
            ret2.left= 800
            ret3.left= 800
            ret4.left= 800
            ret4.left= 800
            ret4_1.left= 800
            ret5.left=800
            ret5_1.left= 800
            ret6.left= 800
            ret6_1.left= 800
            ret7.left= 800
            ret7_1.left= 800
            ret8.left= 800
            ret9.left= 800

        if ret.colliderect(ret3):
            text = font_perdeu.render('Você Perdeu', 1, (255, 255, 255))
            tela.blit(text, (215,200))
            text = font_recomecar.render('Clique para recomeçar', 1, (0, 0, 0))
            tela.blit(text, (210,250))
            audio_explosao.play()
            audio_explosao.set_volume(0.01)
            (ret.left, ret.top) = (xant, yant)
            ret2.left= 800
            ret3.left= 800
            ret4.left= 800
            ret4.left= 800
            ret4_1.left= 800
            ret5.left=800
            ret5_1.left= 800
            ret6.left= 800
            ret6_1.left= 800
            ret7.left= 800
            ret7_1.left= 800
            ret8.left= 800
            ret9.left= 800
                        
        if ret.colliderect(ret4):
            text = font_perdeu.render('Você Perdeu', 1, (255, 255, 255))
            tela.blit(text, (215,200))
            text = font_recomecar.render('Clique para recomeçar', 1, (0, 0, 0))
            tela.blit(text, (210,250))
            audio_explosao.play()
            audio_explosao.set_volume(0.01)
            (ret.left, ret.top) = (xant, yant)
            ret2.left= 800
            ret3.left= 800
            ret4.left= 800
            ret4.left= 800
            ret4_1.left= 800
            ret5.left=800
            ret5_1.left= 800
            ret6.left= 800
            ret6_1.left= 800
            ret7.left= 800
            ret7_1.left= 800
            ret8.left= 800
            ret9.left= 800
                        
        if ret.colliderect(ret4_1):
            text = font_perdeu.render('Você Perdeu', 1, (255, 255, 255))
            tela.blit(text, (215,200))
            text = font_recomecar.render('Clique para recomeçar', 1, (0, 0, 0))
            tela.blit(text, (210,250))
            audio_explosao.play()
            audio_explosao.set_volume(0.01)
            (ret.left, ret.top) = (xant, yant)
            ret2.left= 800
            ret3.left= 800
            ret4.left= 800
            ret4.left= 800
            ret4_1.left= 800
            ret5.left=800
            ret5_1.left= 800
            ret6.left= 800
            ret6_1.left= 800
            ret7.left= 800
            ret7_1.left= 800
            ret8.left= 800
            ret9.left= 800
                        
        if ret.colliderect(ret5):
            text = font_perdeu.render('Você Perdeu', 1, (255, 255, 255))
            tela.blit(text, (215,200))
            text = font_recomecar.render('Clique para recomeçar', 1, (0, 0, 0))
            tela.blit(text, (210,250))
            audio_explosao.play()
            audio_explosao.set_volume(0.01)
            (ret.left, ret.top) = (xant, yant)
            ret2.left= 800
            ret3.left= 800
            ret4.left= 800
            ret4.left= 800
            ret4_1.left= 800
            ret5.left=800
            ret5_1.left= 800
            ret6.left= 800
            ret6_1.left= 800
            ret7.left= 800
            ret7_1.left= 800
            ret8.left= 800
            ret9.left= 800
                        
        if ret.colliderect(ret5_1):
            text = font_perdeu.render('Você Perdeu', 1, (255, 255, 255))
            tela.blit(text, (215,200))
            text = font_recomecar.render('Clique para recomeçar', 1, (0, 0, 0))
            tela.blit(text, (210,250))
            audio_explosao.play()
            audio_explosao.set_volume(0.01)
            (ret.left, ret.top) = (xant, yant)
            ret2.left= 800
            ret3.left= 800
            ret4.left= 800
            ret4.left= 800
            ret4_1.left= 800
            ret5.left=800
            ret5_1.left= 800
            ret6.left= 800
            ret6_1.left= 800
            ret7.left= 800
            ret7_1.left= 800
            ret8.left= 800
            ret9.left= 800
                        
        if ret.colliderect(ret6):
            text = font_perdeu.render('Você Perdeu', 1, (255, 255, 255))
            tela.blit(text, (215,200))
            text = font_recomecar.render('Clique para recomeçar', 1, (0, 0, 0))
            tela.blit(text, (210,250))
            audio_explosao.play()
            audio_explosao.set_volume(0.01)
            (ret.left, ret.top) = (xant, yant)
            ret2.left= 800
            ret3.left= 800
            ret4.left= 800
            ret4.left= 800
            ret4_1.left= 800
            ret5.left=800
            ret5_1.left= 800
            ret6.left= 800
            ret6_1.left= 800
            ret7.left= 800
            ret7_1.left= 800
            ret8.left= 800
            ret9.left= 800
                        
        if ret.colliderect(ret6_1):
            text = font_perdeu.render('Você Perdeu', 1, (255, 255, 255))
            tela.blit(text, (215,200))
            text = font_recomecar.render('Clique para recomeçar', 1, (0, 0, 0))
            tela.blit(text, (210,250))
            audio_explosao.play()
            audio_explosao.set_volume(0.01)
            (ret.left, ret.top) = (xant, yant)
            ret2.left= 800
            ret3.left= 800
            ret4.left= 800
            ret4.left= 800
            ret4_1.left= 800
            ret5.left=800
            ret5_1.left= 800
            ret6.left= 800
            ret6_1.left= 800
            ret7.left= 800
            ret7_1.left= 800
            ret8.left= 800
            ret9.left= 800
                        
        if ret.colliderect(ret7):
            text = font_perdeu.render('Você Perdeu', 1, (255, 255, 255))
            tela.blit(text, (215,200))
            text = font_recomecar.render('Clique para recomeçar', 1, (0, 0, 0))
            tela.blit(text, (210,250))
            audio_explosao.play()
            audio_explosao.set_volume(0.01)
            (ret.left, ret.top) = (xant, yant)
            ret2.left= 800
            ret3.left= 800
            ret4.left= 800
            ret4.left= 800
            ret4_1.left= 800
            ret5.left=800
            ret5_1.left= 800
            ret6.left= 800
            ret6_1.left= 800
            ret7.left= 800
            ret7_1.left= 800
            ret8.left= 800
            ret9.left= 800
                        
        if ret.colliderect(ret7_1):
            text = font_perdeu.render('Você Perdeu', 1, (255, 255, 255))
            tela.blit(text, (215,200))
            text = font_recomecar.render('Clique para recomeçar', 1, (0, 0, 0))
            tela.blit(text, (210,250))
            audio_explosao.play()
            audio_explosao.set_volume(0.01)
            (ret.left, ret.top) = (xant, yant)
            ret2.left= 800
            ret3.left= 800
            ret4.left= 800
            ret4.left= 800
            ret4_1.left= 800
            ret5.left=800
            ret5_1.left= 800
            ret6.left= 800
            ret6_1.left= 800
            ret7.left= 800
            ret7_1.left= 800
            ret8.left= 800
            ret9.left= 800
                        
        if ret.colliderect(ret8):
            text = font_perdeu.render('Você Perdeu', 1, (255, 255, 255))
            tela.blit(text, (215,200))
            text = font_recomecar.render('Clique para recomeçar', 1, (0, 0, 0))
            tela.blit(text, (210,250))
            audio_explosao.play()
            audio_explosao.set_volume(0.01)
            (ret.left, ret.top) = (xant, yant)
            ret2.left= 800
            ret3.left= 800
            ret4.left= 800
            ret4.left= 800
            ret4_1.left= 800
            ret5.left=800
            ret5_1.left= 800
            ret6.left= 800
            ret6_1.left= 800
            ret7.left= 800
            ret7_1.left= 800
            ret8.left= 800
            ret9.left= 800
                        
        if ret.colliderect(ret9):
            text = font_perdeu.render('Você Perdeu', 1, (255, 255, 255))
            tela.blit(text, (215,200))
            text = font_recomecar.render('Clique para recomeçar', 1, (0, 0, 0))
            tela.blit(text, (210,250))
            audio_explosao.play()
            audio_explosao.set_volume(0.01)
            (ret.left, ret.top) = (xant, yant)
            ret2.left= 800
            ret3.left= 800
            ret4.left= 800
            ret4.left= 800
            ret4_1.left= 800
            ret5.left=800
            ret5_1.left= 800
            ret6.left= 800
            ret6_1.left= 800
            ret7.left= 800
            ret7_1.left= 800
            ret8.left= 800
            ret9.left= 800


        if ret.right >= fim.left and ret.top >= fim.top:
            text = font_ganhou.render('Você Ganhou', 1, (255, 255, 255))
            tela.blit(text, (215,200))
            text = font_recomecar.render('Clique para recomeçar', 1, (0, 0, 0))
            tela.blit(text, (202,240))
            ret2.left= 800
            ret3.left= 800
            ret4.left= 800
            ret4.left= 800
            ret4_1.left= 800
            ret5.left=800
            ret5_1.left= 800
            ret6.left= 800
            ret6_1.left= 800
            ret7.left= 800
            ret7_1.left= 800
            ret8.left= 800
            ret9.left= 800


        pygame.draw.rect(tela, cor_azul, fim)
        pygame.draw.rect(tela, cor_amarela, ret)
        pygame.draw.rect(tela, cor_roxa, ret2)
        pygame.draw.rect(tela, cor_roxa, ret3) 
        pygame.draw.rect(tela, cor_roxa, ret4) 
        pygame.draw.rect(tela, cor_roxa, ret4_1) 
        pygame.draw.rect(tela, cor_roxa, ret5)
        pygame.draw.rect(tela, cor_roxa, ret5_1)  
        pygame.draw.rect(tela, cor_roxa, ret6)
        pygame.draw.rect(tela, cor_roxa, ret6_1)
        pygame.draw.rect(tela, cor_roxa, ret7)
        pygame.draw.rect(tela, cor_roxa, ret7_1)
        pygame.draw.rect(tela, cor_roxa, ret8)
        pygame.draw.rect(tela, cor_roxa, ret9)
        text = font_recomecar.render('FIM', 1, (255, 255, 255))
        tela.blit(text, (540,410)) 
          
        pygame.display.update()
    pygame.quit() 


main()

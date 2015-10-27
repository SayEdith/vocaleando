import pygame
import sys
import pygame.locals
from pygame.constants import *
from symbol import if_stmt

pygame.init()

ocultar = 1

class interfaz():
    
    def __init__(self):
        self.portada=pygame.image.load("img/PortadaFF.jpg")
        self.menu=pygame.image.load("img/MenuFF.jpg")
        self.btnVocales=pygame.image.load("img/Mascara_Ejercicios_Borrador.jpg")
        self.imgconsonantes=pygame.image.load("img/Consonantes_Borrador.jpg")
        self.imgact1Vocales=pygame.image.load("img/EjerVocal1.jpg")
        self.img1VocalesRevisado=pygame.image.load("img/EjerVocal1_Revi.jpg")
        self.imgact2Vocales=pygame.image.load("img/EjerVocal2.jpg")
        self.img2VocalesRevisado=pygame.image.load("img/EjerVocal2_Revi.jpg")
        self.imgact3Vocales=pygame.image.load("img/EjerVocal3.jpg")
        self.img3VocalesRevisado=pygame.image.load("img/EjerVocal3_Revi.jpg")
        self.imgact4Vocales=pygame.image.load("img/EjerVocal4.jpg")
        self.img4VocalesRevisado=pygame.image.load("img/EjerVocal4_Revi.jpg")
        self.imgact5Vocales=pygame.image.load("img/EjerVocal5.jpg")
        self.img5VocalesRevisado=pygame.image.load("img/EjerVocal5_Revi.jpg")
        self.imgact6Vocales=pygame.image.load("img/EjerVocal6.jpg")
        self.img6VocalesRevisado=pygame.image.load("img/EjerVocal6_Revi.jpg")
        self.img7Vocales=pygame.image.load("img/EjerVocal7.jpg")
        self.img7VocalesRevisado=pygame.image.load("img/EjerVocal7_Revi.jpg")
        self.img8Vocales=pygame.image.load("img/EjerVocal8.jpg")
        self.img8VocalesRevisado=pygame.image.load("img/EjerVocal8_Revi.jpg")
        self.img9Vocales=pygame.image.load("img/EjerVocal9.jpg")
        self.img9VocalesRevisado=pygame.image.load("img/EjerVocal9_Revi.jpg")
        self.img10Vocales=pygame.image.load("img/EjerVocal10.jpg")
        self.img10VocalesRevisado=pygame.image.load("img/EjerVocal10_Revi.jpg")
        self.imgMenu_consonates_cerrar=pygame.image.load(("img/Menu_Consonate_Cerrar.jpg"))
        
        self.img1consonantes=pygame.image.load("img/EjerConsonante1.jpg")
        self.imgconsonates1_Revi=pygame.image.load("img/EjerConsonante1_Revi.jpg")
        self.img2consonantes=pygame.image.load("img/EjerConsonante2.jpg")
        self.imgconsonantes2_Revi=pygame.image.load("img/EjerConsonante2_Revi.jpg")
        self.img3consonantes=pygame.image.load("img/EjerConsonante3.jpg")
        self.imgconsonates3_Revi=pygame.image.load("img/EjerConsonante3_Revi.jpg")
        self.img4consonantes=pygame.image.load("img/EjerConsonante4.jpg")
        self.imgconsonates4_Revi=pygame.image.load("img/EjerConsonante4_Revi.jpg")
        self.img5consonantes=pygame.image.load("img/EjerConsonante5.jpg")
        self.imgconsonantes5_Revi=pygame.image.load("img/EjerConsonante5_Revi.jpg")
        self.img6consonantes=pygame.image.load("img/EjerConsonante6.jpg")
        self.imgconsonantes6_Revi=pygame.image.load("img/EjerConsonante6_Revi.jpg")
        
        self.img1consonantesMP1=pygame.image.load("img/EjerConsonanteMP1.jpg")
        self.imgconsonantesMP1_Revi=pygame.image.load("img/EjerConsonanteMP1_Revi.jpg")
        self.img2consonantesMP2=pygame.image.load("img/EjerConsonanteMP2.jpg")
        self.imgconsonantesMP2_Revi=pygame.image.load("img/EjerConsonanteMP2_Revi.jpg")
        self.img3consonantesMP3=pygame.image.load("img/EjerConsonanteMP3.jpg")
        self.imgconsonantesMP3_Revi=pygame.image.load("img/EjerConsonanteMP3_Revi.jpg")
        
        self.img1consonantePM1=pygame.image.load("img/EjerConsonantePM1.jpg")
        self.imgconsonantesPM1_Revi=pygame.image.load("img/EjerConsonantePM1_Revi.jpg")
        self.img2consonantesPM2=pygame.image.load("img/EjerConsonantePM2.jpg")
        self.imgconsonantesPM2_Revi=pygame.image.load("img/EjerConsonantePM2_Revi.jpg")
        self.imgconsonantesPM3=pygame.image.load("img/EjerConsonantePM3.jpg")
        self.img3consonantesPM3=pygame.image.load("img/EjerConsonantePM3_Revi.jpg")
        
        self.imgFinal=pygame.image.load("img/fin.jpg")
        
        
        
    def inter_principal(self, superficie, texto): #ventana 1 principal
        
        superficie.blit(self.portada,(0,0))
        self.portada=pygame.transform.scale(self.portada,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
        
                if (x_mouse > 506 and x_mouse <= 681) and (y_mouse > 410 and y_mouse < 505) :
            
                    superficie.blit(self.menu,(0,0))
            
                    ocultar=2
            
    def interfaz_dos(self, superficie, texto):#Segunda interfaz de la aplicacion, presenta las opciones de
        #los botones vocal y consonantes
        
        superficie.blit(self.menu, (0,0))
        #self.menu=pygame.transform.scale(self.menu,(1200,845))
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
        
                if (x_mouse > 702 and x_mouse <= 808) and (y_mouse > 244 and y_mouse < 315) :
        
                    ocultar = 3
                elif (x_mouse > 772 and x_mouse <= 879) and (y_mouse > 458 and y_mouse < 529) :
                    ocultar=4
    
    def interfaz_tres(self,superficie):#ventana principal de las vocales, despues de hacer clic
        
        superficie.blit(self.btnVocales,(0,0))
        self.btnVocales=pygame.transform.scale(self.btnVocales,(1200,845))
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                if (x_mouse > 1002 and x_mouse <= 1122) and (y_mouse > 660 and y_mouse < 762) :
        
                    ocultar=5
            
    def interfaz_cuatro(self,superficie):#ventana principal al hacer clic en el boton consonates
        
        superficie.blit(self.imgconsonantes,(0,0))
        self.imgconsonantes=pygame.transform.scale(self.imgconsonantes,(1200,845))
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                if (x_mouse > 1034 and x_mouse <= 1159) and (y_mouse > 130 and y_mouse < 246) :
            
                    ocultar=5
                if (x_mouse > 1034 and x_mouse <= 1159) and (y_mouse > 130 and y_mouse < 246) :
                    
                    ocultar=5.1
            
    def interfaz_cinco(self,superficie):#ventana del primer ejercicio de las vocales. 
        
        superficie.blit(self.imgact1Vocales,(0,0))
        self.imgact1Vocales=pygame.transform.scale(self.imgact1Vocales,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                if (x_mouse > 687 and x_mouse <= 789) and (y_mouse > 215 and y_mouse < 305) :
                    ocultar=11
                    
                elif (x_mouse > 687 and x_mouse <= 789) and (y_mouse > 330 and y_mouse < 422) :
                    ocultar=11  
                    
                elif (x_mouse > 687 and x_mouse <= 789) and (y_mouse > 452 and y_mouse < 543) :
                    ocultar=11
                    
                elif (x_mouse > 687 and x_mouse <= 789) and (y_mouse > 570 and y_mouse < 663) :
                    ocultar=11
                    
                elif (x_mouse > 687 and x_mouse <= 789) and (y_mouse > 688 and y_mouse < 779) :
                    ocultar=11
              
    def interfaz_seis(self,superficie):#img bueno
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.img1VocalesRevisado,(0,0))
        self.img1VocalesRevisado=pygame.transform.scale(self.img1VocalesRevisado,(1200,845))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1001 and x_mouse <= 1125) and (y_mouse > 657 and y_mouse < 770):
                    ocultar=13
          
    def interfaz_siete(self,superficie):
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.imgact2Vocales,(0,0))
        self.imgact2Vocales=pygame.transform.scale(self.imgact2Vocales,(1200,845))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 688 and x_mouse <= 788) and (y_mouse > 215 and y_mouse < 306) :
                    ocultar=14
                    
                elif (x_mouse > 688 and x_mouse <= 788) and (y_mouse > 334 and y_mouse < 424) :
                    ocultar=14  
                    
                elif (x_mouse > 688 and x_mouse <= 788) and (y_mouse > 453 and y_mouse < 543) :
                    ocultar=14
                    
                elif (x_mouse > 688 and x_mouse <= 788) and (y_mouse > 573 and y_mouse < 664) :
                    ocultar=14
                    
                elif (x_mouse > 688 and x_mouse <= 788) and (y_mouse > 690 and y_mouse < 780) :
                    ocultar=14
                    
    def interfaz_ocho(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.img2VocalesRevisado,(0,0))
        self.img2VocalesRevisado=pygame.transform.scale(self.img2VocalesRevisado,(1200,845))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1004 and x_mouse <= 1124) and (y_mouse > 657 and y_mouse < 770):
                    ocultar=15
      
    def interfaz_nueve(self,superficie):#actividad 3 de las vocales
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.imgact3Vocales,(0,0)) 
        self.imgact3Vocales=pygame.transform.scale(self.imgact3Vocales,(1200,845)) 
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 666 and x_mouse <= 800) and (y_mouse > 207 and y_mouse < 318) :
                    ocultar=16
                    
                elif (x_mouse > 666 and x_mouse <= 800) and (y_mouse > 327 and y_mouse < 437) :
                    ocultar=16  
                    
                elif (x_mouse > 666 and x_mouse <= 800) and (y_mouse > 457 and y_mouse < 566) :
                    ocultar=16
                    
                elif (x_mouse > 666 and x_mouse <= 800) and (y_mouse > 580 and y_mouse < 689) :
                    ocultar=16
                    
                elif (x_mouse > 666 and x_mouse <= 800) and (y_mouse > 701 and y_mouse < 812) :
                    ocultar=16
      
    def interfaz_diez(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.img3VocalesRevisado,(0,0))
        self.img3VocalesRevisado=pygame.transform.scale(self.img3VocalesRevisado,(1200,845))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1002 and x_mouse <= 1125) and (y_mouse > 657 and y_mouse < 770):
                    ocultar=17
        
    def interfaz_once(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.imgact4Vocales,(0,0))
        self.imgact4Vocales=pygame.transform.scale(self.imgact4Vocales,(1200,845))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 666 and x_mouse <= 800) and (y_mouse > 204 and y_mouse < 316) :
                    ocultar=18
                    
                elif (x_mouse > 666 and x_mouse <= 800) and (y_mouse > 325 and y_mouse < 435) :
                    ocultar=18 
                     
                elif (x_mouse > 666 and x_mouse <= 800) and (y_mouse > 455 and y_mouse < 565) :
                    ocultar=18
                    
                elif (x_mouse > 666 and x_mouse <= 800) and (y_mouse > 578 and y_mouse < 688) :
                    ocultar=18
                    
                elif (x_mouse > 666 and x_mouse <= 800) and (y_mouse > 701 and y_mouse < 811) :
                    ocultar=18
        
    def interfaz_doce(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.img4VocalesRevisado,(0,0))
        self.img4VocalesRevisado=pygame.transform.scale(self.img4VocalesRevisado,(1200,845))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1004 and x_mouse <= 1124) and (y_mouse > 656 and y_mouse < 771):
                    ocultar=19
                    
    def interfaz_trece(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.imgact5Vocales,(0,0))
        self.imgact5Vocales=pygame.transform.scale(self.imgact5Vocales,(1200,845))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 690 and x_mouse <= 788) and (y_mouse > 287 and y_mouse < 356) :
                    ocultar=20
                    
                elif (x_mouse > 690 and x_mouse <= 788) and (y_mouse > 385 and y_mouse < 458) :
                    ocultar=20  
                    
                elif (x_mouse > 690 and x_mouse <= 788) and (y_mouse > 489 and y_mouse < 561) :
                    ocultar=20
                    
                elif (x_mouse > 690 and x_mouse <= 788) and (y_mouse > 597 and y_mouse < 669) :
                    ocultar=20
                    
                elif (x_mouse > 690 and x_mouse <= 788) and (y_mouse > 700 and y_mouse < 772) :
                    ocultar=20
                    
    def interfaz_catorce(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.img5VocalesRevisado,(0,0))
        self.img5VocalesRevisado=pygame.transform.scale(self.img5VocalesRevisado,(1200,845))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1004 and x_mouse <= 1124) and (y_mouse > 658 and y_mouse < 769):
                    ocultar=21
                    
    def interfaz_quince(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.imgact6Vocales,(0,0))
        self.imgact6Vocales=pygame.transform.scale(self.imgact6Vocales,(1200,845))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 690 and x_mouse <= 788) and (y_mouse > 302 and y_mouse < 380) :
                    ocultar=22
                    
                elif (x_mouse > 690 and x_mouse <= 788) and (y_mouse > 411 and y_mouse < 487) :
                    ocultar=22  
                    
                elif (x_mouse > 690 and x_mouse <= 788) and (y_mouse > 521 and y_mouse < 598) :
                    ocultar=22
                    
                elif (x_mouse > 690 and x_mouse <= 788) and (y_mouse > 636 and y_mouse < 713) :
                    ocultar=22
                    
                elif (x_mouse > 690 and x_mouse <= 788) and (y_mouse > 745 and y_mouse < 823) :
                    ocultar=22
                    
    def interfaz_dieciseis(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.img6VocalesRevisado,(0,0))
        self.img6VocalesRevisado=pygame.transform.scale(self.img6VocalesRevisado,(1200,845))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1004 and x_mouse <= 1124) and (y_mouse > 657 and y_mouse < 773):
                    ocultar=23
                    
    def interfaz_diecisiete(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.img7Vocales,(0,0))
        self.img7Vocales=pygame.transform.scale(self.img7Vocales,(1200,845))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 665 and x_mouse <= 786) and (y_mouse > 247 and y_mouse < 332) :
                    ocultar=24
                    
                elif (x_mouse > 665 and x_mouse <= 786) and (y_mouse > 356 and y_mouse < 441) :
                    ocultar=24  
                    
                elif (x_mouse > 665 and x_mouse <= 786) and (y_mouse > 466 and y_mouse < 553) :
                    ocultar=24
                    
                elif (x_mouse > 665 and x_mouse <= 786) and (y_mouse > 576 and y_mouse < 661) :
                    ocultar=24
                    
                elif (x_mouse > 665 and x_mouse <= 786) and (y_mouse > 687 and y_mouse < 772) :
                    ocultar=24
    def interfaz_dieciocho(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.img7VocalesRevisado,(0,0))
        self.img7VocalesRevisado=pygame.transform.scale(self.img7VocalesRevisado,(1200,845))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1004 and x_mouse <= 1124) and (y_mouse > 658 and y_mouse < 770):
                    ocultar=25
    def interfaz_diecinueve(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.img8Vocales,(0,0))
        self.img8Vocales=pygame.transform.scale(self.img8Vocales,(1200,845))
        
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 665 and x_mouse <= 786) and (y_mouse > 246 and y_mouse < 331) :
                    ocultar=26
                    
                elif (x_mouse > 665 and x_mouse <= 786) and (y_mouse > 355 and y_mouse < 440) :
                    ocultar=26  
                    
                elif (x_mouse > 665 and x_mouse <= 786) and (y_mouse > 466 and y_mouse < 552) :
                    ocultar=26
                    
                elif (x_mouse > 665 and x_mouse <= 786) and (y_mouse > 575 and y_mouse < 660) :
                    ocultar=26
                    
                elif (x_mouse > 665 and x_mouse <= 786) and (y_mouse > 686 and y_mouse < 771) :
                    ocultar=26
    def interfaz_veinte(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.img8VocalesRevisado,(0,0))
        self.img8VocalesRevisado=pygame.transform.scale(self.img8VocalesRevisado,(1200,845))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1004 and x_mouse <= 1124) and (y_mouse > 658 and y_mouse < 770):
                    ocultar=27
    def interfaz_veinte_uno(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.img9Vocales,(0,0))
        self.img9Vocales=pygame.transform.scale(self.img9Vocales,(1200,845))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 688 and x_mouse <= 797) and (y_mouse > 268 and y_mouse < 352) :
                    ocultar=28
                    
                elif (x_mouse > 688 and x_mouse <= 797) and (y_mouse > 376 and y_mouse < 459) :
                    ocultar=28  
                    
                elif (x_mouse > 688 and x_mouse <= 797) and (y_mouse > 484 and y_mouse < 567) :
                    ocultar=28
                    
                elif (x_mouse > 688 and x_mouse <= 797) and (y_mouse > 588 and y_mouse < 673) :
                    ocultar=28
                    
                elif (x_mouse > 688 and x_mouse <= 797) and (y_mouse > 698 and y_mouse < 782) :
                    ocultar=28
    def interfaz_veinte_dos(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.img9VocalesRevisado,(0,0))
        self.img9VocalesRevisado=pygame.transform.scale(self.img9VocalesRevisado,(1200,845))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1004 and x_mouse <= 1124) and (y_mouse > 658 and y_mouse < 770):
                    ocultar=29
    def interfaz_veinte_tres(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.img10Vocales,(0,0))
        self.img10Vocales=pygame.transform.scale(self.img10Vocales,(1200,845))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 686 and x_mouse <= 795) and (y_mouse > 267 and y_mouse < 351) :
                    ocultar=30
                    
                elif (x_mouse > 686 and x_mouse <= 795) and (y_mouse > 375 and y_mouse < 460) :
                    ocultar=30  
                    
                elif (x_mouse > 686 and x_mouse <= 795) and (y_mouse > 483 and y_mouse < 567) :
                    ocultar=30
                    
                elif (x_mouse > 686 and x_mouse <= 795) and (y_mouse > 588 and y_mouse < 672) :
                    ocultar=30
                    
                elif (x_mouse > 686 and x_mouse <= 795) and (y_mouse > 697 and y_mouse < 780) :
                    ocultar=30
    def interfaz_veinte_cuatro(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.img10VocalesRevisado,(0,0))
        self.img10VocalesRevisado=pygame.transform.scale(self.img10VocalesRevisado,(1200,845))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1004 and x_mouse <= 1124) and (y_mouse > 657 and y_mouse < 771):
                    ocultar=31
    def interfaz_veinte_cinco(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        superficie.blit(self.imgMenu_consonates_cerrar,(0,0))
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 702 and x_mouse <= 810) and (y_mouse > 263 and y_mouse < 333):
                    ocultar=32
                elif (x_mouse > 544 and x_mouse <= 629) and (y_mouse > 541 and y_mouse < 639):
                    sys.exit(0)
    def interfaz_veinte_seis(self,superficie):
        superficie.blit(self.img1consonantes,(0,0))
        self.img1consonantes=pygame.transform.scale(self.img1consonantes,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 262 and x_mouse <= 368) and (y_mouse > 515 and y_mouse < 614):
                    ocultar=33
                elif (x_mouse > 262 and x_mouse <= 368) and (y_mouse > 633 and y_mouse < 732):
                    ocultar=33
                    
    def interfaz_veinte_siete(self,superficie):
        superficie.blit(self.imgconsonates1_Revi,(0,0))
        self.imgconsonates1_Revi=pygame.transform.scale(self.imgconsonates1_Revi,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1031 and x_mouse <= 1154) and (y_mouse > 130 and y_mouse < 246):
                    ocultar=34
    def interfaz_veinte_ocho(self,superficie):
        superficie.blit(self.img2consonantes,(0,0))
        self.img2consonantes=pygame.transform.scale(self.img2consonantes,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 253 and x_mouse <= 400) and (y_mouse >517  and y_mouse < 637):
                    ocultar=35
                elif (x_mouse > 253 and x_mouse <= 400) and (y_mouse > 648 and y_mouse < 768):
                    ocultar=35
    def interfaz_veinte_nueve(self,superficie):
        superficie.blit(self.imgconsonantes2_Revi,(0,0))
        self.imgconsonantes2_Revi=pygame.transform.scale(self.imgconsonantes2_Revi,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1031 and x_mouse <= 1156) and (y_mouse >132  and y_mouse < 247):
                    ocultar=36
    def interfaz_treinta(self,superficie):
        superficie.blit(self.img3consonantes,(0,0))
        self.img3consonantes=pygame.transform.scale(self.img3consonantes,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 211 and x_mouse <= 361) and (y_mouse >530  and y_mouse < 645):
                    ocultar=37
                if (x_mouse > 211 and x_mouse <= 361) and (y_mouse >668  and y_mouse < 785):
                    ocultar=37
    def interfaz_treinta_uno(self,superficie):
        superficie.blit(self.imgconsonates3_Revi,(0,0))
        self.imgconsonates3_Revi=pygame.transform.scale(self.imgconsonates3_Revi,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1031 and x_mouse <= 1156) and (y_mouse >133  and y_mouse < 247):
                    ocultar=38
    def interfaz_treinta_dos(self,superficie):
        superficie.blit(self.img4consonantes,(0,0))
        self.img4consonantes=pygame.transform.scale(self.img4consonantes,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 278 and x_mouse <= 383) and (y_mouse >508  and y_mouse < 608):
                    ocultar=39
                if (x_mouse > 278 and x_mouse <= 383) and (y_mouse >626  and y_mouse < 723):
                    ocultar=39
    def interfaz_treinta_tres(self,superficie):
        superficie.blit(self.imgconsonates4_Revi,(0,0))
        self.imgconsonates4_Revi=pygame.transform.scale(self.imgconsonates4_Revi,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1032 and x_mouse <= 1155) and (y_mouse >129  and y_mouse < 245):
                    ocultar=40
    def interfaz_treinta_cuatro(self,superficie):
        superficie.blit(self.img5consonantes,(0,0))
        self.img5consonantes=pygame.transform.scale(self.img5consonantes,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 265 and x_mouse <= 592) and (y_mouse >525  and y_mouse < 640):
                    ocultar=41
                if (x_mouse > 265 and x_mouse <= 592) and (y_mouse >664  and y_mouse < 780):
                    ocultar=41
    def interfaz_treinta_cinco(self,superficie):
        superficie.blit(self.imgconsonantes5_Revi,(0,0))
        self.imgconsonantes5_Revi=pygame.transform.scale(self.imgconsonantes5_Revi,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1031 and x_mouse <= 1155) and (y_mouse >130  and y_mouse < 245):
                    ocultar=42
    def interfaz_treinta_seis(self,superficie):
        superficie.blit(self.img6consonantes,(0,0))
        self.img6consonantes=pygame.transform.scale(self.img6consonantes,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 277 and x_mouse <= 423) and (y_mouse >521  and y_mouse < 640):
                    ocultar=43
                if (x_mouse > 277 and x_mouse <= 423) and (y_mouse >671  and y_mouse < 789):
                    ocultar=43
    def interfaz_treinta_siete(self,superficie):
        superficie.blit(self.imgconsonantes6_Revi,(0,0))
        self.imgconsonantes6_Revi=pygame.transform.scale(self.imgconsonantes6_Revi,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1032 and x_mouse <= 1156) and (y_mouse >130  and y_mouse < 245):
                    ocultar=44
    def interfaz_treinta_ocho(self,superficie):
        superficie.blit(self.img1consonantesMP1,(0,0))
        self.img1consonantesMP1=pygame.transform.scale(self.img1consonantesMP1,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 169 and x_mouse <= 445) and (y_mouse >536  and y_mouse < 655):
                    ocultar=45
                if (x_mouse > 169 and x_mouse <= 445) and (y_mouse >667  and y_mouse < 785):
                    ocultar=45
    def interfaz_treinta_nueve(self,superficie):
        superficie.blit(self.imgconsonantesMP1_Revi,(0,0))
        self.imgconsonantesMP1_Revi=pygame.transform.scale(self.imgconsonantesMP1_Revi,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1032 and x_mouse <= 1156) and (y_mouse >130  and y_mouse < 245):
                    ocultar=46
    def interfaz_cuarenta(self,superficie):
        superficie.blit(self.img2consonantesMP2,(0,0))
        self.img2consonantesMP2=pygame.transform.scale(self.img2consonantesMP2,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 188 and x_mouse <= 593) and (y_mouse >544  and y_mouse < 644):
                    ocultar=46.1
                if (x_mouse > 188 and x_mouse <= 593) and (y_mouse >680  and y_mouse < 782):
                    ocultar=46.1
    def interfaz_cuarenta_1(self,superficie):
        superficie.blit(self.imgconsonantesMP2_Revi,(0,0))
        self.imgconsonantesMP2_Revi=pygame.transform.scale(self.imgconsonantesMP2_Revi,(1200,845))
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1032 and x_mouse <= 1156) and (y_mouse >130  and y_mouse < 245):
                    ocultar=46.2
        
        
    def interfaz_cuarenta_uno(self,superficie):
        superficie.blit(self.img3consonantesMP3,(0,0))
        self.img3consonantesMP3=pygame.transform.scale(self.img3consonantesMP3,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 178 and x_mouse <= 502) and (y_mouse >506  and y_mouse < 644):
                    ocultar=47
                if (x_mouse > 178 and x_mouse <= 502) and (y_mouse >660  and y_mouse < 806):
                    ocultar=47
    def interfaz_cuarenta_dos(self,superficie):
        superficie.blit(self.imgconsonantesMP3_Revi,(0,0))
        self.imgconsonantesMP3_Revi=pygame.transform.scale(self.imgconsonantesMP3_Revi,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1032 and x_mouse <= 1156) and (y_mouse >130  and y_mouse < 245):
                    ocultar=48
    def interfaz_cuarenta_tres(self,superficie):
        superficie.blit(self.img1consonantePM1,(0,0))
        self.img1consonantePM1=pygame.transform.scale(self.img1consonantePM1,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 189 and x_mouse <= 422) and (y_mouse >545  and y_mouse < 642):
                    ocultar=49
                if (x_mouse > 189 and x_mouse <= 422) and (y_mouse >686  and y_mouse < 783):
                    ocultar=49
    def interfaz_cuarenta_cuatro(self,superficie):
        superficie.blit(self.imgconsonantesPM1_Revi,(0,0))
        self.imgconsonantesPM1_Revi=pygame.transform.scale(self.imgconsonantesPM1_Revi,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1032 and x_mouse <= 1156) and (y_mouse >130  and y_mouse < 245):
                    ocultar=50
    def interfaz_cuarenta_cinco(self,superficie):
        superficie.blit(self.img2consonantesPM2,(0,0))
        self.img2consonantesPM2=pygame.transform.scale(self.img2consonantesPM2,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 168 and x_mouse <= 596) and (y_mouse >537  and y_mouse < 652):
                    ocultar=51
                if (x_mouse > 168 and x_mouse <= 596) and (y_mouse >664  and y_mouse < 779):
                    ocultar=51
    def interfaz_cuarenta_seis(self,superficie):
        superficie.blit(self.imgconsonantesPM2_Revi,(0,0))
        self.imgconsonantesPM2_Revi=pygame.transform.scale(self.imgconsonantesPM2_Revi,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1032 and x_mouse <= 1156) and (y_mouse >130  and y_mouse < 245):
                    ocultar=52
    def interfaz_cuarenta_siete(self,superficie):
        superficie.blit(self.imgconsonantesPM3,(0,0))
        self.imgconsonantesPM3=pygame.transform.scale(self.imgconsonantesPM3,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 169 and x_mouse <= 610) and (y_mouse >546  and y_mouse < 660):
                    ocultar=53
                if (x_mouse > 169 and x_mouse <= 610) and (y_mouse >684  and y_mouse < 800):
                    ocultar=53
    def interfaz_cuarenta_ocho(self,superficie):
        superficie.blit(self.img3consonantesPM3,(0,0))
        self.img3consonantesPM3=pygame.transform.scale(self.img3consonantesPM3,(1200,845))
        
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                
                if (x_mouse > 1031 and x_mouse <= 1153) and (y_mouse >131  and y_mouse < 246):
                    ocultar=54
    def interfaz_cuarenta_nueve(self,superficie):
        superficie.blit(self.imgFinal,(0,0))
        self.imgFinal=pygame.transform.scale(self.imgFinal,(1200,845))
        
        
        
def main():
    
    global ocultar
    x_mouse, y_mouse = pygame.mouse.get_pos()
    ventana = pygame.display.set_mode((1200,845))
    
    prin=interfaz()
    
    while True:
       
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                if(ocultar==1):
                    prin.poscision_elementos_1(ventana)
    
            elif eventos.type == KEYDOWN:
                
                if eventos.key == K_ESCAPE:
                    
                    sys.exit(0)        
                               
        if(ocultar==1):
            prin.inter_principal(ventana,"Ventana principal")
        elif (ocultar==2):
            prin.interfaz_dos(ventana, "Esta es mi ventana 2")
        elif (ocultar==3):
            prin.interfaz_tres(ventana)
        elif (ocultar==4):
            prin.interfaz_cuatro(ventana) 
        elif (ocultar==5):
            prin.interfaz_cinco(ventana)
        elif (ocultar==5.1):
            prin.interfaz_veinte_seis(ventana)
        elif(ocultar==6):
            prin.interfaz_dos(ventana,"Esta es mi ventana 2")
        elif(ocultar==7):
            prin.interfaz_seis(ventana)
        elif(ocultar==8):
            prin.interfaz_seis(ventana)
        elif(ocultar==9):
            prin.interfaz_seis(ventana)
        elif(ocultar==10):
            prin.interfaz_seis(ventana)
        elif(ocultar==11):
            prin.interfaz_seis(ventana)
        elif(ocultar==12):
            prin.interfaz_seis(ventana)
        elif (ocultar==13):
            prin.interfaz_siete(ventana)
        elif (ocultar==14):
            prin.interfaz_ocho(ventana)
        elif (ocultar==15):
            prin.interfaz_nueve(ventana)
        elif (ocultar==16):
            prin.interfaz_diez(ventana)
        elif (ocultar==17):
            prin.interfaz_once(ventana)
        elif (ocultar==18):
            prin.interfaz_doce(ventana)
        elif (ocultar==19):
            prin.interfaz_trece(ventana)
        elif (ocultar==20):
            prin.interfaz_catorce(ventana)
        elif (ocultar==21):
            prin.interfaz_quince(ventana)
        elif (ocultar==22):
            prin.interfaz_dieciseis(ventana)
        elif(ocultar==23):
            prin.interfaz_diecisiete(ventana)
        elif(ocultar==24):
            prin.interfaz_dieciocho(ventana)
        elif(ocultar==25):
            prin.interfaz_diecinueve(ventana)
        elif(ocultar==26):
            prin.interfaz_veinte(ventana)
        elif(ocultar==27):
            prin.interfaz_veinte_uno(ventana)
        elif(ocultar==28):
            prin.interfaz_veinte_dos(ventana)
        elif(ocultar==29):
            prin.interfaz_veinte_tres(ventana)
        elif(ocultar==30):
            prin.interfaz_veinte_cuatro(ventana)
        elif(ocultar==31):
            prin.interfaz_veinte_cinco(ventana)
        elif(ocultar==32):
            prin.interfaz_veinte_seis(ventana)
        elif(ocultar==33):
            prin.interfaz_veinte_siete(ventana)
        elif(ocultar==34):
            prin.interfaz_veinte_ocho(ventana)
        elif(ocultar==35):
            prin.interfaz_veinte_nueve(ventana)
        elif(ocultar==36):
            prin.interfaz_treinta(ventana)
        elif(ocultar==37):
            prin.interfaz_treinta_uno(ventana)
        elif(ocultar==38):
            prin.interfaz_treinta_dos(ventana)
        elif(ocultar==39):
            prin.interfaz_treinta_tres(ventana)
        elif(ocultar==40):
            prin.interfaz_treinta_cuatro(ventana)
        elif(ocultar==41):
            prin.interfaz_treinta_cinco(ventana)
        elif(ocultar==42):
            prin.interfaz_treinta_seis(ventana)
        elif(ocultar==43):
            prin.interfaz_treinta_siete(ventana)
        elif(ocultar==44):
            prin.interfaz_treinta_ocho(ventana)
        elif(ocultar==45):
            prin.interfaz_treinta_nueve(ventana)
        elif(ocultar==46):
            prin.interfaz_cuarenta(ventana)
        elif(ocultar==46.1):
            prin.interfaz_cuarenta_1(ventana)
        elif(ocultar==46.2):
            prin.interfaz_cuarenta_uno(ventana)
        elif(ocultar==47):
            prin.interfaz_cuarenta_dos(ventana)
        elif(ocultar==48):
            prin.interfaz_cuarenta_tres(ventana)
        elif(ocultar==49):
            prin.interfaz_cuarenta_cuatro(ventana)
        elif(ocultar==50):
            prin.interfaz_cuarenta_cinco(ventana)
        elif(ocultar==51):
            prin.interfaz_cuarenta_seis(ventana)
        elif(ocultar==52):
            prin.interfaz_cuarenta_siete(ventana)
        elif(ocultar==53):
            prin.interfaz_cuarenta_ocho(ventana)
        elif(ocultar==54):
            prin.interfaz_cuarenta_nueve(ventana)
        pygame.display.update()
        print(x_mouse, y_mouse )            
if __name__ == '__main__':

    main()

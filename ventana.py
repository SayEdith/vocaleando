import pygame
import sys
import pygame.locals
from pygame.constants import *
from symbol import if_stmt



pygame.init()

ocultar = 1

class interfaz():
    
    def __init__(self):
        self.portada=pygame.image.load("img/portada.jpg")
        self.btnEntrar=pygame.image.load("img/Boton_Entrar.png")
        self.btnprin=pygame.image.load("img/Menu_Borrador.jpg")
        self.btnCerrar=pygame.image.load("img/Boton_Cerrar_Borrador_Menu.png")
        self.btnSiguienteMenu=pygame.image.load("img/Boton_Siguiente_Borrador_Menu.png")
        self.btnSiguienteMenucopia=pygame.image.load("img/Boton_Siguiente_Borrador_Menu - copia.png")
        self.btnVocales=pygame.image.load("img/Mascara_Ejercicios_Borrador.jpg")
        self.imgconsonantes=pygame.image.load("img/Consonantes_Borrador.jpg")
        self.imgact1Vocales=pygame.image.load("img/Vocales_act1.jpg")
        self.imgsheck=pygame.image.load("img/Yes_check.png")
        self.imgmalo=pygame.image.load("img/malo.png")
        self.btnsiguiente=pygame.image.load("img/btnsiguiente.png")
        self.imgact2Vocales=pygame.image.load("img/ejervocal2.jpg")
        
        
        self.fuente_sistema=pygame.font.SysFont("comicsansms",50)
        #self.imagen4 = pygame.image.load("img/sabiduria.png")
        #self.regresar = pygame.image.load("img/regresar.fw.png")
        
        
    def inter_principal(self, superficie, texto): #ventana 1 principal
        
        superficie.blit(self.portada,(0,0))
        self.portada=pygame.transform.scale(self.portada,(800,600))
        superficie.blit(self.btnEntrar,(335,276))
        
    def poscision_elementos_1(self, superficie):#elementos x y para la ventana 1
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 319 and x_mouse <= 457) and (y_mouse > 280 and y_mouse < 358) :
            
            superficie.blit(self.btnprin,(0,0))
            
            ocultar=2
            
            
    def interfaz_dos(self, superficie, texto):#Segunda interfaz de la aplicacion, presenta las opciones de
        #los botones vocal y consonantes
        
        superficie.blit(self.btnprin, (0,0))
        self.btnprin=pygame.transform.scale(self.btnprin,(800,600))
        #superficie.blit(self.btnSiguienteMenu,(415,162.5))
        #self.btnSiguienteMenu=pygame.transform.scale(self.btnSiguienteMenu,(80,50))
        #superficie.blit(self.btnSiguienteMenucopia,(494,286))
        #self.btnSiguienteMenucopia=pygame.transform.scale(self.btnSiguienteMenucopia,(80,50))
        #superficie.blit(self.btnCerrar,(328,418))
        #self.btnCerrar=pygame.transform.scale(self.btnCerrar,(140,140))
     
    def poscision_elementos_2(self, superficie):# posicion de los botones vocal y consonates, al hacer clic
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 468 and x_mouse <= 540) and (y_mouse > 161 and y_mouse < 213) :
        
            ocultar = 3
        elif (x_mouse > 514 and x_mouse <= 587) and (y_mouse > 305 and y_mouse < 360) :
            ocultar=4
            
    def interfaz_tres(self,superficie):#ventana principal de las vocales, despues de hacer clic
        
        superficie.blit(self.btnVocales,(0,0))
        self.btnVocales=pygame.transform.scale(self.btnVocales,(800,600))
      
    
    def poscicion_elementos_3(self,superficie): #posicion de los botones siguiente y atras de inter vocales
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 699 and x_mouse <= 786) and (y_mouse > 381 and y_mouse < 457) :
        
            ocultar=5
            
        elif (x_mouse > 444 and x_mouse <= 510) and (y_mouse > 161 and y_mouse < 213) :
            
            ocultar=7
            
          
        elif (x_mouse > 444 and x_mouse <= 510) and (y_mouse > 237 and y_mouse < 295) :
            
            ocultar=8  
        elif (x_mouse > 444 and x_mouse <= 510) and (y_mouse > 323 and y_mouse < 374) :
            
            ocultar=9
        elif (x_mouse > 444 and x_mouse <= 510) and (y_mouse > 407 and y_mouse < 459) :
            
            ocultar=10
        elif (x_mouse > 444 and x_mouse <= 510) and (y_mouse > 490 and y_mouse < 545) :
            ocultar=11
            
        elif (x_mouse>700 and x_mouse<=783)and (y_mouse>418 and y_mouse<495):
            
            ocultar=13
         
    
    def interfaz_cuatro(self,superficie):#ventana principal al hacer clic en el boton consonates
        
        superficie.blit(self.imgconsonantes,(0,0))
        self.imgconsonantes=pygame.transform.scale(self.imgconsonantes,(800,600))
         
    def poscicion_elementos_4(self,superficie):#x, y al hacer clic en el btn consonantes
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 496 and x_mouse <= 570) and (y_mouse > 286 and y_mouse < 330) :
            
            ocultar=4
          
       
    def interfaz_cinco(self,superficie):#ventana del primer ejercicio de las vocales. 
        
        superficie.blit(self.imgact1Vocales,(0,0))
        self.imgact1Vocales=pygame.transform.scale(self.imgact1Vocales,(800,600))
        
    def poscicion_elementos_5(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        
        if (x_mouse > 700 and x_mouse <= 779) and (y_mouse > 421 and y_mouse < 496) :
            
            ocultar=12
          
        elif (x_mouse > 707 and x_mouse <= 781) and (y_mouse > 419 and y_mouse < 499) :
            #superficie.blit(self.portada,(0,0))
            ocultar=13 
            
    def interfaz_seis(self,superficie):#img bueno
        superficie.blit(self.imgsheck,(550,150))
        #self.imgsheck=pygame.transform.scale(self.imgsheck,(50,50)) 
        
    def interfaz_siete(self,superficie):#img malo
        superficie.blit(self.imgmalo,(550,250))
        #self.imgmalo=pygame.transform.scale(self.imgmalo,(30,30))
        
    def interfaz_ocho(self,superficie):
        superficie.blit(self.imgmalo,(550,340))
        #self.imgmalo=pygame.transform.scale(self.imgmalo,(30,30))
        
    def interfaz_nueve(self,superficie):
        superficie.blit(self.imgmalo,(550,430))
        #self.imgmalo=pygame.transform.scale(self.imgmalo,(30,30))
        
    def interfaz_diez(self,superficie):
        
        superficie.blit(self.imgmalo,(550,520))
        #self.imgmalo=pygame.transform.scale(self.imgmalo,(30,30))
    def interfaz_once(self,superficie):
        
        superficie.blit(self.btnsiguiente,(100,520))
        #self.btnsiguiente=pygame.transform.scale(self.btnsiguiente,(30,30))
        
    def interfaz_doce(self,superficie):
        
        superficie.blit(self.imgact2Vocales,(0,0))
        #self.imgact2Vocales=pygame.transform.scale(self.imgact2Vocales,(800,600))
        
def main():
    
    global ocultar
    x_mouse, y_mouse = pygame.mouse.get_pos()
    ventana = pygame.display.set_mode((800,600))
    
    prin=interfaz()
    
    while True:
       
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
                
            elif eventos.type == MOUSEBUTTONDOWN:
                if(ocultar==1):
                    prin.poscision_elementos_1(ventana)
                    
                elif(ocultar==2):
                    prin.poscision_elementos_2(ventana)
                    
                elif (ocultar==3):
                    prin.poscicion_elementos_3(ventana)
                    
                elif (ocultar==4):
                    prin.poscicion_elementos_2(ventana)
                elif (ocultar==5):
                    prin.poscicion_elementos_3(ventana)
                elif (ocultar==6):
                    prin.poscicion_elementos_3(ventana)
                elif (ocultar==7):
                    prin.poscicion_elementos_3(ventana)
                elif (ocultar==8):
                    prin.poscicion_elementos_3(ventana)
                elif (ocultar==9):
                    prin.poscicion_elementos_3(ventana)
                elif (ocultar==10):
                    prin.poscicion_elementos_3(ventana)
                elif (ocultar==11):
                    prin.poscicion_elementos_3(ventana)
                elif (ocultar==12):
                    prin.poscicion_elementos_5(ventana)
                elif(ocultar==13):
                    prin.poscicion_elementos_5(ventana)
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
        elif(ocultar==6):
            prin.interfaz_dos(ventana,"Esta es mi ventana 2")
        elif(ocultar==7):
            prin.interfaz_seis(ventana)
            prin.interfaz_once(ventana)
        elif(ocultar==8):
            prin.interfaz_siete(ventana)
            prin.interfaz_once(ventana)
        elif(ocultar==9):
            prin.interfaz_ocho(ventana)
            prin.interfaz_once(ventana)
        elif(ocultar==10):
            prin.interfaz_nueve(ventana)
            prin.interfaz_once(ventana)
        elif(ocultar==11):
            prin.interfaz_diez(ventana)
            prin.interfaz_once(ventana)
        elif(ocultar==12):
            prin.interfaz_doce(ventana)
        elif (ocultar==13):
            prin.interfaz_doce(ventana)
        pygame.display.update()
        print(x_mouse, y_mouse )            
if __name__ == '__main__':

    main()

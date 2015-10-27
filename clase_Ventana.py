import pygame
import sys
import pygame.locals
from pygame.constants import *



pygame.init()

ocultar = 1

class interfaz():
    
    def __init__(self):
        self.portada=pygame.image.load("img/portada.jpg")
        self.btnEntrar=pygame.image.load("img/Boton_Entrar.png")
        self.btnprin=pygame.image.load("img/Menu_Borrador.png")
        self.btnCerrar=pygame.image.load("img/Boton_Cerrar_Borrador_Menu.png")
        self.btnSiguienteMenu=pygame.image.load("img/Boton_Siguiente_Borrador_Menu.png")
        self.btnSiguienteMenucopia=pygame.image.load("img/Boton_Siguiente_Borrador_Menu - copia.png")
        self.btnVocales=pygame.image.load("img/Mascara_Ejercicios_Borrador.png")
        self.imgconsonantes=pygame.image.load("img/Consonantes_Borrador.png")
        #self.imagen1 = pygame.image.load("img/boton_1.fw.png")
        #self.imagen2 = pygame.image.load("img/boton_2.fw.png")
        #self.imagen3 = pygame.image.load("img/boton_3.fw.png") 
        self.fuente_sistema=pygame.font.SysFont("comicsansms",50)
        self.imagen4 = pygame.image.load("img/sabiduria.png")
        self.regresar = pygame.image.load("img/regresar.fw.png")
        
        
         
    def inter_principal(self, superficie, texto):
        
        
        #mi_texto=self.fuente_sistema.render(texto,True,(0,255,0))
        superficie.blit(self.portada,(0,0))
        superficie.blit(self.btnEntrar,(335,276))
        
        #superficie.blit(self.imagen1, (50,0))
        #superficie.blit(self.imagen2, (50,200))
        #superficie.blit(self.imagen3, (50,500))
        #superficie.blit(mi_texto,(300,50))
        
    
    def poscision_elementos_1(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        
        if (x_mouse > 319 and x_mouse <= 457) and (y_mouse > 280 and y_mouse < 358) :
            
            superficie.blit(self.btnprin,(0,0))
            
            ocultar=2
            #superficie.fill((255,255,255))
                
        
    def interfaz_dos(self, superficie, texto):#Segunda interfaz de la aplicacion
        #mi_texto=self.fuente_sistema.render(texto,True,(0,255,0))
        superficie.blit(self.btnprin, (0,0))
        self.btnprin=pygame.transform.scale(self.btnprin,(800,600))
        superficie.blit(self.btnSiguienteMenu,(415,162.5))
        self.btnSiguienteMenu=pygame.transform.scale(self.btnSiguienteMenu,(80,50))
        superficie.blit(self.btnSiguienteMenucopia,(494,286))
        self.btnSiguienteMenucopia=pygame.transform.scale(self.btnSiguienteMenucopia,(80,50))
        superficie.blit(self.btnCerrar,(328,418))
        self.btnCerrar=pygame.transform.scale(self.btnCerrar,(140,140))
        #superficie.blit(self.regresar, (50,0))
        #superficie.blit(mi_texto,(300,50))
    
    def interfaz_tres(self,superficie):
        
        superficie.blit(self.btnVocales,(0,0))
        self.btnVocales=pygame.transform.scale(self.btnVocales,(800,600))
      

    def poscision_elementos_2(self, superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if (x_mouse > 413 and x_mouse <= 494) and (y_mouse > 160 and y_mouse < 210) :
        
            ocultar = 3
          
    def poscicion_elementos_3(self,superficie): 
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if (x_mouse > 413 and x_mouse <= 494) and (y_mouse > 200 and y_mouse < 240) :
        
            ocultar = 3
            
    def poscicion_elementos_4(self,superficie):
        global ocultar
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if (x_mouse > 496 and x_mouse <= 570) and (y_mouse > 286 and y_mouse < 330) :
            
            ocultar=4
            
    def interfaz_cuatro(self,superficie):
        
        superficie.blit(self.imgconsonantes,(0,0))
        self.imgconsonantes=pygame.transform.scale(self.imgconsonantes,(800,600))
        
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
                    
                    prin.poscicion_elementos_4(ventana)
            elif eventos.type == KEYDOWN:
                
                if eventos.key == K_ESCAPE:
                    
                    sys.exit(0)        
            
                                      
        if(ocultar==1):
            prin.inter_principal(ventana,"Ventana principal")
            #print (x_mouse, y_mouse)
        elif (ocultar==2):
            prin.interfaz_dos(ventana, "Esta es mi ventana 2")
        elif (ocultar==3):
            prin.interfaz_tres(ventana)
        elif (ocultar==4):
            prin.interfaz_cuatro(ventana) 
        pygame.display.update()
        print(x_mouse, y_mouse )            
if __name__ == '__main__':

    main()
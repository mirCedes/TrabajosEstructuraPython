# -*- coding: utf-8 -*- 
import wx
import wx.xrc
import sys
import os
import subprocess as proceso
class MainWindow(wx.Frame):
    
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800,600))
        self.CreateStatusBar() 
        # Creamos el submenu Archivo
        menuArchivo = wx.Menu()
        menuSalir = menuArchivo.Append(wx.ID_EXIT,"&Salir"," Terminar el programa")
        # Y una label con un control de texto editable al lado y dos eventos para capturar texto
        # Creamos un botón
        Descargar = wx.Button(self, label="Descargar", pos=(200, 140),size=(250, -1))#pos=(15, 100),
        self.lblname = wx.StaticText(self, label="URL", pos=(20,60))
        self.editname = wx.TextCtrl(self, value="", pos=(200, 60), size=(400,-1))
        #un combobox
        self.opciones = ['mp4 [720x1280]', 'webm [720x1280]', 'mp4 [360x640]']
        self.lblhear = wx.StaticText(self, label="Formato del video", pos=(20, 100))
        self.cbx = wx.ComboBox(self, pos=(200, 100), size=(400, -1), choices=self.opciones, style=wx.CB_DROPDOWN)
        # Creamos la barra del menu
        menuBar = wx.MenuBar()
        acercaD =wx.Menu()
        actualizarM=wx.Menu()
        ayudaM =wx.Menu()
        
         
        menuAcerca=menuBar.Append(acercaD,"Ayuda/Acerca de")
        menuActualizar=menuBar.Append(actualizarM,"Actualizar")
        menuBar.Append(menuArchivo,"Salir") 
        self.SetMenuBar(menuBar)
        #submenu
        menuAcercaDeM = acercaD.Append(wx.ID_ABOUT, "Ayuda/Acerca de"," Informacion del programa")
        menuActualizarM = actualizarM.Append(wx.ID_FILE, "Actualizar"," YouTube DL")
        
        # Creamos los eventos
        
        self.Bind(wx.EVT_BUTTON,self.descargar,Descargar)
        self.Bind(wx.EVT_MENU, self.OnExit, menuSalir)  
        self.Bind(wx.EVT_MENU, self.On, menuAcercaDeM)
        self.Bind(wx.EVT_MENU, self.Actualizar, menuActualizarM)
        self.Show(True)
    # Definimos los metodos de los eventos
    def On(self,e):
        # Creamos una ventana de dialogo
        dlg = wx.MessageDialog( self, ":::AYUDA::: \n 1- Pegue la URL del video en la caja de texto. \n 2-Seleccione el tipo de formato. \n 3-Presione el boton DESCARGAR. \n\n\n\n :::ACERCA DE::: \n Es un programa para descargar videos de YouTube :), fue elaborado en PYTHON con YouTube DL por Mirna Herrador, estudiante de Ingenieria en Sistemas Informaticos", "Info...", wx.OK)
        dlg.ShowModal() # La mostramos
        dlg.Destroy() # Finalmente la destruimos
        #Funcion swl boton para realizar descarga
    def Actualizar(self,e):
        pro = proceso.check_output(['youtube-dl','-U'])
        print pro
    def descargar(self, e):
		# Captura la url del video
        url = self.editname .GetValue()
        formato = self.cbx.GetValue()
		#descarga el video
        if formato == 'mp4 [720x1280]':
            proceso.check_output(['youtube-dl --format 22 ',url])
        elif formato=='webm [720x1280]':
            proceso.check_output(['youtube-dl --format 45 ',url])
        elif formato=='mp4 [360x640]':
            proceso.check_output(['youtube-dl --format 18 ',url])
    def OnExit(self,e):
        self.Close(True)# Cerramos el frame
         
app = wx.App(False)
frame = MainWindow(None, "YouTube DL")
app.MainLoop()

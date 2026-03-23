from PySide6.QtWidgets import QPushButton, QMainWindow, QApplication
from PySide6.QtGui import QIcon
from pathlib import Path
import webbrowser

Base_dir = Path(__file__).parent.parent

class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle ("App")
        self.resize(1080, 720)
        Boton = QPushButton ("Hola mundo")
        self.setCentralWidget(Boton)
        self.setWindowIcon (QIcon(str(Base_dir / "assets" / "Icono.png")))
        """
        """
        menu_arriba = self.menuBar()
        #///////////////////////////////////////////////////#
        Archivos = menu_arriba.addMenu("&Archivo")
        Nuevo = Archivos.addAction("Nuevo")
        Nuevo.triggered.connect(lambda: print("Nuevo"))
        #//////////////////////////////////////////////////#
        Archivos.addSeparator()
        Abrir = Archivos.addAction("Abrir")
        Abrir.triggered.connect(lambda: print("Abrir"))
        #//////////////////////////////////////////////////#
        Archivos.addSeparator()
        Guardar = Archivos.addAction("Guardar")
        Guardar.triggered.connect(lambda: print("Guardar"))
        #//////////////////////////////////////////////////#
        Archivos.addSeparator()
        Salir = Archivos.addAction("Salir")
        Salir.triggered.connect(self.close)
        #///////////////////////////////////////////////////#
        """
        """
        #////////////////////////////////////////////////////#
        Editar = menu_arriba.addMenu("&Editar")
        Editar.addAction("Insertar")
        Editar.triggered.connect(lambda: print("Insertar"))
        #////////////////////////////////////////////////////#
        Editar.addSeparator()
        Editar.addAction("Eliminar")
        Editar.triggered.connect(lambda: print("Eliminar"))
        #////////////////////////////////////////////////////# 
        Editar.addSeparator()
        Editar.addAction("deshacer")
        Editar.triggered.connect(lambda: print("Deshacer"))
        #////////////////////////////////////////////////////#
        """
        """
        #////////////////////////////////////////////////////#
        Ver = menu_arriba.addMenu("&Ver")
        Ver.addAction("Zoom +")
        Ver.triggered.connect(lambda: print("Zoom +"))
        #////////////////////////////////////////////////////#
        Ver.addSeparator()
        Ver.addAction("Zoom -")
        Ver.triggered.connect(lambda: print("Zoom -"))
        #////////////////////////////////////////////////////#
        """
        """
        #////////////////////////////////////////////////////#
        Ayuda = menu_arriba.addMenu("&Absolutamente necesario")
        Ayuda.addAction("Visitar sitio web")
        Ayuda.triggered.connect(lambda: webbrowser.open("https://www.leagueoflegends.com/es-es/"))

        

        pantalla = QApplication.primaryScreen().geometry()
        x = (pantalla.width() - self.width()) // 2
        y = (pantalla.height() - self.height()) // 2
        self.move(x, y)
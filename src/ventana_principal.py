from PySide6.QtWidgets import QPushButton, QMainWindow
from PySide6.QtGui import QIcon
from pathlib import Path

Base_dir = Path(__file__).parent.parent

class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle ("App")
        self.resize(1080, 720)
        Boton = QPushButton ("Hola mundo")
        self.setCentralWidget(Boton)
        self.setWindowIcon (QIcon(str(Base_dir / "assets" / "Icono.png")))
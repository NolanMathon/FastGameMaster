import sys
import time
import pyautogui
from PIL import ImageGrab
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QListWidget, QVBoxLayout, QListWidgetItem, QAbstractItemView, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer, QSize
from PyQt5.QtGui import QIcon, QPixmap

session_abo = False
# Liste des maps : [x, y, page2, nom]
maps = {0: [1450, 425, False, "CERES"], 1: [1450, 730, False, "POLARIS"], 2: [425, 730, False, "HELIOS"], 3: [425, 425, False, "ARTEFACT"], 4: [425, 425, True, "SILVA"], 5: [950, 425, True, "THE CLIFF"], 6: [950, 425, False, "ATLANTIS"]}
next_page = [1005, 927] # Emplacementpage 2
pixel_x, pixel_y = 300, 160 # Bouton start
target_color = (44, 214, 255) # Couleur bouton start
map_order = [0, 1, 2, 3, 4, 5, 6]
map_number = 0

class MapOrderDialog(QDialog):
    def __init__(self, parent=None):
        super(MapOrderDialog, self).__init__(parent)
        self.setWindowTitle("Ordre des Maps")
        self.setGeometry(300, 50, 250, len(maps)*120+50) # 100, 50, 250

        layout = QVBoxLayout(self)

        self.map_list = QListWidget(self)
        self.map_list.setIconSize(QSize(200, 200))
        self.map_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.map_list.setDragDropMode(QAbstractItemView.InternalMove)
        self.map_list.setDefaultDropAction(Qt.MoveAction)
        layout.addWidget(self.map_list)

        for idx in map_order:
            item = QListWidgetItem()
            pixmap = QPixmap(f"FastGameMaster/images/{maps[idx][3].lower()}.png")
            pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
            item.setIcon(QIcon(pixmap))
            item.setSizeHint(pixmap.size())  # Ajuster la taille de l'item
            item.setData(Qt.UserRole, idx)
            self.map_list.addItem(item)

        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.accept)  # Connecter le bouton à la méthode accept pour fermer le dialogue avec succès
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.ok_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def get_order(self):
        order = []
        for index in range(self.map_list.count()):
            item = self.map_list.item(index)
            order.append(item.data(Qt.UserRole))
        return order

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(500, 560, 60, 60) # 20, 560, 60, 60

        self.button = QPushButton("ABO : OFF", self)
        self.button.clicked.connect(self.button_click)
        self.button.setStyleSheet("border: 0px; background-color: red;")
        self.button.setFixedSize(60, 60)
        self.button.move(0, 0)

        self.show()

    def button_click(self):
        global session_abo, map_order, map_number
        session_abo = not session_abo
        map_number = 0

        if session_abo:
            self.button.setText("ABO : ON")
            self.button.setStyleSheet("border: 0px; background-color: green;")
            
            # Ouvrir la boîte de dialogue pour choisir l'ordre des maps
            dialog = MapOrderDialog(self)
            if dialog.exec_():
                map_order = dialog.get_order()
                print(map_order)
        else:
            self.button.setText("ABO : OFF")
            self.button.setStyleSheet("border: 0px; background-color: red;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
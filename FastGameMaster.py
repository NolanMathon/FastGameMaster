import time
import pyautogui
import sys
from PIL import ImageGrab
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt, QTimer


session_abo = False
# Liste des maps : [x, y, page2, nom]
# CERES - POLARIS - HELIOS - ARTEFACT - SILVA - THE CLIFF - ATLANTIS
maps = {0: [1450, 425, False, "CERES"], 1: [1450, 730, False, "POLARIS"], 2: [425, 730, False, "HELIOS"], 3: [425, 425, False, "ARTEFACT"], 4: [425, 425, True, "SILVA"], 5: [950, 425, True, "THE CLIFF"], 6: [950, 425, False, "ATLANTIS"]}
next_page = [1005, 927] # Emplacement page 2
pixel_x, pixel_y = 300, 160 # Bouton start
target_color = (44, 214, 255) # Couleur bouton start
map_number = 0

# Création du bouton
class App(QWidget):
    button = ""

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # Garde la fenêtre toujours en avant-plan et sans bordure
        self.setGeometry(20, 560, 60, 60)  # Positionne la fenêtre à 20x490 avec une taille de 60x60
        self.button = QPushButton("ABO : OFF", self)
        self.button.clicked.connect(self.button_click)
        self.button.setStyleSheet("border: 0px; background-color: red;")
        self.button.setFixedSize(60, 60)
        self.button.move(0, 0)  # Positionne le bouton à l'intérieur de la fenêtre
        self.show()

    # Fonction à exécuter lorsque le bouton est cliqué
    def button_click(self):
        global session_abo, map_number
        session_abo = not session_abo
        map_number = 0

        if session_abo: 
            self.button.setText("ABO : ON");
            self.button.setStyleSheet("border: 0px; background-color: green;")
        else: 
            self.button.setText("ABO : OFF");
            self.button.setStyleSheet("border: 0px; background-color: red;")

    def is_session_abo(self):
        return self.session_abo

# Capture l'écran et obtient la couleur du pixel à la position (x, y)
def get_pixel_color(x, y):
    screen = ImageGrab.grab()
    return screen.getpixel((x, y))

# On change la map
def change_map():
    global map_number
    map_number+=1
    if map_number>6: map_number=0
    pyautogui.click(760, 365)
    time.sleep(1)
    if map_number == 4 or map_number == 5 : pyautogui.click(next_page[0], next_page[1]) # Si map page 2, on change de page
    time.sleep(1)
    pyautogui.click(maps[map_number][0], maps[map_number][1]) # On clic sur la map

def start():
    # Obtenir la couleur actuelle du pixel
    current_color = get_pixel_color(pixel_x, pixel_y)

    # Vérifier si la couleur actuelle correspond à la couleur cible
    if current_color == target_color:
        pyautogui.click(pixel_x, pixel_y) # Cliquer sur le bouton START
        if session_abo:
            time.sleep(20)
            change_map()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()

    timer = QTimer()
    timer.timeout.connect(start)
    timer.start(2000)  # Vérifier toutes les 2 secondes

    sys.exit(app.exec_())
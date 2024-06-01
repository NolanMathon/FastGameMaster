from GameMode import GameMode
from MapName import MapName


class Map:
    def __init__(self, name, gamemode, page2, posX, posY):
        self.name = name
        self.gamemode = gamemode
        self.page2 = page2
        self.posX = posX
        self.posY = posY

    def get_default_list():
        return [
            # Map de domination
            Map(MapName.CERES, GameMode.DOMINATION, False, 1450, 425),
            Map(MapName.POLARIS, GameMode.DOMINATION, False, 1450, 730),
            Map(MapName.HELIOS, GameMode.DOMINATION, False, 425, 730),
            Map(MapName.ARTEFACT, GameMode.DOMINATION, False, 425, 425),
            Map(MapName.SILVA, GameMode.DOMINATION, True, 425, 425),
            Map(MapName.THE_CLIFF, GameMode.DOMINATION, True, 950, 425),
            Map(MapName.ATLANTIS, GameMode.DOMINATION, False, 950, 425)
            # Match à mort par équipe
        ]
    

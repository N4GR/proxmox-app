from init.imports import *
from init.logs import setup

def Path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores the path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # If not bundled, use the original path
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class PXIcon:
    def __init__(self, path: str):
        self.path = Path(path)
        
        self.icon = QIcon(self.path)

class Screen:
    def __init__(self, app: QApplication):
        # Setting up log object.
        self.log = setup("OBJECTS.SCREEN")
        
        self.primary = app.primaryScreen()
        self.geometry = self.primary.availableGeometry()
        
        self.width = self.geometry.width()
        self.height = self.geometry.height()

class WindowAssets:
    def __init__(self, screen: Screen, relative_size: tuple[float, float], window_title: int, icon_path: str):
        self.relative_height, self.relative_width = relative_size
        
        self.height = screen.height * self.relative_height
        self.width = screen.width * self.relative_width
        
        self.title = window_title
        
        self.icon = QIcon(Path(icon_path))

class Codes:
    error = {
        0: "OK",
        1: "No input given."
    }
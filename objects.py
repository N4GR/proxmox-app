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

class MainWindowAssets:
    def __init__(self, screen: Screen):
        # Making height and width 50% of the screen width and height.
        self.height = screen.height * 0.5
        self.width = screen.width * 0.5
        
        self.title = "PROXMOX"
        
        self.px_icon = PXIcon("assets/window/proxmox.ico")
        self.icon = self.px_icon.icon

class AddressPopupAssets:
    def __init__(self, screen: Screen):
        self.height = screen.height * 0.05 # 5% of screen height.
        self.width = screen.width * 0.1 # 10% of screen width.
        
        self.title = "PROXMOX"
        
        self.px_icon = PXIcon("assets/window/proxmox.ico")
        self.icon = self.px_icon.icon
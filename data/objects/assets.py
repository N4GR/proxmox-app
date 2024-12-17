from init.imports import *
from init.logs import setup

# Creating log object.
log = setup("DATA.OBJECTS.ASSETS")

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
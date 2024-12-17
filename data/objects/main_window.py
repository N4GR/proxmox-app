from init.logs import setup

# Creating log object.
log = setup("DATA.OBJECTS.MAIN_WINDOW")

from data.objects.assets import PXIcon

class MainWindowAssets:
    def __init__(self):
        self.height = 600
        self.width = 800
        
        self.title = "PROXMOX"
        
        self.px_icon = PXIcon("assets/window/proxmox.ico")
        self.icon = self.px_icon.icon
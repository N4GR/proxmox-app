from init.logs import setup

# Creating log object.
log = setup("DATA.OBJECTS.ADDRESS_POPUP")

from data.objects.assets import PXIcon

class AddressPopupAssets:
    def __init__(self):
        self.height = 100
        self.width = 500
        
        self.title = "PROXMOX"
        
        self.px_icon = PXIcon("assets/window/proxmox.ico")
        self.icon = self.px_icon.icon
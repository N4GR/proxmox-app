from init.imports import *
from init.logs import setup

# Local imports
from modules.window.main_window import MainWindow
from modules.window.address_popup import AddressPopup

class main:
    def __init__(self):
        self.log = setup("MAIN")
        self.log.info("Launching application.")
        
        self.app = QApplication(sys.argv)
        
        # Creating screen object.
        self.screen = Screen(self.app)
        
        self.address_popup = AddressPopup(self.screen)
        self.address_popup.output_signal.connect(self.address_output)
        
        # Run application event loop.
        sys.exit(self.app.exec())
    
    def address_output(self, address: str):
        # Create the window with the given address.
        self.window = MainWindow(address, self.screen)

if __name__ == "__main__":
    main() 
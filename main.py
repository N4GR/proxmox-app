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
        
        self.address_popup = AddressPopup()
        self.address_popup.output_signal.connect(self.address_output)
        
        # Run application event loop.
        sys.exit(self.app.exec())
    
    def address_output(self, address: str):
        # Create the window with the given address.
        self.window = MainWindow(address)

if __name__ == "__main__":
    main()
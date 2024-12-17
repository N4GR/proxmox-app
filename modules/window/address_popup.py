from init.imports import *
from init.logs import setup

from data.objects.address_popup import AddressPopupAssets

class AddressPopup(QWidget):
    output_signal = Signal(str)
    
    def __init__(self):
        super().__init__()
        # Creating assets object.
        self.assets = AddressPopupAssets()
        
        # Creating log object.
        self.log = setup("MODULES.WINDOW.ADDRESS_POPUP")
        self.log.info("Creating.")
        
        # Creating Label above QLineEdit.
        self.label = QLabel(text = "Proxmox Address", parent = self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Creating line edit for address input.
        self.address_input = QLineEdit(self)
        
        # Creating QPushButton to submit address input.
        self.address_input_button = QPushButton(text = "OK", parent = self)
        self.address_input_button.clicked.connect(self.emit_output) # Connecting button to signal.
        
        # Adding window design
        self.add_design()
        
        # Showing window.
        self.show()
    
    def add_design(self):
        def add_layout():
            layout = QVBoxLayout()
            self.setLayout(layout)
            
            layout.addWidget(self.label)
            layout.addWidget(self.address_input)
            layout.addWidget(self.address_input_button)
        
        def center_window():
            self.log.info("Centering.")
            
            screen_geometry = QApplication.primaryScreen().geometry()
            screen_width = screen_geometry.width()
            screen_height = screen_geometry.height()

            window_width = self.width()
            window_height = self.height()

            # Calculate the position to center the window
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2 - 100

            # Move the window to the calculated position
            self.move(x, y)
        
        add_layout()
        
        self.setGeometry(100, 100, self.assets.width, self.assets.height)
        self.setWindowIcon(self.assets.icon)
        
        self.setWindowTitle(self.assets.title)
        
        # Center the window with an Y offset of -100
        center_window()
    
    def emit_output(self):
        address = self.address_input.text()
        
        self.log.info(f"Address submitted: ({address})")
        self.output_signal.emit(address)
        
        self.close_window()
    
    def closeEvent(self, event):
        self.close_window()
        
        event.accept()
    
    def close_window(self):
        self.log.info("Closing.")
        
        self.deleteLater()
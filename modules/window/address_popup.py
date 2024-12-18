from init.imports import *
from init.logs import setup

from modules.history import History

class AddressPopup(QWidget):
    output_signal = Signal(str)
    
    def __init__(self, screen: Screen):
        super().__init__()
        # Creating assets object.
        self.assets = AddressPopupAssets(screen)
        
        # Creating log object.
        self.log = setup("MODULES.WINDOW.ADDRESS_POPUP")
        self.log.info("Creating.")
        
        # Creating the history object.
        self.history = History()
        
        # Creating Label above QLineEdit.
        self.label = ALabel(self)
        
        # Creating line edit for address input.
        self.address_box = AComboBox(self, self.history)
        
        # Creating QPushButton to submit address input.
        self.address_input_button = APushButton(self)
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
            layout.addWidget(self.address_box)
            layout.addWidget(self.address_input_button, alignment = Qt.AlignmentFlag.AlignCenter) # Add widget and align to center.
        
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
        address = self.address_box.currentText()
        
        # Add the address to history.
        self.history.add_item(address)
        
        self.log.info(f"Address submitted: ({address})")
        self.output_signal.emit(address)
        
        self.close_window()
    
    def closeEvent(self, event):
        self.close_window()
        
        event.accept()
    
    def close_window(self):
        self.log.info("Closing.")
        
        self.deleteLater()

class ALabel(QLabel):
    def __init__(self, parent: QWidget | QMainWindow):
        super().__init__()
        self.setParent(parent)
        self.setText("PROXMOX ADDRESS")
        
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

class AComboBox(QComboBox):
    def __init__(self, parent: QWidget | QMainWindow, history: History):
        super().__init__()
        self.setParent(parent)
        self.setEditable(True)
        
        self.addItems(history.json)
            
class APushButton(QPushButton):
    def __init__(self, parent: QWidget | QMainWindow):
        super().__init__()
        self.setParent(parent)
        self.setText("OK")
        
        self.setFixedWidth(parent.width() * 0.1) # 10% of window width
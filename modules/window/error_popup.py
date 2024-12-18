from init.imports import *
from init.logs import setup

class ErrorPopup(QWidget):
    def __init__(self, screen: Screen, error_code: int):
        super().__init__()
        # Variable placeholders to self.
        self.h_layout : QVBoxLayout = None
        
        # Creating log object.
        self.log = setup("MODULES.WINDOW.ERROR_POPUP")
        
        self.error_code = error_code
        
        # Getting error code message.
        self.error_message = Codes.error[self.error_code]
        
        self.log.info(f"Creating error popup ({self.error_code}): {self.error_message}")
        
        # Creating assets object.
        self.assets = WindowAssets(
            screen = screen,
            relative_size = (0.05, 0.1),
            window_title = "PROXMOX",
            icon_path = "assets/window/proxmox.ico"
        )
        
        # Setting screen object.
        self.main_screen = screen
        
        # Adding QWidgets to ErrorPopup
        self.label = ErrorLabel(self, self.error_message)
        self.button = ErrorButton(self)
        
        # Adding the design
        self.add_design()
        
        # Showing Popup.
        self.show()
    
    def add_design(self):
        def add_layout():
            self.h_layout = QVBoxLayout()
            self.setLayout(self.h_layout)
            
            # Adding widgets to layout.
            self.h_layout.addWidget(self.label, alignment = Qt.AlignmentFlag.AlignCenter)
            self.h_layout.addWidget(self.button, alignment = Qt.AlignmentFlag.AlignCenter)

        self.setFixedHeight(self.assets.height) # 5% of main screen height
        self.setFixedWidth(self.assets.width) # 10% of main screen width
        
        self.setWindowTitle(self.assets.title)
        
        self.setWindowIcon(self.assets.icon)
        
        add_layout()
    
class ErrorLabel(QLabel):
    def __init__(self, parent: QWidget | QMainWindow, error_message: str):
        super().__init__()
        self.setParent(parent)
        
        self.error_message = error_message
        
        self.add_design()
        
    def add_design(self):
        self.setText(self.error_message)

class ErrorButton(QPushButton):
    def __init__(self, parent: QWidget | QMainWindow):
        super().__init__()
        self.setParent(parent)
        
        self.add_design()
        
        self.clicked.connect(self.on_clicked)
    
    def add_design(self):
        self.setText("OK")
    
    def on_clicked(self):
        # Delete the parent on clicked.
        self.parent().deleteLater()
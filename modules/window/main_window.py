from init.imports import *
from init.logs import setup

# Local imports
from modules.web_engine import WebEngine
from data.objects.main_window import MainWindowAssets

class MainWindow(QMainWindow):
    def __init__(self, address: str):
        super().__init__()
        # Creating log object.
        self.log = setup("MODULES.WINDOW.MAIN_WINDOW")
        self.log.info("Creating.")
        
        self.address = address
        
        # Initialise main window assets object.
        self.assets = MainWindowAssets()
        
        # Adding window design
        self.add_design()

        # Create a QWebEngineView to display the webpage
        self.browser = WebEngine()

        self.setCentralWidget(self.browser)

        # Set the URL of the website you want to open
        self.browser.setUrl(self.address)  # Replace with your URL (HTTP or invalid SSL)

        # Show the window
        self.show()
    
    def add_design(self):
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
            
        self.setWindowTitle(self.assets.title)
        self.setGeometry(100, 100, self.assets.width, self.assets.height)
        
        self.setWindowIcon(self.assets.icon)
        
        # Center the window with an Y offset of -100
        center_window()
    
    def closeEvent(self, event):
        self.log.info("Closing main window.")
        
        self.browser.close_engine()
        
        event.accept()
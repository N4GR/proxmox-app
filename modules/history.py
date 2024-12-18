from init.imports import *
from init.logs import setup

# Creating log object.
log = setup("MODULES.HISTORY")

class History:
    def __init__(self):
        self.directory = "data"
        self.file = "history.json"
        self.full_path = os.path.join(self.directory, self.file)
        
        self.template = {
            "history": []
        }
        
        self.json = []
        self.exists = False
        
        if self.check_directory() is True:
            self.exists = self.check_exist()
        
        if self.exists is True:
            self.json = self.get_history()
    
    def check_directory(self) -> bool:
        if not os.path.exists(self.directory):
            try:
                os.makedirs(self.directory)
                
                return True
            except Exception as error:
                log.error(error)
                return False
        else:
            return True
    
    def check_exist(self) -> bool:
        def create_json() -> bool:
            try:
                with open(self.full_path, "w") as file:
                    json.dump(self.template, file, indent = 4)
                
                return True
                
            except Exception as error:
                log.error(error)
                return False
        
        if os.path.isfile(self.full_path):
            return True
        else:
            create_json()
    
    def get_history(self) -> dict | bool:
        try:
            with open(self.full_path, "r") as file:
                return json.load(file)["history"]
            
        except Exception as error:
            log.error(error)
            
            return False
    
    def add_item(self, item: str):
        log.info(f"Adding to history: ({item})")
        
        # Checks if the item is already in the list.
        if item in self.json:
            log.info(f"Already in history: ({item})")
            
            # Remove it from the list.
            self.json.remove(item)
            
            # Add it to the beginning of the list.
            self.json.insert(0, item)
        else:
            # Add new item to beginning of list.
            self.json.insert(0, item)
        
        dump = {
            "history": self.json[:5] # First 5 items in list.
        }
        
        with open(self.full_path, "w") as file:
            json.dump(dump, file, indent = 4)
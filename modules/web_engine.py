from init.imports import *
from init.logs import setup

class WebEngine(QWebEngineView):
    def __init__(self):
        super().__init__()
        # Creating log object.
        self.log = setup("MODULES.WEB_ENGINE")
        self.log.info("Creating Web Engine.")
        
        # Create Engine Profile
        self.profile = self.engine_profile()
        self.web_page = self.engine_page(self.profile)
    
        self.setPage(self.web_page)
    
    def engine_profile(self) -> QWebEngineProfile:
        profile = QWebEngineProfile()
        profile.setHttpCacheType(QWebEngineProfile.HttpCacheType.MemoryHttpCache)
        
        return profile
    
    def engine_page(self, profile: QWebEngineProfile) -> QWebEnginePage:
        def ignore_ssl(error: QWebEngineCertificateError):
            error.acceptCertificate()
        
            return True
        
        page = QWebEnginePage(profile)
        page.certificateError.connect(ignore_ssl)
        
        return page
    
    def close_engine(self):
        self.log.info("Closing.")
        
        self.web_page.deleteLater()
        self.deleteLater()
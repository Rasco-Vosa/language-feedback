import yaml
from pathlib import Path 
from dotenv import load_dotenv


class Config:
    def __init__(self, config_path="config/settings.yaml", creds_path="config/.env"):
        self.config_path = Path(config_path)
        self.creds_path = Path(creds_path)
        self.settings = self.load_settings()

    def load_settings(self):
        with open(self.config_path, "r") as f:
            return yaml.safe_load(f)
    
    def load_creds(self):
        load_dotenv(self.creds_path)

    def get_setting(self, key, default=None):
        return self.settings.get(key, default)
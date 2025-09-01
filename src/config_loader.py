import yaml
from pathlib import Path

class Config:
    def __init__(self, config_path="config/settings.yaml"):
        self.config_path = Path(config_path)
        self.data = self.load_config()

    def load_config(self):
        with open(self.config_path, "r") as f:
            return yaml.safe_load(f)

    def get(self, key, default=None):
        return self.data.get(key, default)

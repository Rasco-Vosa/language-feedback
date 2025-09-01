from pathlib import Path

class InputHandler:
    def __init__(self):
        pass

    def load_text(self, file_path: str) -> str:
        path = Path(file_path)
        return path.read_text().strip()

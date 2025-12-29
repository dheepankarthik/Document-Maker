# fonts.py
import os
from PySide6.QtGui import QFontDatabase, QFont

def load_font(filename, size=12):
    base_dir = os.path.dirname(__file__)
    font_path = os.path.join(base_dir, filename)

    font_id = QFontDatabase.addApplicationFont(font_path)
    if font_id == -1:
        raise RuntimeError(f"Failed to load font: {filename}")

    family = QFontDatabase.applicationFontFamilies(font_id)[0]
    return QFont(family, size)

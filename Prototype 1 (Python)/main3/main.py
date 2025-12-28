import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import globals
import PyQt6
from PySide6.QtCore import Qt
import ui
import styles
import text_tools

app = QApplication(sys.argv)

globals.window = QWidget()
globals.window.setWindowTitle("Document Maker")
globals.window.resize(1600, 900)

buttonFrame = ui.build_ui(globals.window)

buttonLayout = QVBoxLayout(buttonFrame)

buttonLabel = QLabel("Options")

buttonLabel.setAlignment(Qt.AlignCenter)

textButton = QPushButton("Add Text")
imageButton = QPushButton("Add Image")

for element in [buttonLabel, textButton, imageButton]:
    buttonLayout.addWidget(element)

textButton.clicked.connect(text_tools.add_text_box)


def keyPressEvent(event):
    if event.key() == Qt.Key_Delete:
        text_tools.delete_selected_items()

globals.window.keyPressEvent = keyPressEvent

buttonLayout.addStretch()

globals.window.show()
sys.exit(app.exec())
import PySide6
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("Document Maker")

window.resize(400, 300)

label = QLabel("Welcome to the Document Maker")

layout = QVBoxLayout()
layout.addWidget(label, alignment=Qt.AlignTop)

window.setLayout(layout)

window.show()



sys.exit(app.exec())
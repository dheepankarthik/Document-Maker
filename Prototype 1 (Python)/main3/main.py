import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt, QRectF, QPointF
import globals
import ui_layout
import text_tools
import image_tools

app = QApplication(sys.argv)

globals.window = QWidget()
globals.window.setWindowTitle("Document Maker")
globals.window.resize(1600, 900)

buttonFrame = ui_layout.build_ui(globals.window)

buttonLayout = QVBoxLayout(buttonFrame)

textBtn = QPushButton("Text Box")
textBtn.clicked.connect(text_tools.add_text_box)

imageBtn = QPushButton("Add Image")
imageBtn.clicked.connect(image_tools.add_image)

# Selection tracking
globals.workspaceScene.selectionChanged.connect(image_tools.update_selection)

# Mouse wheel zoom
globals.workspaceCanvas.wheelEvent = image_tools.wheel_event

# Delete key for images
def key_press(event):
    if event.key() == Qt.Key_Delete:
        image_tools.delete_selected_image()
globals.window.keyPressEvent = key_press

buttonLayout.addWidget(textBtn)
buttonLayout.addWidget(imageBtn)
buttonLayout.addStretch()

globals.workspaceCanvas.wheelEvent = image_tools.wheel_event


globals.window.show()
sys.exit(app.exec())

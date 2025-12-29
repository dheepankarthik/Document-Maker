import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QGraphicsView
import PyQt6
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtCore import Qt
import ui
import styles
import text_tools
import image_tools
import globals

app = QApplication(sys.argv)

import fonts.fonts as fonts 

vendSansFont = fonts.load_font("VendSans-Medium.ttf", 10)
dosisFont = fonts.load_font("Dosis-SemiBold.ttf", 20)

globals.window = QWidget()
globals.window.setWindowTitle("Document Maker")
globals.window.resize(1600, 900)


deleteShortcut = QShortcut(QKeySequence(Qt.Key_Delete), globals.window)
deleteShortcut.setContext(Qt.ShortcutContext.WidgetWithChildrenShortcut)
deleteShortcut.activated.connect(image_tools.delete_selected_items)

ui_objects = ui.build_ui(globals.window)
buttonFrame = ui_objects["buttonFrame"]
titleLabel = ui_objects["titleLabel"]

titleLabel.setFont(dosisFont)

buttonLayout = QVBoxLayout(buttonFrame)

buttonLabel = QLabel("Options")

buttonLabel.setAlignment(Qt.AlignCenter)

textButton = QPushButton("Add Text")
imageButton = QPushButton("Add Image")

styles.apply_textBoxButton_styles(textBoxButton=textButton)



for element in [buttonLabel, textButton, imageButton]:
    element.setFont(vendSansFont)
    buttonLayout.addWidget(element)




textButton.clicked.connect(text_tools.add_text_box)

imageButton.clicked.connect(image_tools.add_image)

globals.workspaceCanvas.wheelEvent = image_tools.wheel_event

buttonLayout.addStretch()

globals.window.show()
sys.exit(app.exec())
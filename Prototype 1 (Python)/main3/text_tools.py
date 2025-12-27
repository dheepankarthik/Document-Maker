from PySide6.QtWidgets import QGraphicsTextItem
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import globals

def add_text_box():
    textItem = QGraphicsTextItem("Add text")
    textItem.setFont(QFont("Times New Roman", 14))
    textItem.setTextWidth(300)
    textItem.setTextInteractionFlags(Qt.TextEditorInteraction)
    textItem.setFlag(QGraphicsTextItem.ItemIsMovable, True)
    textItem.setFlag(QGraphicsTextItem.ItemIsSelectable, True)
    textItem.setPos(50, 50)

    globals.workspaceScene.addItem(textItem)

def delete_selected_text():
    for item in globals.workspaceScene.selectedItems():
        globals.workspaceScene.removeItem(item)

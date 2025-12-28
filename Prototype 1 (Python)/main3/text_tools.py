from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QFrame, QScrollArea, QGraphicsView, QGraphicsScene, QGraphicsTextItem, QGraphicsRectItem
)
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QColor, QFont, QPen
import globals
import styles

def add_text_box():
    text_item = QGraphicsTextItem("Enter text")
    
    text_item.setFont(QFont("Arial", 14))
    
    text_item.setTextWidth(300)

    text_item.setTextInteractionFlags(Qt.TextEditorInteraction)

    text_item.setFlag(QGraphicsTextItem.ItemIsMovable, True)
    text_item.setFlag(QGraphicsTextItem.ItemIsSelectable, True)


    text_item.setPos(50, 50)

    globals.workspaceScene.addItem(text_item)

def delete_selected_items():
    for item in globals.workspaceScene.selectedItems():
        globals.workspaceScene.removeItem(item)


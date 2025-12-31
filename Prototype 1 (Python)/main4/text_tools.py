from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QFrame, QScrollArea, QGraphicsView, QGraphicsScene, QGraphicsTextItem, QGraphicsRectItem
)
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QColor, QFont, QPen
import globals

import pages
import styles

def add_text_box():
    text_item = QGraphicsTextItem("Enter text")
    
    text_item.setFont(QFont("Arial", 14))
    
    text_item.setTextWidth(300)

    text_item.setTextInteractionFlags(Qt.TextEditorInteraction)

    text_item.setFlag(QGraphicsTextItem.ItemIsMovable, True)
    text_item.setFlag(QGraphicsTextItem.ItemIsSelectable, True)
    text_item.setFlag(QGraphicsTextItem.ItemIsFocusable, True)

    original_key_press = text_item.keyPressEvent

    def key_press_event(event):
        if event.key() in (Qt.Key_Delete, Qt.Key_Backspace):
            globals.workspaceScene.removeItem(text_item)
        else:
            original_key_press(event)

    text_item.keyPressEvent = key_press_event


    text_item.setPos(50, 50)

    globals.workspaceScene.addItem(text_item)
    pages.ensure_page_for_item(text_item)
    
    text_item.setFocus()
    update_scene_size(text_item)

def update_scene_size(item):
    """Ensure the scene is large enough to contain the item."""
    rect = globals.workspaceScene.sceneRect()
    item_rect = item.mapToScene(item.boundingRect()).boundingRect()
    new_rect = rect.united(item_rect)  # Union of current rect and item rect
    globals.workspaceScene.setSceneRect(new_rect)

def delete_selected_items():
    for item in globals.workspaceScene.selectedItems():
        globals.workspaceScene.removeItem(item)


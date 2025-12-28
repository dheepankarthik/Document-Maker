from PySide6.QtWidgets import QFileDialog, QGraphicsPixmapItem, QGraphicsView
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import globals

current_image_item = None

def add_image():
    """Add a new image to the canvas."""
    global current_image_item

    file_path, _ = QFileDialog.getOpenFileName(
        globals.window,
        "Select Image",
        "",
        "Images (*.png *.jpg *.jpeg *.bmp)"
    )

    if not file_path:
        return

    pixmap = QPixmap(file_path)
    if pixmap.isNull():
        return

    image_item = QGraphicsPixmapItem(pixmap)
    image_item.original_pixmap = pixmap

    # Enable drag and select
    image_item.setFlag(QGraphicsPixmapItem.ItemIsMovable, True)
    image_item.setFlag(QGraphicsPixmapItem.ItemIsSelectable, True)
    image_item.setTransformationMode(Qt.SmoothTransformation)

    # Default position
    image_item.setPos(100, 100)

    globals.workspaceScene.addItem(image_item)

    # Select the new image by default
    globals.workspaceScene.clearSelection()
    image_item.setSelected(True)
    current_image_item = image_item
    update_scene_size(image_item)

def update_scene_size(item):
    """Ensure the scene is large enough to contain the item."""
    rect = globals.workspaceScene.sceneRect()
    item_rect = item.mapToScene(item.boundingRect()).boundingRect()
    new_rect = rect.united(item_rect)  # Union of current rect and item rect
    globals.workspaceScene.setSceneRect(new_rect)

def update_selection():
    """Keep track of the currently selected image for wheel zoom."""
    global current_image_item
    current_image_item = None
    for item in globals.workspaceScene.selectedItems():
        if isinstance(item, QGraphicsPixmapItem):
            current_image_item = item
            break

def delete_selected_items():
    """Delete any selected item from the workspace scene."""
    for item in globals.workspaceScene.selectedItems():
        globals.workspaceScene.removeItem(item)

def wheel_event(event):
    """Resize selected image using mouse wheel."""
    global current_image_item
    if current_image_item:
        factor = 1.1 if event.angleDelta().y() > 0 else 0.9
        new_scale = current_image_item.scale() * factor
        # Clamp scale to avoid too small or too large
        new_scale = max(0.2, min(new_scale, 5.0))
        current_image_item.setScale(new_scale)
    else:
        # Default scroll if no image selected
        QGraphicsView.wheelEvent(globals.workspaceCanvas, event)

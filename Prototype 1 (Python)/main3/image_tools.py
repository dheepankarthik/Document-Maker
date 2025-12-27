from PySide6.QtWidgets import QFileDialog, QGraphicsPixmapItem, QGraphicsRectItem, QGraphicsView
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import Qt, QRectF, QPointF
import globals

# ---------------- Image Utilities ----------------

def update_handles(image_item):
    """Update positions of corner handles."""
    r = image_item.boundingRect()
    image_item.handles["tl"].setPos(r.topLeft())
    image_item.handles["tr"].setPos(r.topRight())
    image_item.handles["bl"].setPos(r.bottomLeft())
    image_item.handles["br"].setPos(r.bottomRight())

def resize_from_handle(image_item, corner, pos):
    """Resize image based on corner handle drag."""
    rect = QRectF(image_item.boundingRect())

    if corner == "br":
        rect.setBottomRight(pos)
    elif corner == "tr":
        rect.setTopRight(pos)
    elif corner == "bl":
        rect.setBottomLeft(pos)
    elif corner == "tl":
        rect.setTopLeft(pos)

    # Minimum size limit
    if rect.width() < 30 or rect.height() < 30:
        return

    # Preserve aspect ratio
    ratio = image_item.original_pixmap.width() / image_item.original_pixmap.height()
    rect.setHeight(rect.width() / ratio)

    scaled = image_item.original_pixmap.scaled(
        rect.size().toSize(),
        Qt.KeepAspectRatio,
        Qt.SmoothTransformation
    )
    image_item.setPixmap(scaled)
    update_handles(image_item)

# ---------------- Main Functions ----------------

def add_image():
    """Add image to the canvas with resize handles."""
    if globals.window is None or globals.workspaceScene is None:
        return  # Safety check

    # Safe file dialog with parent
    file_path, _ = QFileDialog.getOpenFileName(
        parent=globals.window,
        caption="Select Image",
        dir="",
        filter="Images (*.png *.jpg *.jpeg *.bmp)"
    )
    if not file_path:
        return

    pixmap = QPixmap(file_path)
    if pixmap.isNull():
        return

    image_item = QGraphicsPixmapItem(pixmap)
    image_item.original_pixmap = pixmap

    image_item.setFlag(QGraphicsPixmapItem.ItemIsMovable, True)
    image_item.setFlag(QGraphicsPixmapItem.ItemIsSelectable, True)

    # Default position
    image_item.setPos(100, 100)
    globals.workspaceScene.addItem(image_item)

    # ---------------- Create corner handles ----------------
    image_item.handles = {}

    for corner in ("tl", "tr", "bl", "br"):
        handle = QGraphicsRectItem(-5, -5, 10, 10, image_item)
        handle.setBrush(QColor("blue"))
        handle.setFlag(QGraphicsRectItem.ItemIsMovable, True)
        handle.setFlag(QGraphicsRectItem.ItemSendsScenePositionChanges, True)
        handle.corner = corner

        # Monkey-patch handle movement
        def item_change(change, value, h=handle):
            if change == QGraphicsRectItem.ItemPositionChange:
                resize_from_handle(image_item, h.corner, value)
                return QPointF(0, 0)  # Keep handle at 0,0 relative to parent
            return QGraphicsRectItem.itemChange(h, change, value)

        handle.itemChange = item_change
        image_item.handles[corner] = handle

    update_handles(image_item)

def update_selection():
    """Keep track of currently selected image for wheel zoom."""
    globals.current_image_item = None
    for item in globals.workspaceScene.selectedItems():
        if isinstance(item, QGraphicsPixmapItem):
            globals.current_image_item = item
            break

def delete_selected_image():
    """Delete currently selected image(s)."""
    for item in globals.workspaceScene.selectedItems():
        if isinstance(item, QGraphicsPixmapItem):
            globals.workspaceScene.removeItem(item)

def wheel_event(event):
    """Mouse wheel zoom for selected image."""
    if hasattr(globals, "current_image_item") and globals.current_image_item:
        factor = 1.1 if event.angleDelta().y() > 0 else 0.9
        new_scale = globals.current_image_item.scale() * factor
        # Clamp scale between 0.2 and 5.0
        new_scale = max(0.2, min(new_scale, 5.0))
        globals.current_image_item.setScale(new_scale)
    else:
        # Fallback to default scroll behavior
        QGraphicsView.wheelEvent(globals.workspaceCanvas, event)

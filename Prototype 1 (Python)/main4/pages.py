from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtGui import QPen, QBrush
from PySide6.QtCore import Qt
import globals

PAGE_WIDTH  = 794
PAGE_HEIGHT = 1123
PAGE_GAP    = 40

_pages: list[QGraphicsRectItem] = []

def create_page(index: int):
    y = index * (PAGE_HEIGHT + PAGE_GAP)

    page = QGraphicsRectItem(0, y, PAGE_WIDTH, PAGE_HEIGHT)
    page.setBrush(QBrush(Qt.white))
    page.setPen(QPen(Qt.lightGray, 1))
    page.setZValue(-100)

    globals.workspaceScene.addItem(page)
    _pages.append(page)

    _update_scene_rect()
    return page

def ensure_page_for_item(item):
    if not item:
        return

    bottom = item.sceneBoundingRect().bottom()

    while bottom > current_pages_height():
        create_page(len(_pages))

def current_pages_height():
    if not _pages:
        return 0
    last = _pages[-1]
    return last.rect().y() + PAGE_HEIGHT

def _update_scene_rect():
    globals.workspaceScene.setSceneRect(
        0, 0,
        PAGE_WIDTH,
        current_pages_height()
    )

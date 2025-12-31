from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QFrame, QScrollArea, QGraphicsView, QGraphicsScene, QSizePolicy, QGraphicsRectItem
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QPen, QBrush
import globals
import pages
import styles


from PySide6.QtGui import QFontDatabase


def build_ui(window):
    mainLayout = QVBoxLayout(window)

    # Title Frame
    titleFrame = QFrame()
    
    titleLayout = QVBoxLayout(titleFrame)
    
    titleLabel = QLabel("Welcome to the Document Maker")
    
    titleLabel.setAlignment(Qt.AlignCenter)
    
    titleLayout.addWidget(titleLabel)



    # Body Frame
    bodyFrame = QFrame()
    bodyLayout = QHBoxLayout(bodyFrame)

    buttonFrame = QFrame()
    workspaceFrame = QFrame()

    bodyLayout.addWidget(buttonFrame, stretch=2)
    bodyLayout.addWidget(workspaceFrame, stretch=14)
    mainLayout.addWidget(titleFrame)
    mainLayout.addWidget(bodyFrame)





    # Workspace Layout

    workspaceLayout = QVBoxLayout(workspaceFrame)
    
    workspaceLabel = QLabel("Work\nSpace")
    
    workspaceLabel.setAlignment(Qt.AlignHCenter)
    
    workspaceLayout.addWidget(workspaceLabel)


    # Workspace Scene and Canvas

    globals.workspaceScene = QGraphicsScene()
    globals.workspaceCanvas = QGraphicsView(globals.workspaceScene)

    globals.workspaceCanvas.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
    globals.workspaceCanvas.setStyleSheet("background-color: #e5e5e5")
    globals.workspaceCanvas.setFocusPolicy(Qt.StrongFocus)

    
    workspaceLayout.addWidget(globals.workspaceCanvas)

    # ---------------- Pages ----------------
    pages.create_page(0)

    globals.workspaceScene.setSceneRect(
        0, 0,
        pages.PAGE_WIDTH,
        pages.PAGE_HEIGHT
    )

    styles.apply_styles(titleFrame=titleFrame, buttonFrame=buttonFrame, workspaceFrame=workspaceFrame)

    return {
        "buttonFrame": buttonFrame,
        "titleLabel": titleLabel
    }



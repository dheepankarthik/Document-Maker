from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QFrame, QScrollArea, QGraphicsView, QGraphicsScene, QSizePolicy, QGraphicsRectItem
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QPen, QBrush
import globals
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

    scrollArea = QScrollArea()
    scrollArea.setWidgetResizable(True)
    workspaceLayout.addWidget(scrollArea)

    scrollWidget = QWidget()
    scrollArea.setWidget(scrollWidget)

    scrollLayout = QVBoxLayout(scrollWidget)
    scrollLayout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

    # Workspace Scene and Canvas

    globals.workspaceScene = QGraphicsScene(0, 0, 794, 1123)
    globals.workspaceCanvas = QGraphicsView(globals.workspaceScene)
    globals.workspaceCanvas.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
    globals.workspaceCanvas.setStyleSheet("background-color: white")
    globals.workspaceCanvas.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
    globals.workspaceCanvas.setFocus()
    globals.workspaceCanvas.centerOn(0, 0)

    scrollLayout.addWidget(globals.workspaceCanvas)

    styles.apply_styles(titleFrame=titleFrame, buttonFrame=buttonFrame, workspaceFrame=workspaceFrame)

    return {
        "buttonFrame": buttonFrame,
        "titleLabel": titleLabel
    }



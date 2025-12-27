from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QFrame, QScrollArea, QGraphicsView, QGraphicsScene
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
import globals, styles

def build_ui(window):
    mainLayout = QVBoxLayout(window)

    titleFrame = QFrame()
    titleLayout = QVBoxLayout(titleFrame)
    titleLabel = QLabel("Welcome to the Document Maker")
    titleLabel.setAlignment(Qt.AlignCenter)
    titleLayout.addWidget(titleLabel)

    bodyFrame = QFrame()
    bodyLayout = QHBoxLayout(bodyFrame)

    buttonFrame = QFrame()
    workspaceFrame = QFrame()

    bodyLayout.addWidget(buttonFrame, 2)
    bodyLayout.addWidget(workspaceFrame, 8)

    mainLayout.addWidget(titleFrame)
    mainLayout.addWidget(bodyFrame)

    # Workspace
    workspaceLayout = QVBoxLayout(workspaceFrame)
    workspaceLabel = QLabel("Work Space")
    workspaceLabel.setAlignment(Qt.AlignHCenter)
    workspaceLayout.addWidget(workspaceLabel)

    scrollArea = QScrollArea()
    scrollArea.setWidgetResizable(True)
    workspaceLayout.addWidget(scrollArea)

    scrollWidget = QWidget()
    scrollArea.setWidget(scrollWidget)

    scrollLayout = QVBoxLayout(scrollWidget)

    globals.workspaceScene = QGraphicsScene(0, 0, 600, 400)
    globals.workspaceCanvas = QGraphicsView(globals.workspaceScene)
    globals.workspaceCanvas.setAlignment(Qt.AlignTop | Qt.AlignLeft)
    globals.workspaceCanvas.setStyleSheet("background-color: white")

    scrollLayout.addWidget(globals.workspaceCanvas)

    styles.apply_styles(titleFrame, buttonFrame, workspaceFrame)


    return buttonFrame



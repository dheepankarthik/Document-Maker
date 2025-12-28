from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QFrame, QScrollArea, QGraphicsView, QGraphicsScene, QSizePolicy
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont
import globals
import styles


from PySide6.QtGui import QFontDatabase


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

    bodyLayout.addWidget(buttonFrame, stretch=4)
    bodyLayout.addWidget(workspaceFrame, stretch=12)

    mainLayout.addWidget(titleFrame)
    mainLayout.addWidget(bodyFrame)

    workspaceLayout = QVBoxLayout(workspaceFrame)
    workspaceLabel = QLabel("Work\nSpace")
    workspaceLabel.setAlignment(Qt.AlignHCenter)
    workspaceLayout.addWidget(workspaceLabel)

    scrollArea = QScrollArea()
    scrollArea.setWidgetResizable(True)
    # scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
    workspaceLayout.addWidget(scrollArea)

    scrollWidget = QWidget()
    scrollArea.setWidget(scrollWidget)

    scrollLayout = QVBoxLayout(scrollWidget)
    scrollLayout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

    globals.workspaceScene = QGraphicsScene()
    globals.workspaceCanvas = QGraphicsView(globals.workspaceScene)
    globals.workspaceCanvas.setAlignment(Qt.AlignTop | Qt.AlignLeft)
    globals.workspaceCanvas.setStyleSheet("background-color: white")
    globals.workspaceCanvas.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
    globals.workspaceCanvas.setFocus()



    scrollLayout.addWidget(globals.workspaceCanvas)

    styles.apply_styles(titleFrame=titleFrame, buttonFrame=buttonFrame, workspaceFrame=workspaceFrame)

    return buttonFrame



import PySide6
import sys
from PySide6.QtWidgets import ( QApplication, QWidget, QLabel, QVBoxLayout, 
QHBoxLayout, QSizePolicy, QFrame, QLineEdit, QPushButton, QTextEdit, QScrollArea,
QGraphicsView, QGraphicsScene, QGraphicsTextItem, QFileDialog, QGraphicsPixmapItem, QGraphicsRectItem)

from PySide6.QtGui import QFont, QPixmap, QColor

from PySide6.QtCore import Qt, QRectF, QPointF

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("Document Maker") # Window Title 

window.resize(1600, 900)

titleLabel = QLabel("Welcome to the Document Maker")

buttonLabel = QLabel("Options")

workspaceLabel = QLabel("Work Space")

# ==========================
#   Layouts
# ==========================

"""
This part of the program puts in place the following structure of the program:

Main Layout 

-- Title Frame (for the title of the program)

-- Body Frame

-- -- Options (Buttons) Frame

-- -- --  Title of the Options Frame

-- -- --  Section where the buttons are accessible

-- -- Workspace Frame

-- -- -- Title of the Workspace Frame

-- -- -- The actual workspace



"""
mainLayout = QVBoxLayout(window)

titleFrame = QFrame()

titleLayout = QVBoxLayout(titleFrame)

bodyFrame = QFrame()

bodyLayout = QHBoxLayout(bodyFrame)

buttonFrame = QFrame()

workspaceFrame = QFrame()

buttonLayout = QVBoxLayout(buttonFrame)

workspaceLayout = QVBoxLayout(workspaceFrame)

mainLayout.addWidget(titleFrame)

bodyLayout.addWidget(buttonFrame, stretch=2)

bodyLayout.addWidget(workspaceFrame, stretch=8)

mainLayout.addWidget(titleFrame)

mainLayout.addWidget(bodyFrame, stretch=1)




titleLayout.addWidget(titleLabel)

buttonLayout.addWidget(buttonLabel)

workspaceLayout.addWidget(workspaceLabel, stretch=1)


titleLabel.setAlignment(Qt.AlignCenter)
titleFrame.setFixedHeight(100)

bodyFrame.setFixedHeight(800)


buttonLabel.setAlignment(Qt.AlignTop)
buttonLabel.setAlignment(Qt.AlignHCenter)

workspaceLabel.setAlignment(Qt.AlignTop)
workspaceLabel.setAlignment(Qt.AlignHCenter)


workspaceScrollArea = QScrollArea()
workspaceScrollArea.setWidgetResizable(True)

workspaceScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
workspaceScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

workspaceLayout.addWidget(workspaceScrollArea, stretch=15)

workspaceScrollAreaWidget = QWidget()

workspaceScrollArea.setWidget(workspaceScrollAreaWidget)

workspaceScrollAreaInternalLayout = QVBoxLayout(workspaceScrollAreaWidget)

workspaceScene = QGraphicsScene()
workspaceScene.setSceneRect(0, 0, 600, 400)

workspaceCanvas = QGraphicsView(workspaceScene)
workspaceCanvas.setAlignment(Qt.AlignTop | Qt.AlignLeft)
workspaceCanvas.setStyleSheet("background-color: #ffffff")

workspaceScrollAreaInternalLayout.addWidget(workspaceCanvas)


#Styling 

titleFrame.setStyleSheet("""
QFrame {
    background: qlineargradient(
                         x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4facfe, stop: 1 #00f2fe
    );
}
                         
QLabel {
    font-size: 30px;
    font-family: Dosis;
}
""")

buttonFrame.setStyleSheet("""
QFrame {
    background: qlineargradient(
    x1:0, y1:0,
    x2:1, y2:1,
    stop:0.0  #00c6ff,
    stop:0.25 #0072ff,
    stop:0.5  #6a11cb,
    stop:0.75 #b721ff,
    stop:1.0  #f953c6
);
}
                         
QLabel {
    font-size: 30px;
    font-family: Dosis;
    
}
                          
QPushButton {
                          margin-top: 45px;
                          margin-bottom: 45px;
                          padding: 5px;
}
""")

workspaceFrame.setStyleSheet("""
QFrame {
    background: qlineargradient(
    x1:0, y1:0,
    x2:1, y2:1,
    stop:0.0  #054A91,
    stop:0.25 #3E7CB1,
    stop:0.5  #81A4CD,
    stop:0.75 #DBE4EE   ,
    stop:1.0  #F17300
);
}
""")



# Child Widgets

## Text Box Button Code & Styling

textBoxButton = QPushButton("Text Box")

buttonLayout.addWidget(textBoxButton)

def addTextBox():
    global workspaceScene

    textItem = QGraphicsTextItem("Add text")

    textItem.setFont(QFont("Times New Roman", 14))
    textItem.setDefaultTextColor(Qt.black)
    

    textItem.setTextInteractionFlags(Qt.TextEditorInteraction)

    textItem.setFlag(QGraphicsTextItem.ItemIsMovable, True)
    
    textItem.setFlag(QGraphicsTextItem.ItemIsSelectable, True)

    textItem.setPos(50, 50)

    textItem.setTextWidth(300)

    workspaceScene.addItem(textItem)

def deleteSelectedItems():
    for item in workspaceScene.selectedItems():
        workspaceScene.removeItem(item)

# ---------------- Keyboard Delete ----------------
def keyPressEvent(event):
    if event.key() == Qt.Key_Delete:
        deleteSelectedItems()

textBoxButton.clicked.connect(addTextBox)

textBoxButton.setStyleSheet("""
    QPushButton {
                            background-color: #17BEBB;
                            color: white;
    }
""")


## End of Text Box Button & Styling

## Start of Image Button & Styling

imageButton = QPushButton("Add an image")

buttonLayout.addWidget(imageButton)

currentImageItem = None

# Function for adding an image

def updateHandles(imageItem):
    r = imageItem.boundingRect()
    imageItem.handles["tl"].setPos(r.topLeft())
    imageItem.handles["tr"].setPos(r.topRight())
    imageItem.handles["bl"].setPos(r.bottomLeft())
    imageItem.handles["br"].setPos(r.bottomRight())

def resizeFromHandle(imageItem, corner, pos):
    rect = QRectF(imageItem.boundingRect())

    if corner == "br":
        rect.setBottomRight(pos)
    elif corner == "tr":
        rect.setTopRight(pos)
    elif corner == "bl":
        rect.setBottomLeft(pos)
    elif corner == "tl":
        rect.setTopLeft(pos)

    if rect.width() < 30 or rect.height() < 30:
        return

    ratio = imageItem.originalPixmap.width() / imageItem.originalPixmap.height()
    rect.setHeight(rect.width() / ratio)

    scaled = imageItem.originalPixmap.scaled(
        rect.size().toSize(),
        Qt.KeepAspectRatio,
        Qt.SmoothTransformation
    )

    imageItem.setPixmap(scaled)
    updateHandles(imageItem)


def addImage():

    global workspaceScene

    filePath, _ = QFileDialog.getOpenFileName(
        window,
        "Select Image",
        "",
        "Images (*.png *.jpg *.jpeg *.bmp)"
    )

    if not filePath:
        return
    
    pixmap = QPixmap(filePath)

    imageItem = QGraphicsPixmapItem(pixmap)

    imageItem.setFlag(QGraphicsPixmapItem.ItemIsMovable, True)
    imageItem.setFlag(QGraphicsPixmapItem.ItemIsSelectable, True)

    imageItem.setPos(100, 100)
    workspaceScene.addItem(imageItem)

    imageItem.handles = {}

    for corner in ("tl", "tr", "bl", "br"):
        handle = QGraphicsRectItem(-5, -5, 10, 10, imageItem)
        handle.setBrush(QColor("blue"))
        handle.setFlag(QGraphicsRectItem.ItemIsMovable, True)
        handle.setFlag(QGraphicsRectItem.ItemSendsScenePositionChanges, True)
        handle.corner = corner

        # Monkey-patch itemChange
        def itemChange(change, value, h=handle):
            if change == QGraphicsRectItem.ItemPositionChange:
                resizeFromHandle(imageItem, h.corner, value)
                return QPointF(0, 0)
            return QGraphicsRectItem.itemChange(h, change, value)

        handle.itemChange = itemChange
        imageItem.handles[corner] = handle

    updateHandles(imageItem)

def updateSelection():
    global currentImageItem
    currentImageItem = None

    for item in workspaceScene.selectedItems():
        if isinstance(item, QGraphicsPixmapItem):
            currentImageItem = item
            break

def deleteSelectedImage():
    for item in workspaceScene.selectedItems():
        if isinstance(item, QGraphicsPixmapItem):
            workspaceScene.removeItem(item)

# ---------------- Mouse Wheel Resize ----------------
def wheelEvent(event):
    global currentImageItem

    if currentImageItem:
        factor = 1.1 if event.angleDelta().y() > 0 else 0.9
        newScale = currentImageItem.scale() * factor
        newScale = max(0.2, min(newScale, 5.0))  # clamp
        currentImageItem.setScale(newScale)
    else:
        QGraphicsView.wheelEvent(workspaceCanvas, event)

workspaceCanvas.wheelEvent = wheelEvent

# ---------------- Keyboard Delete ----------------
def keyPressEvent(event):
    if event.key() == Qt.Key_Delete:
        deleteSelectedImage()

window.keyPressEvent = keyPressEvent

imageButton.clicked.connect(addImage)
workspaceScene.selectionChanged.connect(updateSelection)




## End of Image Button & Styling

buttonLayout.addStretch()



window.show()



sys.exit(app.exec())
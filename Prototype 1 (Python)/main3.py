import PySide6
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy, QFrame, QLineEdit, QPushButton, QTextEdit, QScrollArea
from PySide6.QtCore import Qt

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
                          margin-top: 50px;
                          margin-bottom: 50px;
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
    global workspaceScrollAreaInternalLayout
    
    textBoxToAdd = QTextEdit()
    textBoxToAdd.setPlaceholderText("Add text")
    textBoxToAdd.setMinimumHeight(200)
    textBoxToAdd.setSizePolicy(
    QSizePolicy.Expanding,
    QSizePolicy.Fixed 
    )
    textBoxToAdd.setStyleSheet(""" QTextEdit {background-color: white} """)

    def deleteTextBox(frame):
        frame.setParent(None)
        frame.deleteLater()

    
    textBoxFrame = QFrame()
    textBoxLayout = QVBoxLayout(textBoxFrame)

    deleteButton = QPushButton("Delete Text Box")
    deleteButton.clicked.connect(lambda: deleteTextBox(textBoxFrame))
    deleteButton.setMaximumHeight(50)

    textBoxLayout.addWidget(textBoxToAdd)
    textBoxLayout.addWidget(deleteButton)

    
    workspaceScrollAreaInternalLayout.addWidget(textBoxFrame)

textBoxButton.clicked.connect(addTextBox)

textBoxButton.setStyleSheet("""
    QPushButton {
                            background-color: #17BEBB;
                            color: white;
    }
""")


## End of Text Box Button & Styling


buttonLayout.addStretch()



window.show()



sys.exit(app.exec())
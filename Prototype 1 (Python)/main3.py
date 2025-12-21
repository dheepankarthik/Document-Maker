import PySide6
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy, QFrame, QLineEdit
from PySide6.QtCore import Qt

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("Document Maker")

window.resize(1600, 900)

titleLabel = QLabel("Welcome to the Document Maker")

buttonLabel = QLabel("Options")

workspaceLabel = QLabel("Work Space")

# ==========================
#   Layouts
# ==========================

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




window.show()



sys.exit(app.exec())
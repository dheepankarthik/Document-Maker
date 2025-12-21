import PySide6
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("Document Maker")

window.resize(1600, 900)

label = QLabel("Welcome to the Document Maker")
label.setFixedHeight(75)

# Layouts

mainLayout = QVBoxLayout()

titleLayout = QVBoxLayout()

titleLayout.addWidget(label, alignment=Qt.AlignTop)

workLayout = QHBoxLayout()

buttonLayout = QVBoxLayout()

workspaceLayout = QVBoxLayout()
window.setLayout(mainLayout)

mainLayout.addLayout(titleLayout)
mainLayout.addLayout(workLayout)
workLayout.addLayout(buttonLayout)
workLayout.addLayout(workspaceLayout)

buttonLayoutTitle = QLabel("Options")
workspaceLayoutTitle = QLabel("Workspace")

buttonLayout.addWidget(buttonLayoutTitle, alignment=Qt.AlignTop)
workspaceLayout.addWidget(workspaceLayoutTitle, alignment=Qt.AlignTop)

#Styling 

app.setStyleSheet("""
QLabel {
    font-family: Arial;
    font-size: 20px;
}
""")



window.show()



sys.exit(app.exec())
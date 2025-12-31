

def apply_styles(titleFrame, buttonFrame, workspaceFrame):
    titleFrame.setStyleSheet("""
        QLabel { font-size: 30px; font-family: Dosis; background-color: #80FFE8; padding: 10px}
    """)

    buttonFrame.setStyleSheet("""
        QPushButton {
            margin-top: 45px;
            margin-bottom: 45px;
            padding: 10px;
            
        }
                              
        QFrame {
                              background-color: #83BCFF
        }
                              
        
                              
    """)

    workspaceFrame.setStyleSheet("""
        QFrame { background: #97D2FB; }
    """)

def apply_textBoxButton_styles(textBoxButton):
    textBoxButton.setStyleSheet("""
        QPushButton {
                                font-weight: bold;
        }
    """)
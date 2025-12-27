def apply_styles(titleFrame, buttonFrame, workspaceFrame):
    titleFrame.setStyleSheet("""
        QLabel { font-size: 30px; font-family: Dosis; }
    """)

    buttonFrame.setStyleSheet("""
        QPushButton {
            margin-top: 45px;
            margin-bottom: 45px;
            padding: 5px;
        }
    """)

    workspaceFrame.setStyleSheet("""
        QFrame { background: #e0e0e0; }
    """)

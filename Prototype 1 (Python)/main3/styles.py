def apply_styles(titleFrame, buttonFrame, workspaceFrame):
    titleFrame.setStyleSheet("""
        QLabel { font-size: 30px; font-family: Dosis; background-color: #EFD6AC; padding: 10px}
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

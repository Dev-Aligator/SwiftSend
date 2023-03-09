from PySide2.QtWidgets import QScrollArea

class MyScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWidgetResizable(True)
        self.setStyleSheet("""
            QScrollBar:vertical {
                width: 8px;
                margin: 0px 0 0px 0;
                border-radius: 5px;
                background-color: transparent;
            }
            QScrollBar::handle:vertical {
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 5px;
                min-height: 20px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
                border: none;
            }
        """)

    def enterEvent(self, event):
        super().enterEvent(event)
        self.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical {
                width: 8px;
                margin: 0px 0 0px 0;
                border-radius: 5px;
                background-color: transparent;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
                border: none;
            }
        """)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical {
                width: 5px;
                margin: 0px 0 0px 0;
                border-radius: 3px;
                background-color: transparent;
            }
            QScrollBar::handle:vertical {
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 3px;
                min-height: 20px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
                border: none;
            }

                
    """)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical {
                width: 8px;
                margin: 0px 0 0px 0;
                border-radius: 5px;
                background-color: transparent;
            }
        QScrollBar::handle:vertical {
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 5px;
            min-height: 20px;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
                border: none;
            }


    """)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.verticalScrollBar().setStyleSheet("""
        QScrollBar:vertical {
            width: 5px;
            margin: 0px 0 0px 0;
            border-radius: 3px;
            background-color: transparent;
        }
        QScrollBar::handle:vertical {
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 3px;
            min-height: 20px;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
                border: none;
            }

    """)



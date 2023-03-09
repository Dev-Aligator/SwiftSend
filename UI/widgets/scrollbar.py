from PySide2.QtWidgets import QScrollArea

class MyScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWidgetResizable(True)
        self.setStyleSheet("""
            QScrollBar:vertical {
                width: 20px;
                margin: 20px 0 20px 0;
                border-radius: 10px;
                background-color: rgba(255, 255, 255, 0.5);
            }
            QScrollBar::handle:vertical {
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 10px;
                min-height: 20px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 20px;
                border-radius: 10px;
                background-color: rgba(255, 255, 255, 0.5);
            }
            QScrollBar::add-line:vertical:hover, QScrollBar::sub-line:vertical:hover,
            QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed {
                height: 30px;
                margin-top: -10px;
                margin-bottom: -10px;
                background-color: rgba(255, 255, 255, 0.8);
            }
        """)

    def enterEvent(self, event):
        super().enterEvent(event)
        self.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical {
                width: 30px;
                margin: 10px 0 10px 0;
                border-radius: 10px;
                background-color: rgba(255, 255, 255, 0.5);
            }
            QScrollBar::handle:vertical {
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 10px;
                min-height: 20px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 20px;
                border-radius: 10px;
                background-color: rgba(255, 255, 255, 0.5);
            }
            QScrollBar::add-line:vertical:hover, QScrollBar::sub-line:vertical:hover,
            QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed {
                height: 30px;
                margin-top: -10px;
                margin-bottom: -10px;
                background-color: rgba(255, 255, 255, 0.8);
            }
        """)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical {
                width: 20px;
                margin: 20px 0 20px 0;
                border-radius: 10px;
                background-color: rgba(255, 255, 255, 0.5);
            }
            QScrollBar::handle:vertical {
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 10px;
                min-height: 20px;
            }
            QScrollBar::add-line:vertical {
            
            }
                    QScrollBar::sub-line:vertical {
            height: 20px;
            border-radius: 10px;
            background-color: rgba(255, 255, 255, 0.5);
        }
        QScrollBar::add-line:vertical:hover, QScrollBar::sub-line:vertical:hover,
        QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed {
            height: 30px;
            margin-top: -10px;
            margin-bottom: -10px;
            background-color: rgba(255, 255, 255, 0.8);
        }
    """)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical {
                width: 30px;
                margin: 10px 0 10px 0;
                border-radius: 10px;
                background-color: rgba(255, 255, 255, 0.5);
            }
        QScrollBar::handle:vertical {
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            min-height: 20px;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            height: 20px;
            border-radius: 10px;
            background-color: rgba(255, 255, 255, 0.5);
        }
        QScrollBar::add-line:vertical:hover, QScrollBar::sub-line:vertical:hover,
        QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed {
            height: 30px;
            margin-top: -10px;
            margin-bottom: -10px;
            background-color: rgba(255, 255, 255, 0.8);
        }
    """)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.verticalScrollBar().setStyleSheet("""
        QScrollBar:vertical {
            width: 20px;
            margin: 20px 0 20px 0;
            border-radius: 10px;
            background-color: rgba(255, 255, 255, 0.5);
        }
        QScrollBar::handle:vertical {
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            min-height: 20px;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            height: 20px;
            border-radius: 10px;
            background-color: rgba(255, 255, 255, 0.5);
        }
        QScrollBar::add-line:vertical:hover, QScrollBar::sub-line:vertical:hover,
        QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed {
            height: 30px;
            margin-top: -10px;
            margin-bottom: -10px;
            background-color: rgba(255, 255, 255, 0.8);
        }
    """)



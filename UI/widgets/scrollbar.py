from PySide2.QtWidgets import QScrollArea

class MyScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWidgetResizable(True)
        self.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical {
                width: 5px;
                margin: 0;
                border-radius: 2.5px;
                background-color: transparent;
            }
            QScrollBar::handle:vertical {
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 2.5px;
                min-height: 20px;
            }
            QScrollBar::add-line:vertical {
                border: none;
                background: none;
                height: 0px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
                border-bottom-right-radius: 4px;
                border-bottom-left-radius: 4px;
            }

            QScrollBar::sub-line:vertical {
                border: none;
                background: none;
                height: 0px;
                subcontrol-position: top;
                subcontrol-origin: margin;
                border-top-right-radius: 2.5px;
                border-top-left-radius: 2.5px;
            }
        """)

    def enterEvent(self, event):
        super().enterEvent(event)
        self.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical {
                width: 8px;
                margin: 0;
                border-radius: 4px;
                background-color: transparent;
            }
            QScrollBar::handle:vertical {
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 4px;
                min-height: 20px;
            }
            QScrollBar::add-line:vertical {
                border: none;
        background: none;
        height: 0px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
        border-bottom-right-radius: 4px;
        border-bottom-left-radius: 4px;
    }

    QScrollBar::sub-line:vertical {
        border: none;
        background: none;
        height: 0px;
        subcontrol-position: top;
        subcontrol-origin: margin;
        border-top-right-radius: 4px;
        border-top-left-radius: 4px;
    }
        """)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical {
                width: 5px;
                margin: 0;
                border-radius: 2.5px;
                background-color: transparent;
            }
            QScrollBar::handle:vertical {
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 2.5px;
                min-height: 20px;
            }
            QScrollBar::add-line:vertical {
        border: none;
        background: none;
        height: 0px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
        border-bottom-right-radius: 2.5px;
        border-bottom-left-radius: 2.5px;
    }

    QScrollBar::sub-line:vertical {
        border: none;
        background: none;
        height: 0px;
        subcontrol-position: top;
        subcontrol-origin: margin;
        border-top-right-radius: 2.5px;
        border-top-left-radius: 2.5px;
    }
                
    """)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical {
                width: 8px;
                margin: 0;
                border-radius: 4px;
                background-color: transparent;
            }
        QScrollBar::handle:vertical {
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 4px;
            min-height: 20px;
        }
        QScrollBar::add-line:vertical {
        border: none;
        background: none;
        height: 0px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
        border-bottom-right-radius: 4px;
        border-bottom-left-radius: 4px;
    }

    QScrollBar::sub-line:vertical {
        border: none;
        background: none;
        height: 0px;
        subcontrol-position: top;
        subcontrol-origin: margin;
        border-top-right-radius: 4px;
        border-top-left-radius: 4px;
    }


    """)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.verticalScrollBar().setStyleSheet("""
        QScrollBar:vertical {
            width: 5px;
            margin: 0;
            border-radius: 2.5px;
            background-color: transparent;
        }
        QScrollBar::handle:vertical {
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 2.5px;
            min-height: 20px;
        }
        QScrollBar::add-line:vertical {
        border: none;
        background: none;
        height: 0px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
        border-bottom-right-radius: 2.5px;
        border-bottom-left-radius: 2.5px;
    }

    QScrollBar::sub-line:vertical {
        border: none;
        background: none;
        height: 0px;
        subcontrol-position: top;
        subcontrol-origin: margin;
        border-top-right-radius: 2.5px;
        border-top-left-radius: 2.5px;
    }

    """)



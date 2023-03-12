from PySide2.QtWidgets import QMenu, QAction 
from PySide2.QtCore import QPoint

class CascadeMenu(QMenu):
    def __init__(self, parent, button, action_list):
        super().__init__(parent)
        for action in action_list:
            if action == "E̲xit":
                self.addSeparator()
            self.addAction(QAction(action, parent))
        self.setStyleSheet(u"""
QMenu {
    background-color: #282a36;
    border: 1px solid #44475a;
    padding: 8px;
    font-size: 14px;
}

QMenu::item {
    padding: 8px 32px 8px 24px;
    border: none;
    font-weight: 400;
    color: #f8f8f2;
}

QMenu::item:selected {
    background-color: #44475a;
}


QMenu::separator {
    height: 1px;
    background-color: #A9A9A9;
    margin: 4px 0px 4px 0px;
}

QMenu::indicator {
    width: 13px;
    height: 13px;
    padding: 5px;
}

QMenu::indicator:unchecked {
    image: url(icons/unchecked.png);
}

QMenu::indicator:checked {
    image: url(icons/checked.png);
}
""")
        
        button.clicked.connect(lambda: self.show_menu(parent, button))
    def show_menu(self, parent, button):
        position = QPoint(button.geometry().left(), button.geometry().bottom())
        self.popup(parent.mapToGlobal(position)) 
        self.aboutToHide.connect(self.hide_menu)
    def hide_menu(self):
        if self.isVisible():
            self.hide()
        
        

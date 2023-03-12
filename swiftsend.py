import sys

from UI.ui_interface import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## TOGGLE/BURGUER MENU
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.file_transfer_page))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.transfer_process_page))
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.message_page))
        
        self.menu = QMenu(self)
        self.menu.addAction(QAction('Menu Item 1', self))
        self.menu.addAction(QAction('Menu Item 2', self))
        self.menu.addAction(QAction('Menu Item 3', self))
        self.ui.icon_button.clicked.connect(self.show_menu)
    def show_menu(self):
        position = QPoint(self.ui.icon_button.geometry().left(), self.ui.icon_button.geometry().bottom())
        self.menu.popup(self.mapToGlobal(position))

        # Connect the menu to hide when it loses focus
        self.menu.aboutToHide.connect(self.hide_menu)
    def hide_menu(self):
        if self.menu.isVisible():
            self.hide_menu()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
 

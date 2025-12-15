import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from centralwidget import to_do_app_centralwidget


class to_do_app_window(QMainWindow):
    def __init__(
        self,
    ):
        super().__init__()
        self.setWindowTitle("To Do App")
        self.central_widget = to_do_app_centralwidget()

        self.setCentralWidget(self.central_widget)


def main():
    app = QApplication(sys.argv)
    window = to_do_app_window()
    window.show()
    sys.exit(app.exec())
 

if __name__ == "__main__":
    main()

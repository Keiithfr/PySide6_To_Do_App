import sys
from PySide6.QtWidgets import QApplication, QMainWindow


class to_do_app_window(QMainWindow):
    def __init__(
        self,
    ):
        super().__init__()


def main():
    app = QApplication(sys.argv)
    window = to_do_app_window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

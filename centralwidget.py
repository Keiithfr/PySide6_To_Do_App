from PySide6.QtWidgets import (
    QPushButton,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QListWidget,
    QMessageBox,
)
from PySide6.QtCore import Qt


class to_do_app_centralwidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.add_task_label = QLabel("Enter a Task")
        self.input_task = QLineEdit()
        self.input_task.setPlaceholderText("Enter task...")
        self.add_task_button = QPushButton("Add Task")
        self.list = QListWidget()

        # style
        self.add_task_label.setObjectName("add_task_label")
        self.input_task.setObjectName("input_task")
        self.add_task_button.setObjectName("add_task_button")
        self.list.setObjectName("list")

        self.add_task_button.setCursor(Qt.PointingHandCursor)

        with open("style.qss", "r") as f:
            self.setStyleSheet(f.read())

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.add_task_label)
        v_layout.addWidget(self.input_task)
        v_layout.addWidget(self.add_task_button)
        v_layout.addWidget(self.list)

        self.setLayout(v_layout)

        self.add_task_button.clicked.connect(self.add_task)
        self.input_task.returnPressed.connect(self.add_task)
        self.list.itemDoubleClicked.connect(self.delete_task)

    def add_task(self):
        task = self.input_task.text().strip()

        if not task:
            return

        self.list.addItem(task)
        self.input_task.clear()

    def delete_task(self, item):
        reply = QMessageBox.question(
            self,
            "Delete Task",
            f"Delete '{item.text()}'?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            self.list.takeItem(self.list.row(item))

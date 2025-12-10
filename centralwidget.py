from PySide6.QtWidgets import (
    QPushButton,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QListWidget,
)


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

        v_layout = QVBoxLayout
        v_layout.addWidget(self.add_task_label)
        v_layout.addWidget(self.input_task)
        v_layout.addWidget(self.add_task_button)
        v_layout.addWidget(self.list)

        self.setLayout(v_layout)

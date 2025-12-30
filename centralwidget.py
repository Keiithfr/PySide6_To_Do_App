from PySide6.QtWidgets import (
    QPushButton,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QListWidget,
    QMessageBox,
    QListWidgetItem,
)
from PySide6.QtCore import Qt
import json
import os


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

        self.add_task_button.setCursor(
            Qt.PointingHandCursor
        )  # cursor pointer on the button

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
        self.load_tasks()
        self.list.itemChanged.connect(self.on_item_changed)

    def add_task(self):
        task = self.input_task.text().strip()

        if not task:
            return

        item = QListWidgetItem(task)
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Unchecked)

        self.list.addItem(item)
        self.input_task.clear()
        self.save_tasks()

    def update_item_style(self, item):
        if item.checkState() == Qt.Checked:
            item.setForeground(Qt.gray)
            font = item.font()
            font.setStrikeOut(True)
            item.setFont(font)
        else:
            item.setForeground(Qt.white)
            font = item.font()
            font.setStrikeOut(False)
            item.setFont(font)

    def on_item_changed(self, item):

        self.update_item_style(item)
        self.save_tasks()

        # Persistence(saving)

    def get_tasks_path(self):
        return os.path.join(os.path.dirname(__file__), "tasks.json")

    def save_tasks(self):
        tasks = []

        for i in range(self.list.count()):
            item = self.list.item(i)
            tasks.append(
                {
                    "text": item.text(),
                    "completed": item.checkState() == Qt.Checked,
                }
            )

        with open(self.get_tasks_path(), "w") as f:
            json.dump(tasks, f, indent=2)

    def delete_task(self, item):
        reply = QMessageBox.question(
            self,
            "Delete Task",
            f"Delete '{item.text()}'?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            self.list.takeItem(self.list.row(item))
            self.save_tasks()

    def load_tasks(self):
        path = self.get_tasks_path()
        if not os.path.exists(path):
            return
        try:
            with open(path, "r") as f:
                tasks = json.load(f)
        except json.JSONDecodeError:
            # if the file is corrupted or empty
            return

        for task in tasks:
            item = QListWidgetItem(task["text"])
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)

            if task.get("completed"):
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)
            self.update_item_style(item)
            self.list.addItem(item)

import sys
from ProjectClass import Project
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("hello world")
        button = QPushButton("hello!")
        button.clicked.connect(self.button_clicked)

        greeting_message = QLabel("welcome to cozy craft! do you want to resume a project or begin a new one?")
        self.setCentralWidget(button)

    def button_clicked(self) :
        test = Project("test", "crochet")
        test.save_project_data()
        print(test.name)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
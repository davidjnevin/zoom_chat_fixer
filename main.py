import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QFileDialog
from PyQt5.QtCore import Qt
import re


class TextEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Zoom Chat Cleaner')
        self.setFixedSize(500, 500)

        # Create widgets
        self.title_label = QLabel('Drag and Drop .txt File', self)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        self.cancel_button = QPushButton('Cancel', self)
        self.copy_button = QPushButton('Copy', self)

        # Create layout for drag and drop window
        self.drag_drop_layout = QVBoxLayout()
        self.drag_drop_layout.addWidget(self.title_label)
        self.drag_drop_layout.addWidget(self.text_edit)
        self.drag_drop_layout.addStretch()

        # Create layout for cancel and save buttons
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.cancel_button)
        self.button_layout.addWidget(self.copy_button)

        # Create main layout and add sub-layouts
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.drag_drop_layout)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

        # Connect buttons to functions
        self.cancel_button.clicked.connect(self.close)
        self.copy_button.clicked.connect(self.copy_file)

        # Enable drag and drop
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        file_path = event.mimeData().urls()[0].toLocalFile()
        if file_path.endswith('.txt'):
            with open(file_path, 'r') as file:
                lines = file.readlines()
            non_time_lines = [line.replace("\t", "").replace("\r", "").replace("$", "").strip() for line in lines if not re.match(r'^\d{2}:\d{2}:\d{2}', line)]
            self.text_edit.setText("\n".join(non_time_lines))
        else:
            self.text_edit.setText('File must be a .txt file')

    def copy_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt)', options=options)
        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.text_edit.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    text_editor = TextEditor()
    text_editor.show()
    sys.exit(app.exec_())


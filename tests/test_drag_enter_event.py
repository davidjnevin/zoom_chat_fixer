import os
import unittest
from PyQt5.QtWidgets import QApplication
from main import TextEditor

class TestTextEditor(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.text_editor = TextEditor()

    def test_dropEvent_valid_file(self):
        # create a temporary .txt file
        file_name = 'test.txt'
        with open(file_name, 'w') as f:
            f.write('01:00:00 This is a test\n01:01:00 This is another test')

        # simulate dropping the file into the application
        mime_data = self.text_editor.mimeData([f'file://{os.path.abspath(file_name)}'])
        event = type('QDropEvent', (object,), {'mimeData': lambda _: mime_data})()
        self.text_editor.dropEvent(event)

        # check if the text edit widget has the expected text
        expected_text = 'This is a test\nThis is another test'
        actual_text = self.text_editor.text_edit.toPlainText()
        self.assertEqual(expected_text, actual_text)

        # remove the temporary file
        os.remove(file_name)

    def tearDown(self):
        self.app.exit()

if __name__ == '__main__':
    unittest.main()


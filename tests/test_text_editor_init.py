import sys
from PyQt6.QtWidgets import QApplication, QSizePolicy
from main import TextEditor

def test_text_editor_init():
    app = QApplication(sys.argv)
    text_editor = TextEditor()

    # Check that the window title is set correctly
    assert text_editor.windowTitle() == 'Zoom Chat Cleaner'

	# Check that the window size is correct
    assert text_editor.width() == 500
    assert text_editor.height() == 500

    # Check that the size policy is fixed
    assert text_editor.sizePolicy().hasHeightForWidth() == False



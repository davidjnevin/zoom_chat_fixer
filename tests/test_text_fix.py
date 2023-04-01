import os
from unittest.mock import Mock
from main import TextEditor

def test_drag_and_drop():
    # Create a mock of the TextEditor instance
    text_editor = TextEditor()
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.join(tests_dir, "test_file.txt")
    print(root_path)
    
    # Simulate a drag and drop event by calling the dragEnterEvent method with a mock QDragEnterEvent object
    event = Mock()
    try:
        event.mimeData().urls.return_value = [f"file://{root_path}"]
    except Exception as e:
        print(f"Error setting URL for mime data: {e}")
        raise e
    
    try:
        text_editor.dragEnterEvent(event)
    except Exception as e:
        print(f"Error triggering drag enter event: {e}")
        raise e

    # Assert that the event was accepted and that the file path was set correctly
    assert event.accepted()
    assert text_editor.file_path == root_path


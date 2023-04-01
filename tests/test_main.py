import unittest
import main

class TestMain(unittest.TestCase):
    def test_import_main(self):
        try:
            import main
        except ImportError:
            self.fail("Failed to import main module")

if __name__ == '__main__':
    test_main = TestMain()
    test_main.test_import_main()

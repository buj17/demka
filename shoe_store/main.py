import sys

from PySide6.QtWidgets import QApplication

import config.settings
from gui.windows.main_window import MainWindow


def load_stylesheet() -> str:
    style_path = config.settings.BASE_DIR / 'static' / 'style.qss'
    return style_path.open().read()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(load_stylesheet())
    window = MainWindow()
    window.show()
    app.exec()

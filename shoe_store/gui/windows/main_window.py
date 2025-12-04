from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QWidget

import config.settings
import gui.ui.main_window_ui
from gui.widgets import LoginWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = gui.ui.main_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.clear_all_widgets()

        self.load_logo()
        self.load_icon()
        self.setWindowTitle('Магазин "Обувь"')

        self.current_widget = LoginWidget(self)
        self.ui.stackedWidget.addWidget(self.current_widget)

    def load_logo(self):
        logo_path = config.settings.BASE_DIR / 'static' / 'logo.png'
        logo_image = QPixmap(logo_path)
        self.ui.logo_label.setPixmap(logo_image)

    def load_icon(self):
        icon_path = config.settings.BASE_DIR / 'static' / 'Icon.ico'
        icon_image = QPixmap(icon_path)
        self.setWindowIcon(icon_image)

    def switch_widget(self, widget: QWidget):
        self.current_widget = widget
        self.ui.stackedWidget.removeWidget(self.ui.stackedWidget.widget(0))
        self.ui.stackedWidget.addWidget(self.current_widget)

    def clear_all_widgets(self):
        for _ in range(self.ui.stackedWidget.count()):
            widget = self.ui.stackedWidget.widget(0)
            self.ui.stackedWidget.removeWidget(widget)

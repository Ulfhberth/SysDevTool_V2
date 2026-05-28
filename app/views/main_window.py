from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QStatusBar,
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from SysDevTool_V2.app.core import BaseView


class MainWindow(BaseView, QMainWindow):
    """
    Main application window.

    User-action signals (consumed by MainController)
    -------------------------------------------------
    increment_requested()
    decrement_requested()
    reset_requested()

    Public update slots (called by MainController)
    -----------------------------------------------
    on_counter_changed(value: int)
    on_status_changed(message: str)
    """

    increment_requested = pyqtSignal()
    decrement_requested = pyqtSignal()
    reset_requested = pyqtSignal()

    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.setWindowTitle("MVC Demo — PyQt6")
        self.setMinimumSize(400, 250)

        container = QWidget()
        self.setCentralWidget(container)
        self._root_layout = QVBoxLayout(container)

        self._build_ui()
        self._connect_internal_signals()

    def _build_ui(self) -> None:
        self._counter_label = QLabel("0", alignment=Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        self._counter_label.setFont(font)

        button_row = QHBoxLayout()
        self._btn_decrement = QPushButton("−")
        self._btn_reset = QPushButton("Reset")
        self._btn_increment = QPushButton("+")

        for btn in (self._btn_decrement, self._btn_reset, self._btn_increment):
            btn.setFixedHeight(40)
            button_row.addWidget(btn)

        self._root_layout.addStretch()
        self._root_layout.addWidget(self._counter_label)
        self._root_layout.addStretch()
        self._root_layout.addLayout(button_row)

        self._status_bar = QStatusBar()
        self.setStatusBar(self._status_bar)

    def _connect_internal_signals(self) -> None:
        self._btn_increment.clicked.connect(self.increment_requested)
        self._btn_decrement.clicked.connect(self.decrement_requested)
        self._btn_reset.clicked.connect(self.reset_requested)

    def on_counter_changed(self, value: int) -> None:
        self._counter_label.setText(str(value))

    def on_status_changed(self, message: str) -> None:
        self._status_bar.showMessage(message)

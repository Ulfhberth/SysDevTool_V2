import sys
from PyQt6.QtWidgets import QApplication
from .base_controller import BaseController


class Application:
    """
    Bootstrap helper: creates the QApplication, wires up the root
    controller, shows the main window, and starts the event loop.

    Usage::

        from app.core import Application
        from app.models import ExampleModel
        from app.views import MainWindow
        from app.controllers import MainController

        Application(MainController, ExampleModel, MainWindow).run()
    """

    def __init__(
        self,
        controller_cls: type[BaseController],
        model_cls,
        view_cls,
        app_name: str = "App",
    ) -> None:
        self._qt_app = QApplication(sys.argv)
        self._qt_app.setApplicationName(app_name)

        model = model_cls()
        view = view_cls()
        self._controller = controller_cls(model, view)
        self._view = view

    def run(self) -> int:
        self._view.show()
        return self._qt_app.exec()

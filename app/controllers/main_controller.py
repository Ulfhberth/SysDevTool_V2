from SysDevTool_V2.app.core import BaseController
from SysDevTool_V2.app.models import ExampleModel
from SysDevTool_V2.app.views import MainWindow


class MainController(BaseController):
    """
    Wires ExampleModel ↔ MainWindow.

    Signal flow
    -----------
    Model → View:
        ExampleModel.counter_changed  →  MainWindow.on_counter_changed
        ExampleModel.status_changed   →  MainWindow.on_status_changed
        ExampleModel.error_occurred   →  MainWindow.show_error

    View → Controller → Model:
        MainWindow.increment_requested  →  _on_increment  →  model.increment()
        MainWindow.decrement_requested  →  _on_decrement  →  model.decrement()
        MainWindow.reset_requested      →  _on_reset      →  model.reset()
    """

    def __init__(self, model: ExampleModel, view: MainWindow) -> None:
        super().__init__(model, view)

    @property
    def model(self) -> ExampleModel:
        return self._model

    @model.setter
    def model(self, value: ExampleModel) -> None:
        self._model = value

    @property
    def view(self) -> MainWindow:
        return self._view

    @view.setter
    def view(self, value: MainWindow) -> None:
        self._view = value

    def _connect_signals(self) -> None:
        self._model.counter_changed.connect(self._view.on_counter_changed)
        self._model.status_changed.connect(self._view.on_status_changed)
        self._model.error_occurred.connect(self._view.show_error)

        self._view.increment_requested.connect(self._on_increment)
        self._view.decrement_requested.connect(self._on_decrement)
        self._view.reset_requested.connect(self._on_reset)

    def _initialize(self) -> None:
        self._view.on_counter_changed(self._model.counter)
        self._view.on_status_changed(self._model.status)

    def _on_increment(self) -> None:
        self._model.increment()

    def _on_decrement(self) -> None:
        self._model.decrement()

    def _on_reset(self) -> None:
        self._model.reset()

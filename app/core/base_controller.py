from PyQt6.QtCore import QObject
from .base_model import BaseModel
from .base_view import BaseView


class BaseController(QObject):
    """
    Abstract base for all controllers.

    A controller owns exactly one model and one view.  Its sole
    responsibility is wiring signals between them and hosting the
    application logic that translates user actions into model mutations.

    Lifecycle
    ---------
    1. __init__ receives model and view instances.
    2. _connect_signals() wires model → view and view → controller slots.
    3. _initialize() populates the view with the model's initial state.

    Subclasses must implement:
        _connect_signals()
        _initialize()
    """

    def __init__(self, model: BaseModel, view: BaseView,
                 parent: QObject | None = None) -> None:
        super().__init__(parent)
        self.model = model
        self.view = view
        self._connect_signals()
        self._initialize()

    def _connect_signals(self) -> None:
        raise NotImplementedError

    def _initialize(self) -> None:
        raise NotImplementedError

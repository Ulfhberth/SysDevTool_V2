from PyQt6.QtCore import QObject, pyqtSignal


class BaseModel(QObject):
    """
    Abstract base for all models.

    Subclasses emit signals to notify observers (controllers/views) about
    state changes. No direct references to views or controllers are held —
    coupling happens exclusively via signals.
    """

    data_changed = pyqtSignal(str, object)
    error_occurred = pyqtSignal(str)

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self._data: dict[str, object] = {}

    def get(self, key: str, default: object = None) -> object:
        return self._data.get(key, default)

    def set(self, key: str, value: object) -> None:
        """Update a value and emit data_changed if the value actually changed."""
        if self._data.get(key) == value:
            return
        self._data[key] = value
        self.data_changed.emit(key, value)

    def set_many(self, updates: dict[str, object]) -> None:
        for key, value in updates.items():
            self.set(key, value)

    def _emit_error(self, message: str) -> None:
        self.error_occurred.emit(message)

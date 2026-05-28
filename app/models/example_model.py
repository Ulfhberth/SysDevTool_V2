from PyQt6.QtCore import pyqtSignal
from SysDevTool_V2.app.core import BaseModel


class ExampleModel(BaseModel):
    """
    Concrete model: maintains a counter and a status message.

    Signals
    -------
    counter_changed(int)   — emitted when the counter value changes
    status_changed(str)    — emitted when the status message changes
    """

    counter_changed = pyqtSignal(int)
    status_changed = pyqtSignal(str)

    _COUNTER_KEY = "counter"
    _STATUS_KEY = "status"

    def __init__(self) -> None:
        super().__init__()
        self._data[self._COUNTER_KEY] = 0
        self._data[self._STATUS_KEY] = "Bereit"

    @property
    def counter(self) -> int:
        return int(self._data[self._COUNTER_KEY])

    @property
    def status(self) -> str:
        return str(self._data[self._STATUS_KEY])

    def increment(self) -> None:
        new_value = self.counter + 1
        self._data[self._COUNTER_KEY] = new_value
        self.counter_changed.emit(new_value)
        self._update_status(f"Zähler erhöht auf {new_value}")

    def decrement(self) -> None:
        new_value = self.counter - 1
        self._data[self._COUNTER_KEY] = new_value
        self.counter_changed.emit(new_value)
        self._update_status(f"Zähler verringert auf {new_value}")

    def reset(self) -> None:
        self._data[self._COUNTER_KEY] = 0
        self.counter_changed.emit(0)
        self._update_status("Zähler zurückgesetzt")

    def _update_status(self, message: str) -> None:
        self._data[self._STATUS_KEY] = message
        self.status_changed.emit(message)

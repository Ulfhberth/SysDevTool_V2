class BaseView:
    """
    Mixin for all views — carries no Qt base class so that subclasses can
    freely choose QWidget, QMainWindow, QDialog, etc. as their Qt parent.

    Convention
    ----------
    Concrete __init__ must call _build_ui() and _connect_internal_signals()
    after the Qt base class is fully initialized.

    Subclasses must implement:
        _build_ui()                  — create and arrange widgets
        _connect_internal_signals()  — widget-to-widget wiring inside the view
    """

    def _build_ui(self) -> None:
        raise NotImplementedError

    def _connect_internal_signals(self) -> None:
        pass

    def show_error(self, message: str) -> None:
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.critical(self, "Fehler", message)  # type: ignore[arg-type]

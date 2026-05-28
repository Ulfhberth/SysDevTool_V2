import sys
from SysDevTool_V2.app.core import Application
from SysDevTool_V2.app.models import ExampleModel
from SysDevTool_V2.app.views import MainWindow
from SysDevTool_V2.app.controllers import MainController


def main() -> int:
    return Application(
        controller_cls=MainController,
        model_cls=ExampleModel,
        view_cls=MainWindow,
        app_name="SysDevTool V2",
    ).run()


if __name__ == "__main__":
    sys.exit(main())

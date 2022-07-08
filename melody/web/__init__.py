"""All your music, in one place."""

__description__ = "All your music, in one place."
__url__ = "https://github.com/MelodyKit/melody.web"

__title__ = "web"
__author__ = "MelodyKit"
__license__ = "MIT"
__version__ = "0.1.0"

from melody.web import modules
from melody.web.core import setup_app
from melody.web.main import create_and_run_app

__all__ = ("modules", "create_and_run_app", "setup_app")

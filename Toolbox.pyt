from pathlib import Path
from common import ModuleReloader

# Reload all modules in the current directory and its subdirectories
ModuleReloader(Path(__file__).parent).reload_all_modules()


class Toolbox:
    """Class that defines the toolbox.

    Attributes:
        label (str): The label for the toolbox.
        alias (str): The alias for the toolbox.
        tools (list[type]): The list of tools in the toolbox.
    """

    def __init__(self):
        """Initializes the Toolbox instance."""
        self.label: str = "Toolbox"
        self.alias: str = "Toolbox"

        self.tools: list[type] = []

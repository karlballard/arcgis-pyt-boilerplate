from importlib import import_module, reload
from pathlib import Path


class ModuleReloader:
    """Class to dynamically reload relative Python modules.

    ModuleReloader provides functionality to dynamically reload Python modules within a specified
    directory and optionally, its subdirectories.

    Attributes:
        base_path (Path): The base path of the project. This should be an absolute path.
    """

    def __init__(self, base_path: Path):
        """Initializes the instance using a provided base path.

        Args:
            base_path (Path): The base path of the project. This should be an absolute path.
        """
        self.base_path = base_path

    def build_module_name(self, module_path: Path) -> str:
        """Constructs the module name relative to the base path into dot notation.

        Args:
            module_path (Path): The path of the module file.

        Returns:
            str: The module name in dot notation.
        """
        return (module_path.relative_to(self.base_path).with_suffix("").as_posix()
                .replace("/", "."))

    def reload_module(self, module_path: Path) -> None:
        """Imports and reloads a single module based on its path.

        Args:
            module_path (Path): The path of the module file.

        Raises:
            ImportError: If the module fails to import or reload.
        """
        try:
            module_name = self.build_module_name(module_path)
            reload(import_module(module_name))
        except ImportError as e:
            raise ImportError(f"Failed to import or reload: {module_path} ({e})") from e

    def reload_all_modules(self, recursive: bool = True) -> None:
        """Reloads all Python modules within a specified directory and its subdirectories.

        Args:
            recursive (bool, optional): Whether to reload modules in subdirectories recursively.
                Defaults to True.

        Raises:
            ImportError: If a module fails to import or reload.
        """
        files_to_reload = self.base_path.rglob("*.py") if recursive else self.base_path.glob("*.py")

        for module_path in files_to_reload:
            self.reload_module(module_path)

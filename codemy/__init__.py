"""codemy top-level module"""
from importlib import metadata

__version__ = metadata.version("codemy")


def main() -> None:
    """Main entry function for codemy"""
    print("Hello world!")


# This statement is for running the project with:
# $ python codemy/__init__.py
if __name__ == "__main__":
    main()

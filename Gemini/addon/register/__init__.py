"""This module has the functions to register the other modules (folders).

This ``__init__.py`` represents the second phase of the registration initiated
in the ``<project_root>/Gemini/__init__.py`` file.

The registration happens in cascade. The ``__init__.py`` files in other modules
(folders) register each file inside the respective folder.

"""


def register_addon():
    """Registers each module folder."""

    # Properties
    from .. property import register_properties
    register_properties()

    # Menus
    from .. menu import register_menus
    register_menus()

    # Operators
    from .. operator import register_operators
    register_operators()

    # Keymaps
    from . keymap import register_keymap
    register_keymap()


def unregister_addon():
    """Unregisters each module folder."""

    # Properties
    from .. property import unregister_properties
    unregister_properties()

    # Menus
    from .. menu import unregister_menus
    unregister_menus()

    # Operators
    from .. operator import unregister_operators
    unregister_operators()

    # Keymaps
    from . keymap import unregister_keymap
    unregister_keymap()

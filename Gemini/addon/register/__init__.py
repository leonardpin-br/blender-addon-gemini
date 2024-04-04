"""This module has the functions to register the other modules.

The registration happens in cascade. The ``__init__.py`` files in other modules
(folders) register each file inside them.
"""


def register_addon():

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

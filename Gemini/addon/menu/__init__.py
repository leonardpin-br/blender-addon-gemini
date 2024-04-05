"""For Blender to be able to find the classes, they must be registered.

The ``__init__.py`` file registers locally all the menus in this module
folder.

"""

import bpy

from . main_menu import GEM_MT_Main_Menu

classes = (
    GEM_MT_Main_Menu,
)


def register_menus():
    """Registers all menu classes in this module folder.
    """
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_menus():
    """Unregisters all the menu classes in this module folder in reverse order.
    """
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

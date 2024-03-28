"""Last modified in 2024-03-13

Python version 3.10.13 (Blender 4.0.2)

References:
    `"Installing" bpy for Plugin Development in VSCode`_

.. _"Installing" bpy for Plugin Development in VSCode:
   https://blender.stackexchange.com/a/284197

"""

import bpy

from . main_menu import GEM_MT_Main_Menu

classes = (
    GEM_MT_Main_Menu,
)


def register_menus():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_menus():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

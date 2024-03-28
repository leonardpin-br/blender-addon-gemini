"""Last modified in 2024-03-12

Python version 3.10.13 (Blender 4.0.2)

References:
    `"Installing" bpy for Plugin Development in VSCode`_

.. _"Installing" bpy for Plugin Development in VSCode:
   https://blender.stackexchange.com/a/284197

"""

import bpy

from . add_lights import GEM_OP_Add_Lights
from . solidify import GEM_OP_Solidify
from . ray_caster import GEM_OP_Ray

classes = (
    GEM_OP_Add_Lights,
    GEM_OP_Solidify,
    GEM_OP_Ray
)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

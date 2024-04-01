"""For Blender to be able to find the classes, the must be registered.

Thes ``__init__.py`` file registers all the operators in this module folder.

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
    """Registers all classes in this module folder.
    """

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_operators():
    """Unregister all the classes in this module folder in reverse order.
    """

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

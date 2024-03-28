import bpy

from . addon import GEM_Props
from . color import GEM_Color
from . settings import GEM_Settings

classes = (
    GEM_Color,
    GEM_Settings,
    GEM_Props
)


def register_properties():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_properties():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
